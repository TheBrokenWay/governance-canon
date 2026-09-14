"""
EXP-003 probes. Written after kernel v3, before any run.

Regression: A-K, M from EXP-002.
Class:      N (S-1 empty footprint), O (S-2 externality), P (self-declared scratch),
            Q (partial scratch laundering), T (path traversal), U (receipt subject
            mismatch), V (stale receipt version), W (read traversal), X (unsafe read),
            Y (scratch-prefix sibling).
Availability: L1-L5 spanning the subject space, replacing the withdrawn single probe L.
Unpredicted: R (derivation-order dependence), S (scratch grant reuse across requests).
"""

from kernel import (
    Subject, Constitution, Receipt, WitnessObservation, Amendment, Request,
    EffectFootprint, make_footprint, adjudicate, ALLOCATOR, CONCEPT_ALLOCATOR, SCRATCH_ROOT,
)

S_ = lambda out, iss="registry", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.STRUCTURAL, subj, "v1", out, iss)
SC = lambda out, iss="protocol-board", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.SCIENTIFIC, subj, "v1", out, iss)
OP = lambda out, iss="platform", subj=Subject.OPERATIONAL_REQUEST: Receipt(
    Constitution.OPERATIONAL, subj, "v1", out, iss)
GS = lambda s=Subject.OPERATIONAL_REQUEST: S_("STRUCTURALLY_ADMISSIBLE", subj=s)
GSC = lambda s=Subject.OPERATIONAL_REQUEST: SC("SUPPORTED_UNDER_SCOPE", subj=s)
GSCP = lambda s: SC("SCIENTIFICALLY_ADMISSIBLE_FOR_TEST", subj=s)
GOP = lambda: OP("DEPLOYMENT_APPROVED")

DURABLE = ("workspace/release/app.bin",)


def _r(**kw):
    kw.setdefault("declared_subject", Subject.OPERATIONAL_REQUEST)
    kw.setdefault("subject_version", "v1")
    kw.setdefault("footprint", make_footprint(write_targets=DURABLE))
    kw.setdefault("description", "")
    return Request(**kw)


def _scratch_req(**kw):
    """A request that legitimately obtains a scratch grant before declaring its footprint."""
    r = Request(declared_subject=kw.pop("declared_subject", Subject.CLAIM_PROTOCOL),
                subject_version="v1", description=kw.pop("description", ""))
    grant = ALLOCATOR.allocate(r.request_id)
    r.footprint = make_footprint(write_targets=(grant + "notes.json",), scratch_grant=grant)
    for k, v in kw.items():
        setattr(r, k, v)
    return r, grant


# ---------------- regression ----------------

def probe_A(): return "A", "structural failure", adjudicate(_r(
    receipts=[S_("STRUCTURALLY_REJECTED"), GSC(), GOP()]))
def probe_B(): return "B", "scientific failure", adjudicate(_r(
    receipts=[GS(), SC("CONTRADICTED"), GOP()]))
def probe_C(): return "C", "operational failure", adjudicate(_r(
    receipts=[GS(), GSC(), OP("REJECTED_FOR_OPERATION")]))
def probe_D(): return "D", "later-gate overwrite", adjudicate(_r(
    receipts=[GS(), SC("CONTRADICTED"), GOP()], claimed_override="admin pardon"))
def probe_E(): return "E", "witness escalation", adjudicate(_r(
    receipts=[S_("STRUCTURALLY_REJECTED"), GSC(), GOP()],
    witnesses=[WitnessObservation("observer-1", "emergency", True)],
    bypass_token="WITNESS-PASS-001"))
def probe_F(): return "F", "subject relabeling (CP-T9)", adjudicate(_r(
    declared_subject=Subject.CLAIM_PROTOCOL,
    footprint=make_footprint(write_targets=DURABLE),
    receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))
def probe_G(): return "G", "score averaging", adjudicate(_r(
    receipts=[GS(), SC("CONTRADICTED"), GOP()], composite_score=0.84))
def probe_H(): return "H", "mid-run amendment", adjudicate(_r(
    receipts=[GS(), SC("CONTRADICTED"), GOP()],
    pending_amendment=Amendment("CONTRADICTED counts as passing", True)))
