# Prompt 08 — Quality gate for command_coverage.md

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

STEP_ID = 08
STEP_NAME = verify_command_coverage_quality_gate

Recommended model: deepseek-v4-pro:cloud or kimi-k2.6:cloud
Physical instrument access required: NO.

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
COMMANDS_FILE = assets/<VENDOR>/<MODEL>/commands.txt
COVERAGE_FILE = assets/<VENDOR>/<MODEL>/command_coverage.md
REPORT_FILE = assets/<VENDOR>/<MODEL>/workflow_reports/08_verify_command_coverage_quality_gate_report.md

MAIN GOAL

Verify that `command_coverage.md` is a complete, auditable map from command inventory to PyMeasure planning.
Only create or update REPORT_FILE.

CHECKS

1. Every unique command from `commands.txt` is represented, intentionally deferred, or explained as an alias/duplicate.
2. Every coverage row has:
   - subsystem,
   - manual section/source,
   - command,
   - form,
   - Python API plan,
   - API type,
   - protocol test status,
   - hardware policy,
   - status,
   - notes.
3. Risky commands are not marked as normal hardware-tested tasks.
4. Parser candidates are present for block/table/report/trace data.
5. Implementation batches exist and do not bundle too many unrelated subsystems.
6. The first implementation batch is small enough for one Codex turn.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$coverage = "$assetDir/command_coverage.md"

Test-Path $coverage
Select-String -Path $coverage -Pattern "COMMAND COVERAGE TABLE", "IMPLEMENTATION BATCHES", "UNSAFE_OR_DEFERRED_COMMANDS", "PARSER_CANDIDATES"
Select-String -Path $coverage -Pattern "needs-design", "protocol-only", "never", "operator-confirmed-only"
git diff --check
git diff --stat
git status --short
```

REPORT FORMAT

Write REPORT_FILE with:

STATUS: PASS/FAIL
HUMAN_REQUIRED: yes/no
commands in commands.txt:
coverage rows:
missing commands:
extra commands:
unsafe/deferred commands:
parser candidates:
first batch scope acceptable: yes/no
blockers:
next step recommendation:
```
