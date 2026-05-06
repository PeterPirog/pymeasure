# Prompt 15 — Hardware execution decision gate

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 15
STEP_NAME = hardware_execution_decision_gate

Recommended model: qwen3-coder-next:cloud
Physical instrument access required: YES, but this gate only prepares the operator decision.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a
VISA_ADDRESS = <paste real VISA address>

Paths:

COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/15_hardware_execution_decision_gate_report.md

MAIN GOAL

Prepare a go/no-go decision before running real hardware tests.
Do not run the hardware command automatically.
Only create or update REPORT_FILE.

CHECKS

1. VISA address is present and plausible.
2. Hardware test file exists and is collectable without hardware.
3. Tests skip without device address.
4. Tests do not contain destructive or service-only commands.
5. Tests do not enable hazardous output unless explicitly marked operator-confirmed and the operator agrees.
6. Timeout is at least 20000 ms for older GPIB unless manual requires different.
7. Final safe state is defined.
8. Error queue handling is defined if safe API exists.
9. The exact command for the operator to run is printed.

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes
reason: physical instrument execution requires operator confirmation
VISA address:
preflight checklist:
unsafe commands found:
final safe state:
exact command to run:
operator expected outputs to paste back:
```
