# Redactions

One section is withheld from the public edition. It is declared here rather than removed
silently, and the withheld document is hash-committed so that any later disclosure can be
checked against the version that existed on the publication date.

## R-1 — `canon/TRIPLE_GOVERNANCE.md` §8, Project-Family Mapping

**Withheld:** a table mapping the three constitutions onto a specific private implementation —
subsystem ownership and the packaging strategy for a future shared contract — plus the
paragraph specifying that contract.

**Reason:** operational detail about one deployment. It is not part of the framework and
nothing in §§1–7 or §§9–12 depends on it.

**Retained in substance:** one removed sentence was normative rather than descriptive, a
prohibition on unauthorized implementation. Its substance is preserved in §10.

**Hash commitment.** SHA-256 of the unredacted document as it existed on 2026-07-21:

```
a637bcd9889454d75bc9b8c3c5af571b36c1c92fdf768e83add151ee88945687  TRIPLE_GOVERNANCE.md (unpublished, full)
```

`canon/SHA256SUMS` records the digests of the **published** bytes and is a different manifest.
Do not confuse the two.

## Cross-reference repairs

Made before publication, in all three canon files, and noted here for completeness:

- Cross-document links repointed from the original archive filenames to `CCTF.md`, `CSRF.md`,
  `TRIPLE_GOVERNANCE.md`.
- Two companion documents that are not published are named without links.
- One reference to the §8 table was removed from `canon/CSRF.md`.
- Private component names were replaced with their general terms where the framework concept,
  not the component, was the point.

No law, invariant, gate output, claim state, hypothesis, or test was altered.
