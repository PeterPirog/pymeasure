# Prompt 14 — Quality gate after each generic implementation batch

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 14
STEP_NAME = verify_each_implementation_batch_quality_gate

Recommended model: qwen3-coder-next:cloud
Physical instrument access required: NO. This verifies protocol tests and static/code hygiene only.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a
BATCH_ID = <paste batch id>
BATCH_NAME = <paste batch name>
COMMANDS_EXPECTED_IN_BATCH = <paste exact command rows or API names>

Paths:

DRIVER_FILE = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.py
PROTOCOL_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>.py
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/14_verify_each_implementation_batch_quality_gate_report.md

MAIN GOAL

Verify that the last implementation batch is correct, isolated, protocol-tested, and PyMeasure-compliant.
Only update REPORT_FILE unless a small test/report typo must be fixed.
Do not add new features.

CHECKS

1. Driver imports successfully.
2. Protocol tests pass.
3. Every implemented command/API from this batch has an expected_protocol test.
4. No public `get_*` or `set_*` methods were added.
5. No `includeSCPI=True` was added.
6. Property creators are used where appropriate.
7. Command-only actions are methods.
8. Data-transfer commands use parser methods.
9. Validators are used only when manual ranges/discrete sets are confirmed.
10. Hardware tests, if present, skip without address.
11. No unsafe command was added to hardware tests.
12. `command_coverage.md` statuses match implementation and tests.
13. Changed files are limited to driver, tests, documentation if expected, and command_coverage/workflow report.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -m pytest tests/instruments/$vendor/test_${model}_with_device.py -q
python -c "from pymeasure.instruments.$vendor import Fluke5560A; print(Fluke5560A)"
Select-String -Path pymeasure/instruments/$vendor/$model.py -Pattern "includeSCPI=True", "def get_", "def set_"
git diff --check
git diff --stat
git status --short
git diff --name-only
```

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes/no
batch id/name:
commands expected:
commands implemented:
protocol tests found:
pytest result:
import result:
unsafe hardware tests found: yes/no
AGENTS.md compliance issues:
coverage status consistent: yes/no
changed files allowed: yes/no
blockers:
next step recommendation:
```
