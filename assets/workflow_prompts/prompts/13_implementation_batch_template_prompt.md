# Prompt 13 — Generic implementation batch template

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: qwen3-coder-next:cloud
Physical instrument access required: NO for implementation and expected_protocol tests. Optional only for explicitly confirmed safe hardware tests.

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

STEP_ID = 13
STEP_NAME = implementation_batch_template

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a

Batch parameters:

BATCH_ID = 2
BATCH_NAME = <for example: Input channels>
BATCH_SUBSYSTEMS = <for example: INPut, SENSe:VOLTage>
COMMANDS_TO_IMPLEMENT = <paste exact command rows from command_coverage.md>
COMMANDS_TO_EXCLUDE = <paste risky/deferred command rows>

Paths:

ARCHITECTURE_PLAN = assets/<VENDOR>/<MODEL>/architecture_plan.md
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
DRIVER_FILE = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.py
PROTOCOL_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>.py
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py

MAIN GOAL

Implement only BATCH_ID / BATCH_NAME.

Do not implement commands outside COMMANDS_TO_IMPLEMENT.
Do not implement COMMANDS_TO_EXCLUDE.
Do not run destructive or operator-confirmed commands on hardware.
Every implemented command must have an `expected_protocol` test.

PYMEASURE API RULES

- command/query state -> `Instrument.control` or channel control.
- query-only scalar/status -> `Instrument.measurement` or explicit read method.
- command-only action -> method.
- data block/table/report -> method + parser.
- write-only non-action setting -> `Instrument.setting`.
- no `get_*` / `set_*`.
- no `includeSCPI=True`.
- use validators only when ranges/discrete values are confirmed in Programming Guide.
- use `values={...}` and `map_values=True` when Python names differ from device tokens.
- docstrings must start with imperative verbs and include units/ranges/types where known.

TASKS

1. Read `architecture_plan.md` and `command_coverage.md`.
2. Implement only the listed batch commands.
3. Add or extend helper classes if the architecture plan requires channels/traces/windows.
4. Add parser methods for data-transfer commands.
5. Add protocol tests for each implemented command.
6. Add or extend hardware tests only for commands with hardware policy query-only, output-off-only, or roundtrip-safe.
7. Hardware tests must skip without device address.
8. Update only relevant rows in `command_coverage.md`.
9. Do not change unrelated formatting.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -c "from pymeasure.instruments.$vendor import Fluke5560A; print(Fluke5560A)"
git diff --check
git diff --stat
git status --short
```

If hardware tests were added, do not run them unless a device address was explicitly provided. Print:

```powershell
python -m pytest tests/instruments/fluke/test_5560a_with_device.py --device-address "<VISA_ADDRESS>" -q -s
```


EXTRA VERIFICATION FOR STEP 09

Verify batch isolation.
List all changed commands/APIs and compare them to `COMMANDS_TO_IMPLEMENT`.
Fail if any command outside the batch was implemented, unless it is a small supporting helper documented in the report.
Run:

```powershell
git diff --name-only
git diff -- pymeasure/instruments/$vendor/$model.py tests/instruments/$vendor/test_$model.py
```


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

Report batch name, files changed, commands implemented/excluded, tests added, pytest result, import check result, coverage rows updated, `git diff --check`, and `git diff --stat`.
```
