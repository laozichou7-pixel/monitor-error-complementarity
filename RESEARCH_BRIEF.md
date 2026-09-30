# Research Brief

## Do Diverse AI Safety Monitors Actually Have Independent Blind Spots?

**A preregistered study of rule-induced monitor diversity**

AI safety systems increasingly rely on multiple monitors, evaluators, prompts, or auditing procedures. However, having multiple monitors does not necessarily mean having multiple independent lines of oversight.

Two monitors can look different while still failing on the same cases. If their errors are highly correlated, adding the second monitor may provide little additional safety value. Conversely, monitors with similar average performance may be valuable if they catch different failures.

Our project asks:

> **When the underlying monitor model is held fixed, can different monitoring rules or prompts produce meaningfully different error structures?**

We distinguish:

1. **Model heterogeneity**
2. **Rule heterogeneity**
3. **Benchmark / threat-model heterogeneity**

The first experiment isolates rule heterogeneity.

### Experimental design

Using SLEIGHT-Bench, we compare four frozen monitoring-rule conditions:

- A: `control_arena`
- C1: `state_tracking`
- C2: `control_arena_doc_planting_aware`
- C3: `control_arena_env_awareness`

The frozen analysis population contains **40 attack units**, split deterministically into **8 DEV / 32 TEST**. Multi-stage attacks remain grouped at the attack-unit level.

Primary analyses:

- pairwise binary miss correlation;
- baseline rescue;
- strict unique catches;
- four-monitor joint misses;
- remove-one ensemble contribution;
- descriptive category-level coverage;
- attack-level bootstrap uncertainty.

Thresholding is calibrated separately for each monitor at the benchmark's 1% false-positive-rate operating point, using the pinned upstream implementation rather than a reimplemented metric.

### Current status

Completed:

- benchmark asset and provenance audit;
- deterministic DEV/TEST split;
- frozen monitor configurations;
- preregistered analysis plan;
- raw-output schema and reproducibility tooling;
- local repository/decryption verification;
- API connectivity and parsing smoke tests on synthetic data;
- complete analysis pipeline tested on synthetic fixtures.

**We do not yet have confirmatory SLEIGHT results.**

The remaining constraint is access to a suitable inference environment. The intended confirmatory configuration is currently beyond the project's available API budget, and we have deliberately not substituted another provider and presented that as equivalent confirmatory evidence.

### Why we are sharing this before running the main experiment

We are seeking criticism before spending scarce inference resources.

We would especially value feedback on:

- whether error complementarity is a useful operationalization of monitor independence;
- whether fixed-FPR comparison introduces hidden confounds;
- whether the rule conditions are sufficiently distinct for the intended interpretation;
- which external benchmark would provide the strongest follow-up validation;
- whether an independent replication or collaboration route is available.

The broader goal is modest:

> to determine whether “monitor diversity” corresponds to genuinely different detection pathways, or merely multiple implementations of the same blind spots.

**Status:** preregistered and analysis-ready; confirmatory experiment not yet run.