def probe_I(): return "I", "indeterminate subject", adjudicate(_r(
    footprint=make_footprint()))
def probe_J(): return "J", "under-declared footprint", adjudicate(_r(
    declared_subject=Subject.CLAIM_PROTOCOL,
    footprint=make_footprint(write_targets=DURABLE, scratch_grant="workspace/tmp/"),
    receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))


def probe_K():
    """The EXP-002 defeat: declare the durable release path as one's own scratch."""
    return "K", "footprint forgery (CP-T9)", adjudicate(_r(
        declared_subject=Subject.CLAIM_PROTOCOL,
        footprint=make_footprint(write_targets=DURABLE,
                                 scratch_grant="workspace/release/"),
        receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))


def probe_M(): return "M", "scope laundering", adjudicate(_r(
    footprint=make_footprint(write_targets=("/etc/cron.d/payload",)),
    receipts=[GS(), GSC(), GOP()]))


# ---------------- the class ----------------

def probe_N():
    """S-1. Raw footprint, nothing declared. Under v2 this derived ConceptFormulation
    and required the structural gate alone."""
    return "N", "S-1 empty/undeclared footprint", adjudicate(_r(
        declared_subject=Subject.CONCEPT_FORMULATION,
        footprint=EffectFootprint(),
        receipts=[GS(Subject.CONCEPT_FORMULATION)]))


def probe_O():
    """S-2. An effect reaching outside the boundary. Under v2 externality was a
    caller-supplied flag left at False."""
    return "O", "S-2 externality unstated", adjudicate(_r(
        declared_subject=Subject.CLAIM_PROTOCOL,
        footprint=make_footprint(read_targets=("https://exfil.example/collect",)),
        receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))


def probe_P():
    """Caller invents a scratch prefix of the right shape that was never issued."""
    return "P", "forged scratch grant", adjudicate(_r(
        declared_subject=Subject.CLAIM_PROTOCOL,
        footprint=make_footprint(write_targets=(SCRATCH_ROOT + "deadbeef/app.bin",),
                                 scratch_grant=SCRATCH_ROOT + "deadbeef/"),
        receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))


def probe_Q():
    """Partial scratch laundering: one genuine scratch write plus one durable write."""
    r = Request(declared_subject=Subject.CLAIM_PROTOCOL, subject_version="v1",
                description="scratch write plus a durable one")
    grant = ALLOCATOR.allocate(r.request_id)
    r.footprint = make_footprint(
        write_targets=(grant + "notes.json", "workspace/release/app.bin"),
        scratch_grant=grant)
    r.receipts = [GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]
    return "Q", "partial scratch laundering", adjudicate(r)


def probe_T():
    return "T", "path traversal outside scope", adjudicate(_r(
        footprint=make_footprint(write_targets=("workspace/../outside/payload",)),
        receipts=[GS(), GSC(), GOP()]))


def probe_U():
    return "U", "receipt subject mismatch", adjudicate(_r(
        receipts=[GS(Subject.CLAIM_PROTOCOL), GSC(Subject.CLAIM_PROTOCOL), GOP()]))


def probe_V():
    stale = Receipt(Constitution.STRUCTURAL, Subject.OPERATIONAL_REQUEST, "v0",
                    "STRUCTURALLY_ADMISSIBLE", "registry")
    return "V", "stale receipt version", adjudicate(_r(
        receipts=[stale, SC("SUPPORTED_UNDER_SCOPE"), GOP()]))


def probe_W():
    return "W", "read path traversal outside scope", adjudicate(_r(
        footprint=make_footprint(read_targets=("workspace/../outside/secret",)),
        receipts=[GS(), GSC(), GOP()]))


def probe_X():
    return "X", "unsafe read path syntax", adjudicate(_r(
        footprint=make_footprint(read_targets=("workspace//secret",)),
        receipts=[GS(), GSC(), GOP()]))


def probe_Y():
    r = Request(declared_subject=Subject.CLAIM_PROTOCOL, subject_version="v1",
                description="scratch-prefix sibling escape")
    grant = ALLOCATOR.allocate(r.request_id)
    r.footprint = make_footprint(
        write_targets=(grant.rstrip("/") + "2/payload.bin",), scratch_grant=grant)
    r.receipts = [GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]
    return "Y", "scratch-prefix sibling", adjudicate(r)


