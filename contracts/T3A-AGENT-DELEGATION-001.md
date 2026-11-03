# T3A-AGENT-DELEGATION-001 — Constrained Implementation Contract

**Project:** Next 23  
**Delegated executor:** Antigravity (or any later coding agent subject to the same contract)  
**Contract status:** READY FOR HUMAN-AUTHORIZED EXECUTION; NOT A REPORT OF IMPLEMENTATION  
**Target branch:** `experiment/t3a-01-binding-integrity`  
**Specification baseline:** `LLA-001 / CORE-001 / T3A-001 v0.1.1-FROZEN`  
**Date:** 2026-11-03

## A. Mission and non-mission

Implement the **minimum deterministic, local-first T3-A binding integrity simulator** specified by `docs/experiments/T3A-001-v0.1.1-FROZEN.md`. Produce real evidence for every acceptance gate without changing the frozen learning theory or architecture.

**Prove only mechanical behavior:** correct instance-scoped role bindings, identity probe/echo, lawful role readout, complete/query-scoped search, bounded resource lifecycle, provenance safety, and ability to detect deliberately injected defects.

**Do NOT claim:** trained local learning, unsupervised role discovery, learned Relation Assembly, general intelligence, compositional generalization, biological validity, calibration of branch scores, or successful T3-B.

## B. Read-only authorities and precedence

Read, in exact order:
1. `docs/learning/LLA-001-v0.1.1-FROZEN.md`
2. `docs/core/CORE-001-v0.1.1-FROZEN.md`
3. `docs/experiments/T3A-001-v0.1.1-FROZEN.md`
4. `AGENTS.md`
5. `docs/governance/NEXT23-FREEZE-MANIFEST.json`
6. `reports/reviews/NEXT23-FCR-001-FINAL-REVIEW-AND-FREEZE.md`

Hierarchy is **learning theory → architecture → experimental contract**. A lower-level file must not silently redefine a higher-level law. Frozen versions are byte-immutable. If a contradiction affects correctness, return `SPEC_CONFLICT` with exact section IDs and halt affected implementation. Missing mandatory behavior is `SPEC_GAP`; ask for a decision rather than guessing. Harmless low-level choices may be recorded as `IMPLEMENTATION_ASSUMPTION` with a counter-test.

## C. File write permissions

**Read-only:** `docs/**`, `reports/reviews/**`, `AGENTS.md`, `README.md`, `contracts/**`, `scripts/verify_freeze.py`, `.github/**`.

**Write allowlist:** `experiments/t3a/**`, `reports/t3a/**`. Use only this scope unless explicitly approved. Do not create unrelated platforms, apps, model providers, plugin frameworks or AI agents.

**Branch rules:** never write directly to `main`, never merge/force-push, and never mark an experimental branch as a validated release. Commit each completed stage with diff and test evidence; push only if authorized by the operator's actual Git configuration and permissions.

## D. Mechanical model and enforcement

### D1. Representation and typed channels

Use separate finite pools for:
- Entity tokens: allocation slot, monotonically increasing generation, lifecycle and live references.
- Relation instances: allocation slot, generation, state `PENDING/COMMITTED/RETIRING/RELEASED`.
- Role-instance slots: a distinct endpoint for each role in each active relation instance.
- Binary `ROLE_ENTITY` temporary links.
- Binary `ENTITY_FEATURE` links, which may overlap across entities but are NOT identity channels.

Identity-only traversals: `RoleSlot --PROBE--> EntityToken --IDENTITY_ECHO--> RoleSlot`. A typed/epoch/generation validity gate must reject hops on feature edges and unqualified role/instance endpoints. Readout of fillers uses causal `ROLE_READ` hops over valid `ROLE_ENTITY` edges; a positive Join without these is invalid.

### D2. Real message causality

Design a deterministic local message queue. Each message/event records `message_id`, `parent_message_id`, `edge_ref`, `query_ref`, `query_epoch`, source/target endpoint refs with generation, `signal_type`, `microstep`, acceptance/rejection and reason. Record the event **when an actual legal hop occurs**, not after returning an answer. Independent test oracle may compute expected answers, but engine may not import or call it at query time.

Forbid symbolic shortcuts such as: `if owner == Sara and car == ...`, matching entity IDs across fixture records inside `probe_join`, pre-indexed tuple joins that bypass messages, or fabricated `MessageHop` entries. Generation comparisons solely for stale-reference validation are permitted.

### D3. Query scope and completeness

Select sources **within a query** with deterministic fair scheduling (T3-A default: creation order, mark served once); do not use region-wide global 1-WTA. Qualified target instances may become active through valid Echo. One source may have multiple targets. Preserve output pairings and typed `InferenceRecord` fields with supporting message refs.

`COMPLETE` = at least one result AND exhausted all required sources/targets; `NO_MATCH` = zero results AND complete search; `PARTIAL/RESOURCE_LIMIT` = insufficient resources with truthful unserved source/target counts; `REFUSED` for illegal/failed requests; reject old query epochs. Never hide unserved targets after first successful match.

