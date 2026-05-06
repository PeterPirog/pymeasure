# Prompt 02 — Optimize Programming Guide for LLM retrieval

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: kimi-k2.6:cloud or qwen3.6:latest
Physical instrument access required: NO. Manual transformation only.

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

STEP_ID = 02
STEP_NAME = optimize_programming_guide_for_llm

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
INPUT_FILE = assets/<VENDOR>/<MODEL>/programming_guide.md
OUTPUT_FILE = assets/<VENDOR>/<MODEL>/programming_guide_llm.md

MAIN GOAL

Create `programming_guide_llm.md`, an LLM-optimized reference for later PyMeasure driver planning.

Do not implement a driver.
Do not create `commands.txt`.
Do not create `command_coverage.md`.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or real hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/programming_guide_llm.md

SOURCE AUTHORITY RULES

1. Remote command syntax must come from `programming_guide.md`.
2. Do not invent commands, parameters, response formats, value ranges, or examples.
3. Preserve manufacturer notation:
   - uppercase/lowercase SCPI abbreviations,
   - optional nodes,
   - indexes,
   - `?` query markers,
   - suffix notation.
4. Do not transmit documentation brackets as literal command characters.
5. Mark OCR/conversion ambiguity as `needs-verification`.

OUTPUT STRUCTURE

Create `programming_guide_llm.md` with these sections:

1. YAML front matter.
2. `LLM_AGENT_CONTRACT`.
3. `DOCUMENT MAP`.
4. `REMOTE INTERFACE NOTES`.
5. `SCPI NOTATION GUIDE`.
6. `HIGH-VALUE COMMANDS`.
7. `DATA TRANSFER NOTES`.
8. `COMMAND EXTRACTION HINTS FOR commands.txt`.
9. `SAFETY AND RISK HINTS FROM PROGRAMMING GUIDE`.
10. `OCR_AND_CONVERSION_NOTES`.

For `DATA TRANSFER NOTES`, extract every statement about ASCII data, binary blocks, REAL/float formats, byte order, headers, point counts, trace/waveform/table transfers, and parser requirements.

For `COMMAND EXTRACTION HINTS`, identify where the complete command list is located: command index, appendix, TOC, summary table, and detailed command reference. State priority rules.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$output = "$assetDir/programming_guide_llm.md"

Test-Path $output
Get-Content $output -TotalCount 160
Select-String -Path $output -Pattern "LLM_AGENT_CONTRACT", "DOCUMENT MAP", "SCPI NOTATION", "DATA TRANSFER", "COMMAND EXTRACTION"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 02

Verify that `programming_guide_llm.md` contains clear source-authority rules and does not invent commands.
Run:

```powershell
Select-String -Path $output -Pattern "Do not invent", "Programming Guide", "needs-verification", "DATA TRANSFER", "COMMAND EXTRACTION"
git diff --name-only
```

Allowed changed paths are `programming_guide_llm.md` and this step report only.


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

Report output path, source file, key command-list source sections found, data-transfer sections found, uncertainty, and results of `git diff --check` and `git diff --stat`.
```
