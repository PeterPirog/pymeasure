# Prompt 03 — Optimize Operator / Operation Manual for PyMeasure safety planning

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

STEP_ID = 03
STEP_NAME = optimize_operator_manual_for_llm

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
INPUT_CANDIDATES:
- assets/<VENDOR>/<MODEL>/operators_manual.md
- assets/<VENDOR>/<MODEL>/operation_manual.md
- assets/<VENDOR>/<MODEL>/manual.md

OUTPUT_FILE = assets/<VENDOR>/<MODEL>/operators_manual_llm.md

MAIN GOAL

Create `operators_manual_llm.md`, an LLM/PyMeasure-oriented safety and operation knowledge base.

Use this file for safe hardware-test policy, physical DUT connection constraints, remote interface setup context, warm-up and reset behavior, model/option constraints, and error-code interpretation.

Do not use the Operators Manual as the authoritative source for complete remote command syntax. If command-like tokens are mentioned, list them only as cross-references requiring Programming Guide confirmation.

Do not implement code.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/operators_manual_llm.md

TASKS

1. Find the first existing input file from INPUT_CANDIDATES.
2. If none exists, stop and report checked paths.
3. Extract and reorganize the manual into the sections below.
4. Preserve model and option limitations exactly as stated.
5. Mark ambiguous OCR/conversion artifacts as `needs-verification`.

OUTPUT STRUCTURE

1. YAML front matter.
2. `LLM_AGENT_CONTRACT`.
3. `DOCUMENT ROLE IN PYMEASURE WORKFLOW`.
4. `QUICK FACTS FOR RETRIEVAL`.
5. `SAFETY SUMMARY FOR DRIVER AND HARDWARE TEST PLANNING`.
6. `REMOTE OPERATION AND INTERFACE SUMMARY`.
7. `REMOTE PORT SETUP FACTS`.
8. `OPERATE / STANDBY / RESET BEHAVIOR`.
9. `DUT CONNECTION AND FIXTURE CONSTRAINTS`.
10. `OUTPUT / INPUT FUNCTION MAP FOR PYMEASURE PLANNING`.
11. `MODEL AND OPTION DEPENDENCIES`.
12. `WARM-UP, ZEROING, AND METROLOGY PREREQUISITES`.
13. `PERSISTENT SETTINGS / CALIBRATION SECURITY`.
14. `ERROR-CODE KNOWLEDGE BASE`.
15. `HARDWARE-TEST POLICY`.
16. `COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION`.
17. `PYMEASURE DESIGN IMPLICATIONS`.
18. `OCR_AND_CONVERSION_NOTES`.

Use these hardware-test policies only:

- query-only
- output-off-only
- roundtrip-safe
- operator-confirmed-only
- protocol-only
- never
- needs-verification

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$output = "$assetDir/operators_manual_llm.md"

Test-Path $output
Get-Content $output -TotalCount 160
Select-String -Path $output -Pattern "LLM_AGENT_CONTRACT", "SAFETY SUMMARY", "REMOTE OPERATION", "STANDBY", "HARDWARE-TEST POLICY"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 03

Verify that command-like tokens from the Operators/Operation Manual are isolated as cross-references only.
Run:

```powershell
Select-String -Path $output -Pattern "COMMAND-LIKE REFERENCES", "Programming Guide confirmation", "HARDWARE-TEST POLICY", "operator-confirmed-only", "never"
git diff --name-only
```

Allowed changed paths are `operators_manual_llm.md` and this step report only.


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

Report input file used, output path, highest-risk test topics, remote interfaces found, model/option dependencies, command-like references isolated, and results of `git diff --check` and `git diff --stat`.
```
