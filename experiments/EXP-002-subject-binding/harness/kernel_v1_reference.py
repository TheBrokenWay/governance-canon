"""
Minimal reference kernel for Triple Governance.

Written to a plain reading of canon/TRIPLE_GOVERNANCE.md sections 6 and 7.
No dependency on any operational product. Standard library only.

This is a reference implementation for testing the specification. It is not a
production governance system and makes no claim to be one.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import hashlib
import json
import time


# --------------------------------------------------------------------------
# Section 6.0 — the four authoritative subjects
# --------------------------------------------------------------------------

class Subject(str, Enum):
    CONCEPT_FORMULATION = "ConceptFormulation"
    CLAIM_PROTOCOL = "ClaimProtocol"
    CLAIM_STATE_REVISION = "ClaimStateRevision"
    OPERATIONAL_REQUEST = "OperationalRequest"


class Constitution(str, Enum):
    STRUCTURAL = "structural"
    SCIENTIFIC = "scientific"
    OPERATIONAL = "operational"


# Which constitution adjudicates which subject. Section 6.0's table.
SUBJECT_AUTHORITY = {
    Subject.CONCEPT_FORMULATION: Constitution.STRUCTURAL,
    Subject.CLAIM_PROTOCOL: Constitution.SCIENTIFIC,
    Subject.CLAIM_STATE_REVISION: Constitution.SCIENTIFIC,
    Subject.OPERATIONAL_REQUEST: Constitution.OPERATIONAL,
}


# --------------------------------------------------------------------------
# Sections 6.1-6.3 — gate outputs, kept as distinct vocabularies per constitution
# --------------------------------------------------------------------------

STRUCTURAL_OUTPUTS = {"REGISTERED", "STRUCTURALLY_ADMISSIBLE",
                      "STRUCTURALLY_REJECTED", "NEEDS_REVISION"}

SCIENTIFIC_PROTOCOL_OUTPUTS = {"SCIENTIFICALLY_ADMISSIBLE_FOR_TEST",
                               "NEEDS_REVISION", "INADMISSIBLE_PROTOCOL"}

SCIENTIFIC_CLAIM_OUTPUTS = {"UNRESOLVED", "SUPPORTED_UNDER_SCOPE", "WEAKENED",
                            "CONTRADICTED", "SUPERSEDED"}

OPERATIONAL_OUTPUTS = {"SANDBOX_ONLY", "EXPERIMENT_APPROVED", "SHADOW_APPROVED",
                       "DEPLOYMENT_APPROVED", "REJECTED_FOR_OPERATION", "ROLLED_BACK"}

# The outputs that permit an action to proceed under each constitution.
PASSING = {
    Constitution.STRUCTURAL: {"REGISTERED", "STRUCTURALLY_ADMISSIBLE"},
    Constitution.SCIENTIFIC: {"SCIENTIFICALLY_ADMISSIBLE_FOR_TEST",
                              "SUPPORTED_UNDER_SCOPE"},
    Constitution.OPERATIONAL: {"EXPERIMENT_APPROVED", "SHADOW_APPROVED",
                               "DEPLOYMENT_APPROVED"},
}

VALID_OUTPUTS = {
    Constitution.STRUCTURAL: STRUCTURAL_OUTPUTS,
    Constitution.SCIENTIFIC: SCIENTIFIC_PROTOCOL_OUTPUTS | SCIENTIFIC_CLAIM_OUTPUTS,
    Constitution.OPERATIONAL: OPERATIONAL_OUTPUTS,
}


class Violation(Exception):
    """Raised when a caller attempts something the constitutions forbid outright."""


# --------------------------------------------------------------------------
# Receipts
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Receipt:
    """One gate's decision about one subject. Issued by one constitution only."""
    constitution: Constitution
    subject: Subject
    subject_version: str
    output: str
    issuer: str
    issued_at: float = field(default_factory=time.time)

    def __post_init__(self):
        if self.output not in VALID_OUTPUTS[self.constitution]:
            raise Violation(
                f"{self.constitution.value} cannot emit '{self.output}' — "
                f"not in its output vocabulary"
            )
        # Invariant 14: one issuer cannot satisfy multiple authority classes.
        # Enforced at the kernel level in adjudicate().

    @property
    def passed(self) -> bool:
        return self.output in PASSING[self.constitution]

    def digest(self) -> str:
        return hashlib.sha256(json.dumps({
            "constitution": self.constitution.value,
            "subject": self.subject.value,
            "subject_version": self.subject_version,
            "output": self.output,
            "issuer": self.issuer,
        }, sort_keys=True).encode()).hexdigest()


@dataclass(frozen=True)
class WitnessObservation:
    """Section 6.4. A witness records and may trigger review. It cannot mint authority."""
    observer: str
    note: str
    # A witness may request review or revocation. It has no field that grants a pass,
    # by construction: there is nowhere to put one.
    requests_review: bool = False


@dataclass
class Amendment:
    """Section 2 amendment rule: prospective only, never retroactive."""
    text: str
    lowers_strictness: bool
    submitted_at: float = field(default_factory=time.time)


# --------------------------------------------------------------------------
# The request
# --------------------------------------------------------------------------

