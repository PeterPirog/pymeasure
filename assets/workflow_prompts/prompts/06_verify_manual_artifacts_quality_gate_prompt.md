# Prompt 06 — Quality gate for manual artifacts and commands.txt

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 06
STEP_NAME = verify_manual_artifacts_quality_gate

Recommended model: kimi-k2.6:cloud or deepseek-v4-pro:cloud
Physical instrument access required: NO.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
PROGRAMMING_GUIDE_LLM = assets/<VENDOR>/<MODEL>/programming_guide_llm.md
OPERATORS_MANUAL_LLM = assets/<VENDOR>/<MODEL>/operators_manual_llm.md
SERVICE_MANUAL_LLM = assets/<VENDOR>/<MODEL>/service_manual_llm.md
COMMANDS_FILE = assets/<VENDOR>/<MODEL>/commands.txt
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/06_verify_manual_artifacts_quality_gate_report.md

MAIN GOAL

Verify that prompts 02–05 produced reliable source artifacts before command coverage or implementation begins.
Do not modify driver, tests, or docs.
Only create or update REPORT_FILE.

CHECKS

1. Confirm all required artifacts exist, except optional manuals that were explicitly missing and reported.
2. Confirm `commands.txt` has:
   - source rules,
   - command form legend,
   - command inventory,
   - command counts,
   - parser candidates,
   - risk hints,
   - source evidence.
3. Confirm non-programming manuals did not add unconfirmed commands to the main command inventory.
4. Confirm `needs-verification` is used for ambiguity.
5. Confirm artifacts separate:
   - command syntax from Programming Guide,
   - operator safety from Operators/Operation Manual,
   - service-only/calibration risk from Service Manual.
6. Count command rows and report top subsystems.
7. List blockers that require a human.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$commands = "$assetDir/commands.txt"

Test-Path "$assetDir/programming_guide_llm.md"
Test-Path $commands
Select-String -Path $commands -Pattern "COMMAND INVENTORY", "COMMAND COUNTS", "PARSER CANDIDATES", "RISK HINTS", "Source evidence"
Select-String -Path $commands -Pattern "needs-verification"
git diff --check
git diff --stat
git status --short
```

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes/no
manual artifacts present:
commands count:
source separation verified: yes/no
unconfirmed command leakage found: yes/no
needs-verification count:
blockers:
next step recommendation:
```
