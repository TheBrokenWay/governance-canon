"""
Triple Governance reference kernel, version 3.

v1: authority from a caller-supplied subject label.          Probe F defeated it.
v2: authority derived from a caller-supplied effect footprint. Probe K defeated it.
v3: every derivation input is kernel-controlled or self-limiting.

The rule this version implements, from DERIVATION_INPUT_AUDIT.md:

    A derivation input is safe only if it is kernel-controlled, or if misdeclaring it
    defeats the attacker's own purpose. Every other input is a K.

Changes from v2:
  - Scratch is kernel-ALLOCATED. The caller receives a prefix and cannot declare one.
  - Externality is DERIVED against a kernel boundary. The field is removed from the
    caller's reach: a field that cannot be sent cannot be lied about.
  - Determinacy is ESTABLISHED by the kernel. An empty or absent footprint is
    indeterminate, not "no effect".

Standard library only. No product bindings.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import hashlib
import json
import secrets
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
# Kernel-controlled boundary constants. Not reachable by any caller.
# --------------------------------------------------------------------------

ADJUDICATED_SCOPE = ("workspace/",)
SCRATCH_ROOT = "workspace/.scratch/"


class ScratchAllocator:
    """Issues per-request scratch prefixes and remembers which request owns each.

    The caller receives a prefix. It cannot name one. It cannot widen one.
    """

    def __init__(self) -> None:
        self._issued: dict[str, str] = {}   # prefix -> request_id

    def allocate(self, request_id: str) -> str:
        prefix = f"{SCRATCH_ROOT}{secrets.token_hex(8)}/"
        self._issued[prefix] = request_id
        return prefix

    def owner(self, prefix: str) -> Optional[str]:
        return self._issued.get(prefix)


ALLOCATOR = ScratchAllocator()


# --------------------------------------------------------------------------
# The caller's declaration. Deliberately narrow.
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class EffectFootprint:
    """
    What the request will touch.

    `write_targets` and `read_targets` are caller-supplied and SELF-LIMITING: the
    executor acts on exactly these values, so understating one sends the effect
    elsewhere rather than sneaking it past a gate.

    `scratch_grant` is a prefix the caller RECEIVED from the allocator. It is not a
    declaration; it is a token, and it is checked against the issuing record.

    There is no `external` field and no `determinate` field. Both were caller-supplied
    in v2 and neither was self-limiting. Externality and determinacy are now decided
    by the kernel (see derive_subject).
    """
    write_targets: tuple[str, ...] = ()
    read_targets: tuple[str, ...] = ()
    scratch_grant: Optional[str] = None
    declared: bool = False      # set True by make_footprint(); a raw() footprint is not


def make_footprint(write_targets=(), read_targets=(), scratch_grant=None) -> EffectFootprint:
    """The only supported way to build a footprint. Marks it as actually declared."""
    return EffectFootprint(tuple(write_targets), tuple(read_targets), scratch_grant, True)


# --------------------------------------------------------------------------
# Derivation. Every input below is kernel-controlled or self-limiting.
# --------------------------------------------------------------------------

def _in_scope(target: str) -> bool:
    return any(target.startswith(s) for s in ADJUDICATED_SCOPE)


def _is_granted_scratch(target: str, fp: EffectFootprint, request_id: str) -> bool:
    """A write counts as scratch only if it lands under a prefix this request was issued."""
    g = fp.scratch_grant
    if not g:
        return False
    if not g.startswith(SCRATCH_ROOT):
        return False                          # not a kernel-issued shape
    if ALLOCATOR.owner(g) != request_id:
        return False                          # issued to some other request, or never issued
    return target.startswith(g)


def derive_subject(fp: EffectFootprint, request_id: str) -> tuple[Optional[Subject], list[str]]:
    notes: list[str] = []

    # Determinacy is established here, not declared.
    if not fp.declared:
        notes.append("no footprint was declared through the kernel's own path")
        return None, notes
    if not fp.write_targets and not fp.read_targets:
        notes.append("footprint declares no target; the effect cannot be established")
        return None, notes

    durable = [t for t in fp.write_targets if not _is_granted_scratch(t, fp, request_id)]
    # Externality is derived against the kernel boundary, never declared.
    outside = [t for t in (fp.write_targets + fp.read_targets) if not _in_scope(t)]

    if outside:
        notes.append(f"targets outside the adjudicated boundary: {outside}")
        return Subject.OPERATIONAL_REQUEST, notes
    if durable:
        notes.append(f"durable writes derived from targets and grant: {durable}")
        return Subject.OPERATIONAL_REQUEST, notes
    if fp.write_targets:
        notes.append("all writes land in this request's issued scratch")
        return Subject.CLAIM_PROTOCOL, notes
    notes.append("read-only effect")
    return Subject.CLAIM_PROTOCOL, notes


def scope_violations(fp: EffectFootprint, request_id: str) -> list[str]:
    out = []
    for t in fp.write_targets:
        if not _is_granted_scratch(t, fp, request_id) and not _in_scope(t):
            out.append(f"durable write to '{t}' lies outside the adjudicated scope "
                       f"{list(ADJUDICATED_SCOPE)}; the kernel cannot govern it and will "
                       f"not authorize it")
    if fp.scratch_grant and ALLOCATOR.owner(fp.scratch_grant) not in (None, request_id):
        out.append(f"scratch grant '{fp.scratch_grant}' was issued to a different request; "
                   f"grants are not transferable")
    if fp.scratch_grant and ALLOCATOR.owner(fp.scratch_grant) is None:
        out.append(f"scratch grant '{fp.scratch_grant}' was never issued by this kernel")
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
            raise Violation(f"{self.constitution.value} cannot emit '{self.output}'")

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
    declared_subject: Subject
    subject_version: str
    description: str
    request_id: str = field(default_factory=lambda: secrets.token_hex(6))
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

    derived, notes = derive_subject(req.footprint, req.request_id)
    reasons.extend(notes)

    if derived is None:
        violations.append(
            "INDETERMINATE_SUBJECT: the kernel could not establish the effect. Abstention "
            "is required; an undeclared or empty footprint is not 'no effect' (invariant 16)")
        return Decision("REFUSE", None, reasons,
                        [r.digest() for r in req.receipts], violations)

    if derived is not req.declared_subject:
        violations.append(
            f"SUBJECT_BINDING_VIOLATION: declared '{req.declared_subject.value}', derived "
            f"'{derived.value}'. Recorded against the requester (invariant 16)")

    violations.extend(scope_violations(req.footprint, req.request_id))
    subject = derived

    if req.composite_score is not None:
        violations.append("composite score supplied; gate decisions are not averaged "
                          "into a scalar (invariant 2)")
    if req.bypass_token is not None:
        violations.append("bypass token supplied; the witness plane cannot mint authority "
                          "(section 6.4)")
    if req.claimed_override is not None:
        violations.append(f"override claimed ({req.claimed_override}); operational approval "
                          f"cannot make a scientific claim true (invariant 5)")
    if req.pending_amendment is not None:
        if req.pending_amendment.lowers_strictness:
            violations.append("amendment lowering strictness submitted during adjudication; "
                              "revisions are prospective only")
        reasons.append("pending amendment deferred; baseline locked for this run")

    issuers: dict[str, set[Constitution]] = {}
    for r in req.receipts:
        issuers.setdefault(r.issuer, set()).add(r.constitution)
    for issuer, consts in issuers.items():
        if len(consts) > 1:
            violations.append(f"issuer '{issuer}' signed for "
                              f"{sorted(c.value for c in consts)}; a single issuer cannot "
                              f"satisfy multiple constitutions (invariant 14)")

    by_const: dict[Constitution, list[Receipt]] = {}
    for r in req.receipts:
        by_const.setdefault(r.constitution, []).append(r)
    for c in sorted(required_constitutions(subject), key=lambda x: x.value):
        rs = by_const.get(c, [])
        if not rs:
            violations.append(f"no {c.value} receipt; required for derived subject "
                              f"{subject.value}")
            continue
        if not all(r.passed for r in rs):
            failed = [r.output for r in rs if not r.passed]
            violations.append(f"{c.value} gate failed ({', '.join(failed)}); two passes "
                              f"cannot compensate for one failure (invariant 1)")

    verdict = "REFUSE" if violations else "EXECUTE"
    if verdict == "EXECUTE":
        reasons.append(f"all gates required by the derived subject {subject.value} passed "
                       f"independently")
    return Decision(verdict, subject.value, reasons,
                    [r.digest() for r in req.receipts], violations)
