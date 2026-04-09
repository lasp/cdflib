---
name: unit-test-workflow
description: "Run and validate cdflib unit tests after code changes. Use when editing Python code, verifying regressions, or preparing a PR. Covers default local pytest runs, optional remote-data tests, and failure triage."
argument-hint: "Describe what changed and whether you want full, targeted, or remote-data validation."
---

# cdflib Unit Test Workflow

## What This Skill Produces
- A repeatable test workflow after code changes.
- A clear choice between quick local validation and slower remote-data validation.
- A pass/fail decision with explicit completion checks.

## When to Use
- After modifying code under `cdflib/`.
- Before opening or updating a pull request.
- When investigating possible regressions in parsing, writing, epochs, or xarray behavior.

## Repository Test Model
- Unit tests live in `tests/`.
- Default local validation command is:

```bash
pytest
```

- In this repository, the default `pytest` run is the normal fast path and does not run the remote-data suite.
- Remote-data tests depend on downloading sample files and are slower (~15 minutes).
- Remote-data coverage is also exercised by CI on a weekly schedule (Monday 06:00 UTC) in `.github/workflows/remote-tests.yaml`.

## Procedure

### 1. Choose Test Scope
- If code changes are functional (logic, parsing, writing, time conversion, xarray integration), run full local tests with `pytest`.
- If the change is docs-only or non-runtime metadata, tests may be optional unless requested by maintainers.
- If code touches behavior known to depend on external sample data, include remote-data validation when practical.

### 2. Run Default Local Suite
Use:

```bash
pytest
```

Expected outcome:
- Exit code 0.
- No new failures introduced by the change.

### 3. Branch for Remote-Data Validation (Optional/Deeper)
Use this branch when changes affect data-read compatibility across real-world files or when maintainers request deeper confidence.

Recommended command path from project docs:

```bash
pytest -m remote_data
```

Alternative CI-style invocation:

```bash
pytest --remote-data
```

### 4. Interpret Results and Act
- If tests pass: report completion and summarize what scope was run.
- If tests fail:
  - Identify first failing test and traceback.
  - Determine whether failure is caused by the new changes or a pre-existing issue.
  - Fix code/tests as appropriate.
  - Re-run `pytest` until green.

### 5. Completion Checks
A testing cycle is complete when all of the following are true:
- The intended test scope was run (default local suite at minimum).
- `pytest` passed for that scope.
- Any failures encountered were triaged and addressed.
- The final summary states exactly which command(s) were run.

## Quick Decision Table

| Situation | Command | Notes |
|---|---|---|
| Standard code change | `pytest` | Default, expected for most edits |
| Suspected remote-data impact | `pytest -m remote_data` or `pytest --remote-data` | Slower, network-dependent |
| Pre-merge confidence check | `pytest` (+ remote-data when relevant) | Match change risk to test depth |

## Agent Output Format
When using this skill, report:
1. What changed.
2. Which test command(s) were run.
3. Whether tests passed.
4. If failures occurred, what was fixed and what re-runs succeeded.
