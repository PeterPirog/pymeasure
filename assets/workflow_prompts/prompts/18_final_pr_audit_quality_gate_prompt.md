# Prompt 18 — Final PR audit quality gate

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 18
STEP_NAME = final_pr_audit_quality_gate

Recommended model: deepseek-v4-pro:cloud or qwen3-coder-next:cloud
Physical instrument access required: NO, unless the operator chooses to repeat hardware tests.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a

Paths:

DRIVER_FILE = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.py
VENDOR_INIT = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/__init__.py
PROTOCOL_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>.py
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py
DOC_FILE = docs/api/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.rst
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/18_final_pr_audit_quality_gate_report.md

MAIN GOAL

Perform a final upstream-PR readiness audit.
Only create or update REPORT_FILE unless fixing tiny documentation/test import issues is explicitly necessary.

CHECKS

1. Driver file exists and imports.
2. Vendor `__init__.py` exports the class.
3. Protocol tests pass.
4. Hardware tests collect and skip without address.
5. Documentation file exists.
6. Vendor docs index includes the new file.
7. No public get/set API.
8. No includeSCPI=True.
9. Destructive/hazardous commands not run in hardware tests.
10. All implemented commands have protocol tests.
11. Final PR diff excludes local artifacts.
12. `git diff --check` is clean.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -m pytest tests/instruments/$vendor/test_${model}_with_device.py -q
python -c "from pymeasure.instruments.$vendor import Fluke5560A; print(Fluke5560A)"
git diff --check
git diff --stat
git status --short
git diff --name-only
```

Fail if `git diff --name-only` includes:

assets/
AGENTS.md
Agents.md
*.pdf
workflow_reports/
manual conversion files
codex_worklog.md
command_coverage.md

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes/no
pytest protocol result:
hardware collect/skip result:
import result:
docs present: yes/no
vendor init export: yes/no
local artifacts in final diff: yes/no
diff check clean: yes/no
missing protocol coverage:
unsafe hardware test findings:
final recommendation:
```
