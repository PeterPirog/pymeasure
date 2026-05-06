# Quality gate matrix — coherent numbering v6

| Gate step | Runs after | Main verification | Human needed if |
|---:|---|---|---|
| 06 | 02–05 | Manual artifacts and `commands.txt` are complete and source-separated | Command syntax ambiguity or unconfirmed command leakage |
| 08 | 07 | `command_coverage.md` maps every command to API/test/risk | Missing coverage or unsafe policy conflict |
| 10 | 09 | Architecture is explicit and PyMeasure-compliant | Channel/helper architecture ambiguity |
| 12 | 11 | Batch 1 imports, protocol tests pass, batch scope isolated | Test failure or out-of-batch implementation |
| 14 | each 13 | Every subsystem batch imports, tests pass, coverage is updated | Test failure or out-of-batch implementation |
| 15 | before 16 | VISA preflight, operator approval, safe hardware plan | Always, because physical hardware is involved |
| 18 | after 17 | Upstream PR diff excludes local artifacts and tests/docs pass | Final PR approval or unresolved failures |

## Non-negotiable fail conditions

- Invented command syntax.
- Missing source evidence for commands.
- Main command inventory polluted by service/operator manual command-like tokens not confirmed in Programming Guide.
- Implemented command without protocol test.
- Hardware test that runs destructive/service/calibration/delete/format/store/power-off/long self-test commands.
- Public `get_*` or `set_*` API.
- `includeSCPI=True` in a new SCPI driver.
- Final PR diff contains `assets/`, `AGENTS.md`, PDFs, worklogs, or workflow reports.

## Required report path

Every step must write a local report under:

```text
assets/<vendor>/<model>/workflow_reports/
```

Every report must contain at least:

```text
STATUS: PASS or FAIL
HUMAN_REQUIRED: yes/no
changed files:
commands run:
acceptance results:
blockers:
next step recommendation:
```
