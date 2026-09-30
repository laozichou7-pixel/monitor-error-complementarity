# Project Status

## Completed

- Research question narrowed to a falsifiable monitor-complementarity test.
- Model, rule, and benchmark/threat-model heterogeneity separated as distinct variables.
- SLEIGHT-Bench selected for the first shared evaluation space.
- Benchmark asset/provenance audit completed.
- Frozen 40-unit analysis population established.
- Deterministic 8 DEV / 32 TEST split established.
- Four rule conditions frozen.
- Analysis metrics frozen.
- Raw result schema and reproducibility tooling prepared.
- Local benchmark/repository validation completed.
- Synthetic API smoke test completed.
- Analysis pipeline tested on synthetic data.

## Important repository-asset note

One additional repository directory was observed outside the frozen manifest:

`attacks/refusal_forcing/refusal-poisoning-credential-exfil`

It is treated as an **out-of-manifest repository asset** and is not added to the frozen 40-unit experiment.

No claim is made here about why the upstream repository contains it or why it is outside the frozen analysis population.

## Not completed

- No real SLEIGHT monitor-score dataset has been generated.
- No 1% FPR confirmatory result has been computed.
- No empirical claim about monitor independence or complementarity has been established.
- No external-benchmark replication has been run.

## Current blocker

The current blocker is inference access under acceptable cost and data-governance conditions.

This is an execution/resource constraint, not an analysis-pipeline failure.

## Next empirical milestone

Produce real `raw_results.jsonl` plus upstream-compatible monitor thresholds, then run the frozen analysis plan.
