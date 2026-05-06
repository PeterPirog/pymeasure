# Prompt 09 — Produce architecture and batch plan before implementation

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: deepseek-v4-pro:cloud
Physical instrument access required: NO. Architecture planning only.

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

STEP_ID = 09
STEP_NAME = architecture_and_batches

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator
PYMEASURE_VENDOR_PACKAGE = fluke

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
COMMANDS_FILE = assets/<VENDOR>/<MODEL>/commands.txt
COVERAGE_FILE = assets/<VENDOR>/<MODEL>/command_coverage.md
PROGRAMMING_GUIDE_LLM = assets/<VENDOR>/<MODEL>/programming_guide_llm.md
OPERATORS_MANUAL_LLM = assets/<VENDOR>/<MODEL>/operators_manual_llm.md
SERVICE_MANUAL_LLM = assets/<VENDOR>/<MODEL>/service_manual_llm.md
OUTPUT_FILE = assets/<VENDOR>/<MODEL>/architecture_plan.md

MAIN GOAL

Create `architecture_plan.md`.

This plan must decide the PyMeasure class architecture and implementation batches before any driver code is written.

Do not implement code.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/architecture_plan.md

TASKS

1. Read `commands.txt` and `command_coverage.md`.
2. Identify instrument type, command subsystem tree, global commands, indexed channel/window/trace commands, data-transfer commands, risky commands, long-running commands, and model/option dependencies.
3. Decide architecture:
   - single `Instrument` class,
   - `Instrument` + `Channel`,
   - `Instrument` + `ChannelCreator`,
   - `Instrument` + `MultiChannelCreator`,
   - trace/window helper classes,
   - parser methods.
4. Recommend implementation batches.

OUTPUT STRUCTURE

1. Header.
2. `INSTRUMENT CLASSIFICATION`.
3. `REMOTE COMMAND TREE`.
4. `PYMEASURE ARCHITECTURE DECISION`.
5. `CLASS AND API SKETCH`.
6. `RISK AND SAFETY DESIGN`.
7. `IMPLEMENTATION BATCH PLAN`.
8. `BATCH 1 EXACT SCOPE`.
9. `DO NOT IMPLEMENT YET`.

Rules:
- Use `SCPIMixin, Instrument` if Programming Guide confirms SCPI/IEEE-488.2 common commands.
- Do not use `includeSCPI=True`.
- Do not design public `get_*` or `set_*`.
- Use parser methods for block/table/trace data.
- Use channels or helper classes only where they make the API clearer and fit the manual.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$plan = "$assetDir/architecture_plan.md"

Test-Path $plan
Get-Content $plan -TotalCount 200
Select-String -Path $plan -Pattern "PYMEASURE ARCHITECTURE DECISION", "IMPLEMENTATION BATCH PLAN", "BATCH 1 EXACT SCOPE"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 07

Verify that the architecture plan contains a batch-1 exact scope and explicit do-not-implement boundaries.
Run:

```powershell
Select-String -Path $plan -Pattern "SCPIMixin", "ChannelCreator", "MultiChannelCreator", "parser", "BATCH 1 EXACT SCOPE", "DO NOT IMPLEMENT"
git diff --name-only
```

Fail if the architecture does not explicitly choose between single class, channels, MultiChannelCreator, or helper classes.


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

Report output path, chosen architecture, whether channels/helpers are needed, first batch scope, highest-risk deferred groups, confirmation that only `architecture_plan.md` changed, and results of `git diff --check` and `git diff --stat`.
```
