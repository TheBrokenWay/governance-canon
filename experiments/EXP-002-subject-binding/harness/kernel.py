"""
Triple Governance reference kernel, version 2.

v1 (EXP-001) assigned adjudicative authority from a caller-supplied `subject` label.
Probe F defeated it: an operational deployment declared as a ClaimProtocol executed with
zero violations, because the operational gate was never required.

v2 implements proposed invariant 16 — subject binding. The authoritative subject is
DERIVED from the request's effect footprint. The declared label is retained and carries
no authority.

Standard library only. No dependency on any operational product.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import hashlib
import json
import time


class Subject(str, Enum):
    CONCEPT_FORMULATION = "ConceptFormulation"
    CLAIM_PROTOCOL = "ClaimProtocol"
    CLAIM_STATE_REVISION = "ClaimStateRevision"
    OPERATIONAL_REQUEST = "OperationalRequest"


class Constitution(str, Enum):
    STRUCTURAL = "structural"
    SCIENTIFIC = "scientific"
    OPERATIONAL = "operational"


SUBJECT_AUTHORITY = {
    Subject.CONCEPT_FORMULATION: Constitution.STRUCTURAL,
    Subject.CLAIM_PROTOCOL: Constitution.SCIENTIFIC,
    Subject.CLAIM_STATE_REVISION: Constitution.SCIENTIFIC,
    Subject.OPERATIONAL_REQUEST: Constitution.OPERATIONAL,
}

STRUCTURAL_OUTPUTS = {"REGISTERED", "STRUCTURALLY_ADMISSIBLE",
                      "STRUCTURALLY_REJECTED", "NEEDS_REVISION"}
SCIENTIFIC_OUTPUTS = {"SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", "NEEDS_REVISION",
                      "INADMISSIBLE_PROTOCOL", "UNRESOLVED", "SUPPORTED_UNDER_SCOPE",
                      "WEAKENED", "CONTRADICTED", "SUPERSEDED"}
OPERATIONAL_OUTPUTS = {"SANDBOX_ONLY", "EXPERIMENT_APPROVED", "SHADOW_APPROVED",
                       "DEPLOYMENT_APPROVED", "REJECTED_FOR_OPERATION", "ROLLED_BACK"}

PASSING = {
    Constitution.STRUCTURAL: {"REGISTERED", "STRUCTURALLY_ADMISSIBLE"},
    Constitution.SCIENTIFIC: {"SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", "SUPPORTED_UNDER_SCOPE"},
    Constitution.OPERATIONAL: {"EXPERIMENT_APPROVED", "SHADOW_APPROVED",
                               "DEPLOYMENT_APPROVED"},
}
VALID_OUTPUTS = {
    Constitution.STRUCTURAL: STRUCTURAL_OUTPUTS,
    Constitution.SCIENTIFIC: SCIENTIFIC_OUTPUTS,
    Constitution.OPERATIONAL: OPERATIONAL_OUTPUTS,
}


class Violation(Exception):
    pass


# --------------------------------------------------------------------------
# INVARIANT 16 — subject binding
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class EffectFootprint:
    """
    What the request would actually touch. These are the request's own operating
    parameters — the same values the executor would act on — not a summary of them.

    `durable` is NOT a caller assertion about durability. It is derived below from
    whether any write target survives the request's lifetime, which is a property of
    the target itself.
    """
    write_targets: tuple[str, ...] = ()      # paths/resources the request writes
    read_targets: tuple[str, ...] = ()
    scratch_prefixes: tuple[str, ...] = ()   # locations reclaimed at request end
    external: bool = False                   # reaches beyond the adjudicated boundary
    determinate: bool = True                 # False when the effect cannot be computed


# The scope this kernel is authorized to adjudicate over. Not caller-supplied.
ADJUDICATED_SCOPE = ("workspace/",)


def _survives(target: str, fp: EffectFootprint) -> bool:
    """A write is durable unless it lands entirely in declared scratch."""
    return not any(target.startswith(p) for p in fp.scratch_prefixes)


def derive_subject(fp: EffectFootprint) -> tuple[Optional[Subject], list[str]]:
    """
    Derive the authoritative subject from the footprint. Returns (subject, notes).
    A None subject means indeterminate: abstention is required, not a default.
    """
    notes: list[str] = []
    if not fp.determinate:
        notes.append("effect footprint is not determinate")
        return None, notes

    durable_writes = [t for t in fp.write_targets if _survives(t, fp)]
    if durable_writes or fp.external:
        notes.append(
            f"durable or external effect derived from parameters: {durable_writes or 'external'}"
        )
        return Subject.OPERATIONAL_REQUEST, notes

    if fp.write_targets:
        notes.append("writes confined to declared scratch; not an operational effect")
    if not fp.write_targets and not fp.read_targets:
        notes.append("no effect on any target")
        return Subject.CONCEPT_FORMULATION, notes

    notes.append("read-only or scratch-only effect")
    return Subject.CLAIM_PROTOCOL, notes


def scope_violations(fp: EffectFootprint) -> list[str]:
    """Invariant 16 corollary: a durable write outside the adjudicated scope is refused."""
    out = []
    for t in fp.write_targets:
        if _survives(t, fp) and not any(t.startswith(s) for s in ADJUDICATED_SCOPE):
            out.append(
                f"durable write to '{t}' lies outside the adjudicated scope "
                f"{list(ADJUDICATED_SCOPE)}; the kernel cannot govern it and will not "
                f"authorize it"
            )
    return out


# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Receipt:
    constitution: Constitution
    subject: Subject
    subject_version: str
    output: str
    issuer: str
    issued_at: float = field(default_factory=time.time)

    def __post_init__(self):
        if self.output not in VALID_OUTPUTS[self.constitution]:
            raise Violation(
                f"{self.constitution.value} cannot emit '{self.output}'")

    @property
    def passed(self) -> bool:
        return self.output in PASSING[self.constitution]

    def digest(self) -> str:
        return hashlib.sha256(json.dumps({
            "constitution": self.constitution.value, "subject": self.subject.value,
            "subject_version": self.subject_version, "output": self.output,
            "issuer": self.issuer}, sort_keys=True).encode()).hexdigest()


@dataclass(frozen=True)
class WitnessObservation:
    observer: str
    note: str
    requests_review: bool = False


@dataclass
class Amendment:
    text: str
    lowers_strictness: bool
    submitted_at: float = field(default_factory=time.time)


@dataclass
class Request:
    declared_subject: Subject          # retained; carries no authority
    subject_version: str
    description: str
    footprint: EffectFootprint = field(default_factory=EffectFootprint)
    receipts: list[Receipt] = field(default_factory=list)
    witnesses: list[WitnessObservation] = field(default_factory=list)
    claimed_override: Optional[str] = None
    bypass_token: Optional[str] = None
    composite_score: Optional[float] = None
    pending_amendment: Optional[Amendment] = None


@dataclass
class Decision:
    verdict: str
    derived_subject: Optional[str]
    reasons: list[str]
    receipts: list[str]
    violations: list[str]


def required_constitutions(subject: Subject) -> set[Constitution]:
    if subject is Subject.OPERATIONAL_REQUEST:
        return {Constitution.STRUCTURAL, Constitution.SCIENTIFIC, Constitution.OPERATIONAL}
    if subject in (Subject.CLAIM_PROTOCOL, Subject.CLAIM_STATE_REVISION):
        return {Constitution.STRUCTURAL, Constitution.SCIENTIFIC}
    return {Constitution.STRUCTURAL}


def adjudicate(req: Request) -> Decision:
    reasons: list[str] = []
    violations: list[str] = []

    # ---- INVARIANT 16, first: authority is derived before anything is checked ----
    derived, notes = derive_subject(req.footprint)
    reasons.extend(notes)

    if derived is None:
        violations.append(
            "INDETERMINATE_SUBJECT: the effect could not be derived from the request's "
            "parameters. Abstention is required; no default classification is applied "
            "(invariant 16)"
        )
        return Decision("REFUSE", None, reasons, [r.digest() for r in req.receipts],
                        violations)

    if derived is not req.declared_subject:
        violations.append(
            f"SUBJECT_BINDING_VIOLATION: declared '{req.declared_subject.value}', "
            f"derived '{derived.value}' from the effect footprint. Recorded against the "
            f"requester (invariant 16)"
        )

    violations.extend(scope_violations(req.footprint))

    subject = derived   # authority follows the derivation, never the label

    # ---- the v1 checks, unchanged ----
    if req.composite_score is not None:
        violations.append(
            "composite score supplied; gate decisions are not averaged into a scalar "
            "(invariant 2)")
    if req.bypass_token is not None:
        violations.append(
            "bypass token supplied; the witness plane cannot mint authority (section 6.4)")
    if req.claimed_override is not None:
        violations.append(
            f"override claimed ({req.claimed_override}); operational approval cannot make "
            f"a scientific claim true (invariant 5)")
    if req.pending_amendment is not None:
        if req.pending_amendment.lowers_strictness:
            violations.append(
                "amendment lowering strictness submitted during adjudication; revisions are "
                "prospective only")
        reasons.append("pending amendment deferred; baseline locked for this run")

    issuers: dict[str, set[Constitution]] = {}
    for r in req.receipts:
        issuers.setdefault(r.issuer, set()).add(r.constitution)
    for issuer, consts in issuers.items():
        if len(consts) > 1:
            violations.append(
                f"issuer '{issuer}' signed for {sorted(c.value for c in consts)}; a single "
                f"issuer cannot satisfy multiple constitutions (invariant 14)")

    needed = required_constitutions(subject)
    by_const: dict[Constitution, list[Receipt]] = {}
    for r in req.receipts:
        by_const.setdefault(r.constitution, []).append(r)

    for c in sorted(needed, key=lambda x: x.value):
        rs = by_const.get(c, [])
        if not rs:
            violations.append(
                f"no {c.value} receipt; required for derived subject {subject.value}")
            continue
        if not all(r.passed for r in rs):
            failed = [r.output for r in rs if not r.passed]
            violations.append(
                f"{c.value} gate failed ({', '.join(failed)}); two passes cannot "
                f"compensate for one failure (invariant 1)")

    verdict = "REFUSE" if violations else "EXECUTE"
    if verdict == "EXECUTE":
        reasons.append(
            f"all gates required by the DERIVED subject {subject.value} passed independently")

    return Decision(verdict, subject.value, reasons,
                    [r.digest() for r in req.receipts], violations)
