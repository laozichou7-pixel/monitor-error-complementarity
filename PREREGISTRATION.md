# Preregistration — First Experiment

## Objective

Test whether **rule heterogeneity**, while holding the underlying monitor model fixed, produces complementary error structure on a common benchmark.

This is a frozen study plan, not a claim that the experiment has already been run.

## Conditions

| ID | Prompt / rule condition |
|---|---|
| A | `control_arena` |
| C1 | `state_tracking` |
| C2 | `control_arena_doc_planting_aware` |
| C3 | `control_arena_env_awareness` |

The intended confirmatory design holds the base monitor model, transcript view, and inference settings constant while changing only the rule/prompt condition.

## Frozen analysis population

- 40 attack units
- 8 DEV
- 32 TEST
- multi-stage source transcripts remain grouped at the attack-unit level

DEV is reserved for engineering validation and code-path checks. TEST is not to be modified based on observed TEST results.

## Primary outcomes

1. Pairwise binary miss correlation, with full 2×2 contingency tables.
2. Baseline rescue: attacks missed by A but caught by C1/C2/C3.
3. Strict unique catch.
4. Four-monitor joint miss.
5. Remove-one ensemble contribution.

## Thresholding

Use a monitor-specific operating point calibrated at **1% false-positive rate**.

The threshold implementation should be taken from the pinned upstream SLEIGHT version. Do not silently substitute a separately implemented quantile rule.

Trial-level catch uses the upstream-consistent strict convention:

`score > threshold`

unless the pinned upstream implementation proves otherwise.

## Attack-unit aggregation

For a multi-stage attack unit:

- preserve raw source/stage scores;
- treat the attack unit as caught if any stage/trial catches;
- retain stage-level results for inspection.

## Secondary analyses

- descriptive category coverage;
- per-trial catch;
- any-trial catch;
- raw attack-level table;
- attack-unit bootstrap intervals.

Category-level results are descriptive because cells are small and uneven.

## Interpretation constraints

A lower OR-ensemble joint-miss rate alone is not sufficient evidence for useful rule heterogeneity.

Relevant signals include:

- rescue of baseline misses;
- non-identical miss vectors;
- strict unique catches;
- remove-one contribution;
- complementary catches spanning more than one idiosyncratic case/category.

A near-identical miss structure would weaken the rule-heterogeneity hypothesis.

Results from synthetic benchmark transcripts must not be generalized to all real-world monitoring deployments.

## Current empirical status

**No confirmatory benchmark results yet.**