@dataclass
class Request:
    subject: Subject
    subject_version: str
    description: str
    receipts: list[Receipt] = field(default_factory=list)
    witnesses: list[WitnessObservation] = field(default_factory=list)
    # Channels a caller may try to use to compensate for a failure:
    claimed_override: Optional[str] = None      # probe D
    bypass_token: Optional[str] = None          # probe E
    composite_score: Optional[float] = None     # probe G
    pending_amendment: Optional[Amendment] = None  # probe H


@dataclass
class Decision:
    verdict: str            # "EXECUTE" or "REFUSE"
    reasons: list[str]
    receipts: list[str]     # receipt digests, custody only
    violations: list[str]


# --------------------------------------------------------------------------
# Which constitutions must pass for a given subject
# --------------------------------------------------------------------------

def required_constitutions(subject: Subject) -> set[Constitution]:
    """
    Invariant 9: a production decision based on a scientific claim requires all relevant
    gates, each receipt separate. An OperationalRequest that acts on a claim is the case
    that needs all three.
    """
    if subject is Subject.OPERATIONAL_REQUEST:
        return {Constitution.STRUCTURAL, Constitution.SCIENTIFIC, Constitution.OPERATIONAL}
    if subject in (Subject.CLAIM_PROTOCOL, Subject.CLAIM_STATE_REVISION):
        return {Constitution.STRUCTURAL, Constitution.SCIENTIFIC}
    return {Constitution.STRUCTURAL}


# --------------------------------------------------------------------------
# Adjudication
# --------------------------------------------------------------------------

def adjudicate(req: Request) -> Decision:
    reasons: list[str] = []
    violations: list[str] = []

    # --- Invariant 15 / receipt containment: a composite score is not an input. ---
    if req.composite_score is not None:
        violations.append(
            "composite score supplied; non-compensable rules cannot be averaged "
            "(invariant 2: gate decisions are not averaged into a scalar)"
        )

    # --- Section 6.4: a witness cannot mint authority. ---
    if req.bypass_token is not None:
        violations.append(
            "bypass token supplied; the witness plane cannot mint structural, "
            "scientific, or operational authority (section 6.4)"
        )

    # --- Invariants 3,4,5: no constitution may override another's failure. ---
    if req.claimed_override is not None:
        violations.append(
            f"override claimed ({req.claimed_override}); "
            "operational approval cannot make a scientific claim true (invariant 5)"
        )

    # --- Section 2 amendment rule: prospective only. ---
    if req.pending_amendment is not None:
        if req.pending_amendment.lowers_strictness:
            violations.append(
                "amendment lowering strictness submitted during adjudication; "
                "a revision cannot be applied retroactively to a decision in progress. "
                "Deferred to the next protocol version."
            )
        reasons.append("pending amendment deferred; baseline strictness locked for this run")

    # --- Section 6.0: the subject determines the authority. ---
    for r in req.receipts:
        if r.subject != req.subject:
            violations.append(
                f"receipt for subject {r.subject.value} presented against a request "
                f"for subject {req.subject.value} (section 6.0: authoritative subject "
                f"mismatch)"
            )
        expected = SUBJECT_AUTHORITY[r.subject]
        if r.constitution is not expected and r.constitution not in required_constitutions(req.subject):
            violations.append(
                f"{r.constitution.value} issued a receipt for {r.subject.value}, "
                f"which is adjudicated by {expected.value}"
            )

    # --- Invariant 14: no single issuer across authority classes. ---
    issuers: dict[str, set[Constitution]] = {}
    for r in req.receipts:
        issuers.setdefault(r.issuer, set()).add(r.constitution)
    for issuer, consts in issuers.items():
        if len(consts) > 1:
            violations.append(
                f"issuer '{issuer}' signed for {sorted(c.value for c in consts)}; "
                "a single issuer cannot satisfy multiple constitutions (invariant 14)"
            )

    # --- Invariant 1: every required gate must pass on its own. No compensation. ---
    needed = required_constitutions(req.subject)
    by_const: dict[Constitution, list[Receipt]] = {}
    for r in req.receipts:
        by_const.setdefault(r.constitution, []).append(r)

    for c in sorted(needed, key=lambda x: x.value):
        rs = by_const.get(c, [])
        if not rs:
            violations.append(f"no {c.value} receipt; required for {req.subject.value}")
            continue
        if not all(r.passed for r in rs):
            failed = [r.output for r in rs if not r.passed]
            violations.append(
                f"{c.value} gate failed ({', '.join(failed)}); "
                "two passes cannot compensate for one failure (invariant 1)"
            )

    # --- Invariant 4: scientific support is not operational authorization. ---
    if req.subject is Subject.OPERATIONAL_REQUEST:
        op = by_const.get(Constitution.OPERATIONAL, [])
        if not op:
            violations.append(
                "operational authorization absent; scientific support cannot "
                "authorize deployment (invariant 4)"
            )

    verdict = "REFUSE" if violations else "EXECUTE"
    if verdict == "EXECUTE":
        reasons.append("all required gates passed independently")

    return Decision(
        verdict=verdict,
        reasons=reasons,
        receipts=[r.digest() for r in req.receipts],
        violations=violations,
    )
