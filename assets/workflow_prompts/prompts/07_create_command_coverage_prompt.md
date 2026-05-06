# Prompt 07 — Create command_coverage.md from commands.txt

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: kimi-k2.6:cloud or deepseek-v4-pro:cloud
Physical instrument access required: NO. Planning and coverage table only.

VISA_ADDRESS_EXAMPLE, if present, is only metadata for local instructions and generated commands.
A cloud model cannot access a local GPIB/USB/LAN/RS-232 instrument directly.
Real hardware communication may only happen on the operator's local computer or explicitly configured local runner.


UPSTREAM PYMEASURE AGENTS.MD COMPLIANCE

Before editing, read the repository-level `AGENTS.md` file if it exists.
Follow it as the highest-priority local repository rule set.
In particular:

- Use Python 3.9+ compatible code.
- Keep line length at or below 100 characters.
- Follow PEP8 and PEP257.
- Use lowercase filenames for instrument modules.
- Place instrument drivers under `pymeasure/instruments/<manufacturer>/`.
- Update the manufacturer `__init__.py` when a driver class is added.
- Add protocol tests under `tests/instruments/<manufacturer>/`.
- Name hardware/device tests with the `_with_device.py` suffix.
- Add documentation under `docs/api/instruments/<manufacturer>/`.
- Prefer PyMeasure property creators: `control`, `measurement`, and `setting`.
- Do not create public `get_*` or `set_*` methods.
- Use validators only when ranges/discrete sets are confirmed by manuals.
- Use `map_values=True` when Python-facing names differ from device tokens.
- For channels with fewer than 16 channels, prefer `Instrument.ChannelCreator`.
- For more than 16 channels, prefer `Instrument.MultiChannelCreator`.
- Use `expected_protocol` / `ProtocolAdapter` for communication tests without hardware.
- Use imperative docstring summaries with a period at the end.
- Document properties with wording such as "Control", "Measure", "Get", or "Set".
- Do not use comments for obvious code; comments should explain non-obvious reasons.



STEP METADATA

STEP_ID = 07
STEP_NAME = create_command_coverage

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator
PYMEASURE_VENDOR_PACKAGE = fluke

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
COMMANDS_FILE = assets/<VENDOR>/<MODEL>/commands.txt
PROGRAMMING_GUIDE_LLM = assets/<VENDOR>/<MODEL>/programming_guide_llm.md
OPERATORS_MANUAL_LLM = assets/<VENDOR>/<MODEL>/operators_manual_llm.md
SERVICE_MANUAL_LLM = assets/<VENDOR>/<MODEL>/service_manual_llm.md
OUTPUT_FILE = assets/<VENDOR>/<MODEL>/command_coverage.md

MAIN GOAL

Create or update `command_coverage.md`.

This file maps manual commands to planned PyMeasure API, test coverage, hardware-test policy, and implementation batches.

Do not implement the driver yet.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/command_coverage.md

INPUT PRIORITY

1. `commands.txt` is the authoritative command inventory.
2. `programming_guide_llm.md` may provide command context.
3. `operators_manual_llm.md` and `service_manual_llm.md` may provide safety/test-policy context.
4. Do not invent missing commands.

OUTPUT STRUCTURE

1. Header with instrument, vendor, model, class name, instrument type, branch, manual sources, last updated, and local artifact notice.

2. `STATUS LEGEND`:
todo, implemented, protocol-tested, hardware-tested, unsafe, deferred, not-implemented, needs-verification.

3. `API TYPE LEGEND`:
SCPIMixin, Instrument.control, Instrument.measurement, Instrument.setting, method, method/parser, channel control, channel measurement, channel method, deferred, not-implemented, needs-design.

4. `HARDWARE TEST POLICY LEGEND`:
query-only, output-off-only, roundtrip-safe, operator-confirmed-only, protocol-only, never, needs-verification.

5. `COMMAND COVERAGE TABLE`.

Header must be exactly:

| Subsystem | Manual section | Command | Form | Python API | Type | Validator / mapping | Protocol test | Hardware test | Hardware policy | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

Rules:
- one row per command from `commands.txt`,
- command/query state -> `Instrument.control` or channel control,
- query-only scalar/status -> `Instrument.measurement` or method,
- command-only action -> method,
- data transfer -> `method/parser`,
- destructive/service/calibration/delete/format/NVM -> deferred/not-implemented or explicit method with protocol-only/never,
- use `needs-design` when architecture decision is required.

6. `IMPLEMENTATION BATCHES`.

Suggested batches:
1. Skeleton/Common/Status
2. Interface/System/Error queue
3. Input channels or input subsystem
4. Source/Output
5. Trigger/Arm/Initiate
6. Sense/Frequency/Sweep/Average
7. Calculate/Trace/Data parsers
8. Display/Window/Marker/Units
9. Memory/MMEM/Program/Test/Calibration risk
10. Documentation/final cleanup

7. `UNSAFE_OR_DEFERRED_COMMANDS`.

8. `PARSER_CANDIDATES`.

9. `MODEL_AND_OPTION_DEPENDENCIES`.

10. `FINAL REVIEW CHECKLIST`.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$coverage = "$assetDir/command_coverage.md"

Test-Path $coverage
Get-Content $coverage -TotalCount 180
Select-String -Path $coverage -Pattern "COMMAND COVERAGE TABLE", "IMPLEMENTATION BATCHES", "UNSAFE_OR_DEFERRED_COMMANDS", "PARSER_CANDIDATES"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 06

Verify that every command row from `commands.txt` is represented in `command_coverage.md`, unless explicitly listed as duplicate/alias/deferred with a reason.
Add a reconciliation summary:

```text
commands.txt unique commands:
command_coverage.md command rows:
missing from coverage:
extra in coverage:
aliases/deferred:
```

Fail if unexplained missing commands exist.


MANDATORY AUTOMATED QUALITY GATE

At the end of this prompt, create or update a step report file:

assets/<VENDOR>/<MODEL>/workflow_reports/<STEP_ID>_<STEP_NAME>_report.md

If the directory does not exist, create it.

The report must contain:

1. `STATUS: PASS` or `STATUS: FAIL`.
2. `HUMAN_REQUIRED: yes/no`.
3. A short reason if human input is required.
4. Files created or modified.
5. Commands run.
6. Exact output or summary of acceptance commands.
7. Counts requested by this prompt.
8. Any `needs-verification` items.
9. Any deviation from `AGENTS.md` or PyMeasure conventions.
10. A clear next-step recommendation.

Use `STATUS: FAIL` and stop if:

- required input files are missing,
- commands or API are invented without manual evidence,
- files outside the allowed scope were changed,
- acceptance commands fail,
- `git diff --check` reports whitespace errors,
- implementation prompts add features outside their batch scope,
- hardware tests would require unsafe or operator-confirmed actions,
- final cleanup still includes `assets/`, `AGENTS.md`, PDFs, local logs, or worklogs in the PR diff.

Do not proceed to the next workflow step automatically if `STATUS: FAIL`.
Do not ask the operator for help unless the report marks `HUMAN_REQUIRED: yes` and explains why.

FINAL REPORT

Report output path, number of command rows, planned batches, unsafe/deferred count, parser candidates count, first recommended implementation batch, confirmation that only `command_coverage.md` changed, and results of `git diff --check` and `git diff --stat`.
```
