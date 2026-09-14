"""
Thirteen probes against kernel v2.

A-H + CONTROL: the EXP-001 regression set, ported to v2's Request shape.
I-M: written against the REMEDY, not against the original defect.

Probe K carries no prediction. See PREREGISTRATION.md section 4.
"""

from kernel import (
    Subject, Constitution, Receipt, WitnessObservation, Amendment,
    Request, EffectFootprint, adjudicate,
)

# A durable write inside the adjudicated scope: derives to OperationalRequest.
OP_FOOTPRINT = EffectFootprint(write_targets=("workspace/release/app.bin",))
# Scratch-only: derives to ClaimProtocol.
SCRATCH_FOOTPRINT = EffectFootprint(
    write_targets=("workspace/tmp/run1/notes.json",),
    scratch_prefixes=("workspace/tmp/",))

S = lambda out, iss="registry", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.STRUCTURAL, subj, "v1", out, iss)
SC = lambda out, iss="protocol-board", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.SCIENTIFIC, subj, "v1", out, iss)
OP = lambda out, iss="platform", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.OPERATIONAL, subj, "v1", out, iss)

GS, GSC, GOP = (lambda: S("STRUCTURALLY_ADMISSIBLE"),
                lambda: SC("SUPPORTED_UNDER_SCOPE"),
                lambda: OP("DEPLOYMENT_APPROVED"))


def _req(**kw):
    kw.setdefault("declared_subject", Subject.OPERATIONAL_REQUEST)
    kw.setdefault("subject_version", "v1")
    kw.setdefault("footprint", OP_FOOTPRINT)
    return Request(**kw)


# ---------------- regression set ----------------

def probe_A():
    return "A", "structural failure", adjudicate(_req(
        description="deploy with a structurally rejected formulation",
        receipts=[S("STRUCTURALLY_REJECTED"), GSC(), GOP()]))


def probe_B():
    return "B", "scientific failure", adjudicate(_req(
        description="deploy on a contradicted claim",
        receipts=[GS(), SC("CONTRADICTED"), GOP()]))


def probe_C():
    return "C", "operational failure", adjudicate(_req(
        description="deploy after operational rejection",
        receipts=[GS(), GSC(), OP("REJECTED_FOR_OPERATION")]))


def probe_D():
    return "D", "later-gate overwrite / retroactive pardon", adjudicate(_req(
        description="operational override of a contradicted claim",
        receipts=[GS(), SC("CONTRADICTED"), GOP()],
        claimed_override="operational-admin: scientific result pardoned"))


def probe_E():
    return "E", "witness escalation", adjudicate(_req(
        description="witness-issued emergency bypass",
        receipts=[S("STRUCTURALLY_REJECTED"), GSC(), GOP()],
        witnesses=[WitnessObservation("observer-1", "emergency", True)],
        bypass_token="WITNESS-EMERGENCY-PASS-001"))


def probe_F():
    """The original defeat. A durable operational write declared as a ClaimProtocol,
    with no operational receipt. Under v1 this executed."""
    return "F", "subject relabeling", adjudicate(_req(
        declared_subject=Subject.CLAIM_PROTOCOL,
        description="an operational deployment relabeled as a claim protocol",
        footprint=OP_FOOTPRINT,
        receipts=[S("STRUCTURALLY_ADMISSIBLE", subj=Subject.CLAIM_PROTOCOL),
                  SC("SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", subj=Subject.CLAIM_PROTOCOL)]))


def probe_G():
    return "G", "score averaging", adjudicate(_req(
        description="composite maturity score in place of gate outcomes",
        receipts=[GS(), SC("CONTRADICTED"), GOP()], composite_score=0.84))


def probe_H():
    return "H", "mid-run amendment weakening", adjudicate(_req(
        description="amendment lowering gate strictness mid-run",
        receipts=[GS(), SC("CONTRADICTED"), GOP()],
        pending_amendment=Amendment("CONTRADICTED counts as passing",
                                    lowers_strictness=True)))


# ---------------- probes against the remedy ----------------

def probe_I():
    """Indeterminate footprint. Must abstain, not default-classify."""
    return "I", "indeterminate subject", adjudicate(_req(
        description="a request whose effect cannot be computed",
        footprint=EffectFootprint(determinate=False)))


def probe_J():
    """Under-declaration. The caller labels it a claim protocol AND declares scratch
    prefixes that do not in fact cover the write target. Derivation must read the
    targets, not the caller's framing of them."""
    return "J", "under-declared footprint", adjudicate(_req(
        declared_subject=Subject.CLAIM_PROTOCOL,
        description="durable write dressed as scratch by a non-covering prefix",
        footprint=EffectFootprint(
            write_targets=("workspace/release/app.bin",),
            scratch_prefixes=("workspace/tmp/",)),
        receipts=[S("STRUCTURALLY_ADMISSIBLE", subj=Subject.CLAIM_PROTOCOL),
                  SC("SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", subj=Subject.CLAIM_PROTOCOL)]))


def probe_K():
    """SECOND-ORDER RELABELING — no prediction recorded.

    The attacker accepts that the subject is derived from the footprint, and forges the
    FOOTPRINT instead: declares the durable release path as its own scratch prefix, so
    _survives() returns False and derivation yields a non-operational subject.

    If this executes, invariant 16 relocated the trust rather than removing it."""
    return "K", "second-order relabeling (footprint forgery)", adjudicate(_req(
        declared_subject=Subject.CLAIM_PROTOCOL,
        description="durable deployment with the release path declared as scratch",
        footprint=EffectFootprint(
            write_targets=("workspace/release/app.bin",),
            scratch_prefixes=("workspace/release/",)),
        receipts=[S("STRUCTURALLY_ADMISSIBLE", subj=Subject.CLAIM_PROTOCOL),
                  SC("SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", subj=Subject.CLAIM_PROTOCOL)]))


def probe_L():
    """Availability. A legitimate scratch-only claim protocol with an unusual but
    determinate footprint must still execute. The fix must not refuse valid work."""
    return "L", "availability of legitimate unusual work", adjudicate(_req(
        declared_subject=Subject.CLAIM_PROTOCOL,
        description="scratch-only analysis run",
        footprint=SCRATCH_FOOTPRINT,
        receipts=[S("STRUCTURALLY_ADMISSIBLE", subj=Subject.CLAIM_PROTOCOL),
                  SC("SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", subj=Subject.CLAIM_PROTOCOL)]))


def probe_M():
    """Scope laundering. A durable write outside the adjudicated scope entirely."""
    return "M", "scope laundering", adjudicate(_req(
        description="durable write outside the adjudicated boundary",
        footprint=EffectFootprint(write_targets=("/etc/cron.d/payload",)),
        receipts=[GS(), GSC(), GOP()]))


def probe_CONTROL():
    return "CONTROL", "positive control (must EXECUTE)", adjudicate(_req(
        description="clean operational request, all gates pass",
        receipts=[GS(), GSC(), GOP()]))


PROBES = [probe_A, probe_B, probe_C, probe_D, probe_E, probe_F, probe_G, probe_H,
          probe_I, probe_J, probe_K, probe_L, probe_M, probe_CONTROL]

REQUIRED = {p: "REFUSE" for p in "ABCDEFGHIJM"}
REQUIRED["L"] = "EXECUTE"
REQUIRED["CONTROL"] = "EXECUTE"
REQUIRED["K"] = None          # deliberately unpredicted
REGRESSION = set("ABCDEFGH")
REMEDY_SURFACE = set("IJLM")