### D4. Lifecycle, atomicity and provenance

Creation transaction is all-or-nothing: `PENDING → COMMIT` or `PENDING → ROLLBACK`. A failed creation must not leak a half-bound, externally visible relation. Free relation roles and links without deleting an entity still referenced elsewhere. On final entity release, hard-scrub all incident temporary edges. Increment generation monotonically on reallocation **including after rollback**; reject in-flight old-generation messages. Never reuse a live allocation.

Query execution may update temporary scheduler state, but not observational `E+`, `E-`, consolidated utility or other persistent learning state. `Observed`, `Predictive`, and `Inferred` must not be conflated. Resource limits are fixed/tested; a saturated engine must refuse or report partial results honestly.

## E. Implement in authorized stages

| Gate | Deliverable | Required proof |
|---|---|---|
| I0 — Document gate | Read-only inventory, version/hash verification, assumptions register | `python scripts/verify_freeze.py` PASS; any gaps reported |
| I1 — Mechanical foundation | resources, role slots, binary typed links, lifecycle-safe basic read | real tests for `T3A-01`, `02`, `03`, typed-channel invariants |
| I2 — Query + Join | query-scoped microstep queue, PROBE/ECHO, ROLE_READ, independent oracle | `T3A-04`, `05`, `06`, trace-replay evidence |
| I3 — Lifecycle + integrity | release, hard scrub, generation, atomic budget, provenance | `T3A-07`, `08`, `09`, `10`; no learning commits |
| I4 — Adversarial gate | extras, mutation tests, reproducibility, code audit, final report | `T3A-EXTRA-01/02`; `M-01..M-12` executed and killed; no fixture oracle in engine |

**Stop at every gate** to produce a factual handoff. Continue across phases only if the operator has expressly authorized autonomous execution and no `BLOCKED` gate or `SPEC_CONFLICT` exists. A later stage may not erase prior test evidence.

## F. Required tests and deliberate breaking

Implement **all** baseline cases `T3A-01..T3A-10` with clearly named pytest tests. The frozen contract's fixtures, positive/negative expected results, edge/epoch validity, and minimal trace requirements are authoritative.

In addition, `T3A-EXTRA-01` tests multiple valid target relations per source (no dropped target); `T3A-EXTRA-02` tests disabled readout, stale query epochs, and post-hoc trace fabrication. Execute all mutations `M-01..M-12` as real toggles or isolated faults; record the killer assertion and execution outcome. Do **not** simply declare a mutant detectable by inspection.

Mandatory adversarial checks include feature-overlap false resonance, within-instance role swap, owner with multiple possessions, non-exhaustive false `NO_MATCH`, stale message after slot reuse, rollback generation ABA, live-entity reference preservation, disallowed identity hop, disabled Echo, disabled ROLE_READ, and an internal `Inferred` event attempting to increment observational evidence.

## G. Handoff format: REQUIRED after each gate

Write `reports/t3a/I<gate>-HANDOFF.md` and provide:

1. Gate ID, branch, true HEAD SHA, modified/created files, summary of code behavior.
2. Exact commands run and exit codes, real pytest PASS/FAIL/SKIP; no invented coverage.
3. Test-case matrix: `PASS | FAIL | BLOCKED | NOT_RUN` with reason.
4. Link/path to causal message traces; proof that engine did not query oracle/test fixtures for answers.
5. Mutation results `KILLED | SURVIVED | BLOCKED | NOT_RUN` (I4).
6. Resource budget statistics, generation/rollback/provenance evidence.
7. `SPEC_GAP`, `SPEC_CONFLICT`, `IMPLEMENTATION_ASSUMPTION`, and open risks.
8. Frozen-document delta: MUST be zero; manifest verification and `git diff --check` output.
9. What is explicitly not implemented/tested; next authorized action.

Final report `reports/t3a/T3A-001-VERIFICATION-REPORT.md` must contain actual evidence, not anticipated results. If any mandatory mutant is missing/survives, `FULL PASS` is forbidden. The agent cannot approve its own architectural changes or merge results to `main`.

## H. Operational commands

```bash
git status --short
git branch --show-current
python scripts/verify_freeze.py
python -m pytest experiments/t3a/tests -q
python -m pytest experiments/t3a/tests/test_mutations.py -v
python -m pytest experiments/t3a/tests/test_replay.py -v
git diff --check
```

If a test module does not exist, report `NOT_RUN`; do not silently omit it or substitute output. No secrets, internet-dependent model calls or new production dependencies without explicit review.

## I. Handoff / acceptance signatures

- **Execution authority:** bounded technical implementation only.
- **Review authority:** human project owner and independent engineering review.
- **Initial T3-A state:** `NOT_RUN`.
- **Acceptance outcome:** `PENDING REAL EXECUTION EVIDENCE`.
- **Freeze:** documentary `v0.1.1` remains unchanged; no automatic `v0.1.2` or implementation freeze.

This file grants NO permission to claim a proven local-learning algorithm.