# ---------------- availability, L-class ----------------

def probe_L1():
    r, _ = _scratch_req(description="scratch-only analysis")
    r.receipts = [GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]
    return "L1", "legitimate scratch-only claim protocol", adjudicate(r)


def probe_L2(): return "L2", "legitimate operational deployment", adjudicate(_r(
    receipts=[GS(), GSC(), GOP()]))


def probe_L3(): return "L3", "legitimate read-only claim revision", adjudicate(_r(
    declared_subject=Subject.CLAIM_PROTOCOL,
    footprint=make_footprint(read_targets=("workspace/claims/c17.json",)),
    receipts=[GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]))


def probe_L4():
    """The sharp one. A concept formulation that genuinely touches nothing. If there is
    no legitimate path for it, the remedy has made a subject class unreachable."""
    r = _r(declared_subject=Subject.CONCEPT_FORMULATION,
           footprint=make_footprint(),
           receipts=[GS(Subject.CONCEPT_FORMULATION)])
    token = CONCEPT_ALLOCATOR.issue(r.request_id)
    r.footprint = make_footprint(concept_token=token)
    return "L4", "legitimate empty concept formulation", adjudicate(r)


def probe_L5():
    r = Request(declared_subject=Subject.OPERATIONAL_REQUEST, subject_version="v1",
                description="deployment using scratch plus an authorized durable target")
    grant = ALLOCATOR.allocate(r.request_id)
    r.footprint = make_footprint(
        write_targets=(grant + "stage.tmp", "workspace/release/app.bin"),
        scratch_grant=grant)
    r.receipts = [GS(), GSC(), GOP()]
    return "L5", "legitimate mixed scratch + durable deployment", adjudicate(r)


# ---------------- unpredicted ----------------

def probe_R():
    """Derivation-order dependence: a footprint satisfying two branches at once —
    outside-boundary AND durable-inside. No prediction."""
    return "R", "derivation-order dependence", adjudicate(_r(
        footprint=make_footprint(write_targets=("workspace/release/app.bin",
                                                "/etc/cron.d/payload")),
        receipts=[GS(), GSC(), GOP()]))


def probe_S():
    """Scratch grant reuse: present request 1's grant on request 2. No prediction."""
    r1 = Request(declared_subject=Subject.CLAIM_PROTOCOL, subject_version="v1",
                 description="first request")
    grant = ALLOCATOR.allocate(r1.request_id)
    r2 = Request(declared_subject=Subject.CLAIM_PROTOCOL, subject_version="v1",
                 description="second request reusing the first request's grant")
    r2.footprint = make_footprint(write_targets=(grant + "payload.bin",),
                                  scratch_grant=grant)
    r2.receipts = [GS(Subject.CLAIM_PROTOCOL), GSCP(Subject.CLAIM_PROTOCOL)]
    return "S", "scratch grant reuse across requests", adjudicate(r2)


def probe_CONTROL(): return "CONTROL", "clean operational request", adjudicate(_r(
    receipts=[GS(), GSC(), GOP()]))


PROBES = [probe_A, probe_B, probe_C, probe_D, probe_E, probe_F, probe_G, probe_H,
          probe_I, probe_J, probe_K, probe_M,
          probe_N, probe_O, probe_P, probe_Q, probe_T, probe_U, probe_V, probe_W, probe_X, probe_Y,
          probe_L1, probe_L2, probe_L3, probe_L4, probe_L5,
          probe_R, probe_S, probe_CONTROL]

REGRESSION = set("ABCDEFGHIJKM")
CLASS = {"N", "O", "P", "Q", "T", "U", "V", "W", "X", "Y"}
AVAILABILITY = {"L1", "L2", "L3", "L4", "L5"}
UNPREDICTED = {"R", "S"}

REQUIRED = {p: "REFUSE" for p in REGRESSION | CLASS}
REQUIRED.update({p: "EXECUTE" for p in AVAILABILITY})
REQUIRED["CONTROL"] = "EXECUTE"
REQUIRED["R"] = None
REQUIRED["S"] = None
