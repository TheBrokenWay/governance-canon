# Publication checklist

## v0.2.0 candidate

Preserve the `v0.1.0` tag and history unchanged. The v0.2.0 release consists
of `V0.2.0-REMEDIATION.md`, the three `RESULT-v0.2.0` records (with
EXP-003's canonical file named `RESULT-v0.2.0-final.json`), and
`verify_reproducibility.py`. Before publication, run `make verify` from a clean
checkout and record its output, commit, tag, release archive hash, and manifest
hash. The candidate fixes write-once result handling, read/write path syntax
checks, concept registration reachability, and receipt subject/version binding.
It does not claim OS-level symlink containment or authenticated receipt
provenance; those remain explicit limitations in the remediation record.

State at last audit, 2026-09-14. Everything below either passes or is named as a manual step.

## Passing — verified mechanically

| Check | Result |
|---|---|
| `cd canon && sha256sum -c SHA256SUMS` | 3 of 3 OK |
| Secrets, credentials, keys, tokens | none |
| IP addresses, hostnames, emails, filesystem paths | none |
| Internal component and service names, roadmap gaps | none |
| Third parties named | AI systems/providers are named for attribution; no private operational details |
| Harnesses execute from a cold run | EXP-001, EXP-002, EXP-003 execute; this does not mean their criteria passed |
| Git repository with commit history and a release tag | initialised, tagged `v0.1.0` |
| `__pycache__` excluded | yes |

## Manual steps remaining

1. **License.** v0.2.0 includes the full CC BY 4.0 legalcode with SPDX and LLC attribution.

   ```
   curl -sL https://creativecommons.org/licenses/by/4.0/legalcode.txt > LICENSE
   ```

   Then re-add the title line, `SPDX-License-Identifier: CC-BY-4.0`, and the copyright line at
   the top.

2. **Create the GitHub repository at exactly `TheBrokenWay/governance-canon`.** `CITATION.cff`
   names that path; a mismatch breaks the DOI record's backlink.

3. **Push, then mint the Zenodo DOI on the `v0.1.0` tag the same day.** The DOI is the
   third-party archival timestamp and it is the reason this is one repository rather than three.

## Who can push this

Not the Claude session that built it: no GitHub connector exists in the registry, its `gh` is
scoped to pre-configured repositories, and the device shell is blocked by the 2026-09-08 Windows
update. Push is the author's or Codex's. Step-by-step commands: `PUSH-governance-canon.txt`.

## Never publish here

**The EXP-004 routing-policy package must not enter this repository.** Its `inputs/` directory
holds, by design, the pre-redaction state of these files — the control-plane vulnerability
disclosure, the private archive path, the internal agent-ownership scheme, the absent-service
gap map, and the internal component names. Those are its seeded defects and it cannot function
without them. Publishing it would restore every redaction in one commit.

It lives privately and its **result** returns here — scores and the routing rule, not the
dossier.

## What this repository claims, and does not

Claimed: three frameworks, a method published as instructions, and three preregistered
experiments — two of which failed their own criteria and are reported unpatched — plus a dated
retraction of an overclaim the author made in his own favour.

Not claimed: that any framework is validated. No `IS-*`, `SR-*` or `CSRF-1`–`CSRF-6` test has
been run. Every experiment is one lineage on its own harness. `R-3` in EXP-002 is a single
source with an independent digest still pending. No external verification exists.
