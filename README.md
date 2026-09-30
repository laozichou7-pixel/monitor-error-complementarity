# Monitor Error Complementarity

**A preregistered study of rule-induced AI monitor diversity, correlated misses, and ensemble complementarity.**

> **Current empirical status:** No confirmatory SLEIGHT results have been generated. Synthetic outputs, where used, are engineering-validation artifacts only.

## Research question

AI safety systems increasingly rely on multiple monitors, evaluators, prompts, or auditing procedures. But multiple monitors do not automatically provide multiple independent lines of oversight.

This project asks:

> **When the underlying monitor model is held fixed, can different monitoring rules or prompts produce meaningfully different error structures?**

We care not only about average detection performance, but about whether different monitors:

- miss the same attacks;
- rescue each other's failures;
- produce strict unique catches;
- reduce ensemble joint misses;
- add non-redundant coverage when composed.

We separate three sources of apparent monitor diversity:

1. **Model heterogeneity**
2. **Rule heterogeneity**
3. **Benchmark / threat-model heterogeneity**

The first experiment isolates **rule heterogeneity**.

## First experiment

The initial study uses SLEIGHT-Bench as a shared evaluation space and compares four frozen rule conditions:

- **A** — `control_arena`
- **C1** — `state_tracking`
- **C2** — `control_arena_doc_planting_aware`
- **C3** — `control_arena_env_awareness`

The frozen analysis unit is **40 attack units**, with a deterministic **8 DEV / 32 TEST split**. Multi-stage attacks stay grouped at the attack-unit level.

Primary analyses:

- pairwise binary miss correlation;
- baseline rescue;
- strict unique catches;
- four-monitor joint misses;
- remove-one ensemble contribution;
- descriptive category coverage;
- attack-level bootstrap uncertainty.

Thresholding is monitor-specific at the benchmark's 1% false-positive-rate operating point and is intended to use the pinned upstream implementation rather than a separately reimplemented metric.

## Current status

Completed:

- research question narrowed to a falsifiable empirical test;
- benchmark asset/provenance audit;
- deterministic DEV/TEST split;
- frozen monitor conditions;
- analysis plan and result schema;
- local repository/decryption verification;
- API connectivity and parsing smoke test on synthetic data;
- result-analysis pipeline tested on synthetic fixtures.

Not completed:

- **no confirmatory SLEIGHT score data have been generated**;
- no empirical conclusion about rule-induced monitor complementarity has been made.

The current blocker is access to an inference environment that is both affordable and compatible with the benchmark's data-governance constraints.

## Research discipline

This repository distinguishes:

- engineering validation from empirical evidence;
- benchmark assets from analysis units;
- prompt diversity from model diversity;
- lower joint miss from genuine complementary error structure;
- a preregistered hypothesis from a confirmed result.

A reduction in OR-ensemble joint miss alone is not treated as sufficient evidence of useful monitor diversity.

## Repository map

- [`RESEARCH_BRIEF.md`](RESEARCH_BRIEF.md) — one-page overview
- [`PREREGISTRATION.md`](PREREGISTRATION.md) — frozen first-experiment plan
- [`STATUS.md`](STATUS.md) — current state and blocker
- [`docs/DATA_BOUNDARIES.md`](docs/DATA_BOUNDARIES.md) — public/private data boundaries
- [`docs/OUTREACH_NOTES.md`](docs/OUTREACH_NOTES.md) — external communication discipline

## External reference

SLEIGHT-Bench: https://github.com/safety-research/sleight-bench

## Status

**Preregistered and analysis-ready. Confirmatory experiment not yet run.**

## License

No license has been selected yet. Until a license is added, normal copyright applies.
