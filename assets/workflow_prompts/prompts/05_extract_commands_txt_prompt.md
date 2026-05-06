# Prompt 05 — Extract all commands from Programming Guide to commands.txt

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: kimi-k2.6:cloud or qwen3.6:latest
Physical instrument access required: NO. Command extraction from manuals only.

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

STEP_ID = 05
STEP_NAME = extract_commands_txt

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
PRIMARY_SOURCE = assets/<VENDOR>/<MODEL>/programming_guide.md
OPTIONAL_OPTIMIZED_SOURCE = assets/<VENDOR>/<MODEL>/programming_guide_llm.md
OPTIONAL_OPERATOR_CONTEXT = assets/<VENDOR>/<MODEL>/operators_manual_llm.md
OPTIONAL_SERVICE_CONTEXT = assets/<VENDOR>/<MODEL>/service_manual_llm.md
OUTPUT_FILE = assets/<VENDOR>/<MODEL>/commands.txt

MAIN GOAL

Create `commands.txt`.

The file must contain an audit-friendly inventory of all remote-control commands found in the Programming Guide.

Remote command syntax must come only from the Programming Guide source. Operator/service manuals may only add risk notes or test-policy hints. They must not add commands to the main inventory unless the same command is confirmed in the Programming Guide.

Do not implement a driver.
Do not create `command_coverage.md`.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or real hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/commands.txt

COMMAND DISCOVERY STRATEGY

Extract commands from all useful programming-guide regions:

1. command index,
2. command summary,
3. table of contents command entries,
4. detailed command reference sections,
5. common commands section,
6. subsystem command sections,
7. appendix containing command list.

Use detailed command sections as higher authority when they conflict with summaries or TOC.

Deduplicate commands, but do not remove meaningful variants if they differ by query form, optional path, index notation, subsystem, command family, or command-only/query-only behavior.

OUTPUT STRUCTURE

Create `commands.txt` with:

1. Header:
   - instrument,
   - vendor,
   - model,
   - class name,
   - instrument type,
   - programming guide source,
   - generated on,
   - local artifact notice.

2. `SOURCE RULES`.

3. `COMMAND FORM LEGEND` using only:
   - command only
   - query only
   - command/query
   - unknown
   - needs-verification

4. `COMMAND INVENTORY`.

The first line of inventory must be exactly:

Subsystem | Command | Form | Short description | Source evidence | Notes

Each command row must use exactly:

<Subsystem> | <Command> | <Form> | <Short description> | <Source evidence> | <Notes>

Subsystem values may include:
Common, Status, System, Output, Source, Input, Sense, Measure, Trigger, Arm, Initiate, Calculate, Trace, Marker, Display, Memory, MMEMory, Format, Calibration, Diagnostic, Test, Communication, Other.

5. `COMMAND COUNTS`.

Include:
- Total unique commands
- command only
- query only
- command/query
- unknown
- needs-verification
- counts by subsystem

6. `COMMAND GROUPS FOR NEXT WORKFLOW STEP`.

Groups:
- Common/status commands
- Error/status queue commands
- Input/channel commands
- Source/output commands
- Measurement/sense commands
- Trigger/arm/initiate commands
- Calculate/trace/data commands
- Display/window/marker commands
- Format/data-transfer commands
- Memory/file commands
- Calibration/adjustment commands
- Diagnostic/test commands
- Model/option-dependent commands
- Commands requiring manual verification

7. `PARSER CANDIDATES`.

Format:

Command | Reason | Source evidence | Notes

8. `RISK HINTS FOR LATER HARDWARE TEST DESIGN`.

Format:

Command or topic | Risk hint | Suggested later hardware-test policy | Source evidence | Notes

Use only:
query-only, output-off-only, roundtrip-safe, operator-confirmed-only, protocol-only, never, needs-verification.

9. `COMMAND-LIKE REFERENCES FROM NON-PROGRAMMING SOURCES`.

Use only if operator/service sources mention unconfirmed command-like tokens.

10. `PYMEASURE NOTES FOR NEXT PROMPT`.

Include:
- use `SCPIMixin, Instrument` if Programming Guide confirms IEEE-488.2/SCPI common commands,
- do not use `includeSCPI=True`,
- command/query -> later `Instrument.control` after API design,
- query-only -> later `Instrument.measurement` or explicit method,
- command-only action -> method,
- block/table/report -> method + parser,
- no `get_*` or `set_*`,
- hardware tests skip without VISA address,
- destructive commands must be protocol-only, operator-confirmed-only, never, or deferred.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$commands = "$assetDir/commands.txt"

Test-Path $commands
Get-Content $commands -TotalCount 160
Select-String -Path $commands -Pattern "\*IDN\?", "\*RST", "\*CLS", "\*OPC", "\*WAI"
Select-String -Path $commands -Pattern "COMMAND COUNTS", "PARSER CANDIDATES", "RISK HINTS", "needs-verification"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 05

Verify completeness and traceability of `commands.txt`.
Run:

```powershell
Select-String -Path $commands -Pattern "COMMAND INVENTORY", "COMMAND COUNTS", "PARSER CANDIDATES", "RISK HINTS"
Select-String -Path $commands -Pattern "Source evidence"
git diff --name-only
```

Fail this step if the inventory has no counts, no source evidence, or no `needs-verification` mechanism.
Allowed changed paths are `commands.txt` and this step report only.


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

Report output path, total unique commands, counts by form, top subsystems, parser candidates, risky command groups, confirmation that only `commands.txt` changed, and results of `git diff --check` and `git diff --stat`.
```
