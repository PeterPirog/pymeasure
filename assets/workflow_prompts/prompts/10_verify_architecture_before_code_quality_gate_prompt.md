# Prompt 10 — Quality gate for architecture before code

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 10
STEP_NAME = verify_architecture_before_code_quality_gate

Recommended model: deepseek-v4-pro:cloud
Physical instrument access required: NO.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
ARCHITECTURE_PLAN = assets/<VENDOR>/<MODEL>/architecture_plan.md
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/10_verify_architecture_before_code_quality_gate_report.md

MAIN GOAL

Decide whether it is safe to start implementation.
Only create or update REPORT_FILE.

CHECKS

1. Architecture plan explicitly chooses class structure.
2. If SCPI/IEEE-488.2 is confirmed, architecture uses `SCPIMixin, Instrument` and forbids `includeSCPI=True`.
3. If channels exist, architecture chooses `ChannelCreator` for fewer than 16 channels or `MultiChannelCreator` for more than 16 channels, unless justified.
4. Data-transfer/parser commands are not planned as simple properties.
5. Hazardous/destructive/service commands are deferred or protocol-only/never.
6. Batch 1 exact scope is small and limited to skeleton/common/status/safe basics.
7. Required PyMeasure paths are named using lowercase filenames and correct vendor package.
8. Human is required only if architecture is ambiguous or manuals conflict.

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes/no
chosen architecture:
channel strategy:
parser strategy:
SCPIMixin decision:
includeSCPI forbidden: yes/no
batch 1 scope:
high-risk deferred groups:
blockers:
next step recommendation:
```
