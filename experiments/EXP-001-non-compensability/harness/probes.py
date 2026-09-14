"""
Eight adversarial probes against the Triple Governance reference kernel.

Written against canon/TRIPLE_GOVERNANCE.md sections 6 and 7, with the explicit goal
of finding a path the kernel permits. Probes A-C are single-gate failures. D-H are
compensation channels identified by cross-lineage review as unexamined by A-C.

Each probe returns a record. The runner does not aggregate them into a score.
"""

from kernel import (
    Subject, Constitution, Receipt, WitnessObservation, Amendment,
    Request, adjudicate, Violation,
)

GOOD_STRUCT = lambda issuer="registry": Receipt(
    Constitution.STRUCTURAL, Subject.OPERATIONAL_REQUEST, "v1",
    "STRUCTURALLY_ADMISSIBLE", issuer)
GOOD_SCI = lambda issuer="protocol-board": Receipt(
    Constitution.SCIENTIFIC, Subject.OPERATIONAL_REQUEST, "v1",
    "SUPPORTED_UNDER_SCOPE", issuer)
GOOD_OP = lambda issuer="platform": Receipt(
    Constitution.OPERATIONAL, Subject.OPERATIONAL_REQUEST, "v1",
    "DEPLOYMENT_APPROVED", issuer)


def probe_A():
    """Structural fails, scientific and operational pass."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="deploy with a structurally rejected formulation",
        receipts=[
            Receipt(Constitution.STRUCTURAL, Subject.OPERATIONAL_REQUEST, "v1",
                    "STRUCTURALLY_REJECTED", "registry"),
            GOOD_SCI(), GOOD_OP(),
        ])
    return "A", "structural failure", adjudicate(req)


def probe_B():
    """Scientific fails, structural and operational pass."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="deploy on a contradicted claim",
        receipts=[
            GOOD_STRUCT(),
            Receipt(Constitution.SCIENTIFIC, Subject.OPERATIONAL_REQUEST, "v1",
                    "CONTRADICTED", "protocol-board"),
            GOOD_OP(),
        ])
    return "B", "scientific failure", adjudicate(req)


def probe_C():
    """Operational fails, structural and scientific pass."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="deploy after operational rejection",
        receipts=[
            GOOD_STRUCT(), GOOD_SCI(),
            Receipt(Constitution.OPERATIONAL, Subject.OPERATIONAL_REQUEST, "v1",
                    "REJECTED_FOR_OPERATION", "platform"),
        ])
    return "C", "operational failure", adjudicate(req)


def probe_D():
    """Later-gate overwrite: operational asserts an administrative pardon of a failed
    scientific gate. Invariant 5."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="operational override of a contradicted claim",
        receipts=[
            GOOD_STRUCT(),
            Receipt(Constitution.SCIENTIFIC, Subject.OPERATIONAL_REQUEST, "v1",
                    "CONTRADICTED", "protocol-board"),
            GOOD_OP(),
        ],
        claimed_override="operational-admin: scientific result pardoned for this release")
    return "D", "later-gate overwrite / retroactive pardon", adjudicate(req)


def probe_E():
    """Witness escalation: a witness-plane agent issues an emergency bypass token
    against a structural failure. Section 6.4."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="witness-issued emergency bypass",
        receipts=[
            Receipt(Constitution.STRUCTURAL, Subject.OPERATIONAL_REQUEST, "v1",
                    "STRUCTURALLY_REJECTED", "registry"),
            GOOD_SCI(), GOOD_OP(),
        ],
        witnesses=[WitnessObservation("observer-1", "emergency: grant pass", True)],
        bypass_token="WITNESS-EMERGENCY-PASS-001")
    return "E", "witness escalation", adjudicate(req)


def probe_F():
    """Cross-constitutional subject relabeling: an operational request presented as a
    claim protocol so the operational gate is never consulted. Section 6.0."""
    req = Request(
        subject=Subject.CLAIM_PROTOCOL, subject_version="v1",
        description="an operational deployment relabeled as a claim protocol",
        receipts=[
            Receipt(Constitution.STRUCTURAL, Subject.CLAIM_PROTOCOL, "v1",
                    "STRUCTURALLY_ADMISSIBLE", "registry"),
            Receipt(Constitution.SCIENTIFIC, Subject.CLAIM_PROTOCOL, "v1",
                    "SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", "protocol-board"),
            # no operational receipt: that is the point of the relabel
        ])
    return "F", "subject relabeling", adjudicate(req)


def probe_G():
    """Score averaging: aggregate the three gates into a composite >= 0.80 with one
    failure. Invariant 2."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="composite maturity score offered in place of gate outcomes",
        receipts=[
            GOOD_STRUCT(),
            Receipt(Constitution.SCIENTIFIC, Subject.OPERATIONAL_REQUEST, "v1",
                    "CONTRADICTED", "protocol-board"),
            GOOD_OP(),
        ],
        composite_score=0.84)
    return "G", "score averaging", adjudicate(req)


def probe_H():
    """Mid-run amendment: submit an amendment lowering strictness during adjudication.
    Section 2 amendment rule."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="amendment lowering gate strictness submitted mid-run",
        receipts=[
            GOOD_STRUCT(),
            Receipt(Constitution.SCIENTIFIC, Subject.OPERATIONAL_REQUEST, "v1",
                    "CONTRADICTED", "protocol-board"),
            GOOD_OP(),
        ],
        pending_amendment=Amendment(
            "CONTRADICTED shall be treated as passing for release purposes",
            lowers_strictness=True))
    return "H", "mid-run amendment weakening", adjudicate(req)


def probe_CONTROL():
    """Positive control. All three gates pass, no compensation attempted.
    If this refuses, the kernel refuses everything and probes A-H prove nothing."""
    req = Request(
        subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
        description="clean request, all gates pass",
        receipts=[GOOD_STRUCT(), GOOD_SCI(), GOOD_OP()])
    return "CONTROL", "positive control (must EXECUTE)", adjudicate(req)


PROBES = [probe_A, probe_B, probe_C, probe_D,
          probe_E, probe_F, probe_G, probe_H, probe_CONTROL]

# Required behavior per probe. The control must execute; everything else must refuse.
REQUIRED = {p: "REFUSE" for p in "ABCDEFGH"}
REQUIRED["CONTROL"] = "EXECUTE"
