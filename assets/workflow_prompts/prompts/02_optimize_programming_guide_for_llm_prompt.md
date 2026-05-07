Prompt 02 — Optimize Programming Guide for LLM retrieval
```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.

EXECUTION MODE REQUIRED.

Create or update the required files now. Do not only describe the steps. Do not only return snippets.
Apply file changes directly in the repository and run the acceptance commands.

If file writing is blocked, stop and report in chat:
BLOCKED: missing file-write permission

If terminal execution is blocked, still create the report file with STATUS: FAIL and
HUMAN_REQUIRED: yes, and explain that terminal execution is blocked.

============================================================
CENTRAL WORKFLOW CONFIGURATION
============================================================

Do not hard-code vendor/model paths in this prompt.
Read the instrument configuration from this file:

CONFIG_FILE = assets/workflow_prompts/workflow_config.json

The config file is the single source of truth for:

- vendor
- model
- class_name
- instrument_type
- pymeasure_vendor_package
- model_lower
- visa_address_example
- asset_dir
- manual paths
- workflow_reports_dir

Expected JSON keys:

{
  "vendor": "fluke",
  "model": "5560A",
  "class_name": "Fluke5560A",
  "instrument_type": "multifunction precision calibrator / precision source calibrator",
  "pymeasure_vendor_package": "fluke",
  "model_lower": "5560a",
  "visa_address_example": "GPIB0::4::INSTR",
  "asset_dir": "assets/fluke/5560A",
  "manuals": {
    "programming_guide": "assets/fluke/5560A/programming_guide.md",
    "operator_manual_candidates": [
      "assets/fluke/5560A/operators_manual.md",
      "assets/fluke/5560A/operators_guide.md",
      "assets/fluke/5560A/operation_manual.md",
      "assets/fluke/5560A/manual.md"
    ],
    "service_manual": "assets/fluke/5560A/service_manual.md"
  },
  "workflow_reports_dir": "assets/fluke/5560A/workflow_reports"
}

If CONFIG_FILE does not exist, stop and create a report file only if the report directory can be inferred.
Otherwise report in chat:

STATUS: FAIL
HUMAN_REQUIRED: yes
BLOCKER: missing workflow_config.json

Do not continue using fallback hard-coded paths.

Derived paths for this step must be built from CONFIG_FILE:

ASSET_DIR = config.asset_dir
INPUT_FILE = config.manuals.programming_guide
OUTPUT_FILE = config.asset_dir + "/programming_guide_llm.md"
REPORT_DIR = config.workflow_reports_dir
REPORT_FILE = config.workflow_reports_dir + "/02_optimize_programming_guide_for_llm_report.md"

============================================================
MODEL AND HARDWARE ACCESS
============================================================

Recommended model for this step: hal/kimi-k2.6:cloud
Fallback model: hal/qwen3.5:397b-cloud
Execution-agent fallback: hal/qwen3-coder-next:cloud

Physical instrument access required: NO.
This step is manual transformation only.

visa_address_example from CONFIG_FILE is only metadata for local instructions and generated commands.
A cloud model cannot access a local GPIB/USB/LAN/RS-232 instrument directly.
Real hardware communication may only happen on the operator's local computer or explicitly configured local runner.

============================================================
UPSTREAM PYMEASURE AGENTS.MD COMPLIANCE
============================================================

Before editing, read the repository-level `AGENTS.md` file if it exists.
Follow it as the highest-priority local repository rule set.

For this step, the relevant rules are:

- Do not invent device-specific SCPI commands.
- Use source manuals as authority for device-specific behavior.
- Preserve command syntax exactly as documented.
- Do not implement any driver in this step.
- Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.

============================================================
STEP METADATA
============================================================

STEP_ID = 02
STEP_NAME = optimize_programming_guide_for_llm

Use instrument metadata from CONFIG_FILE:

VENDOR = config.vendor
MODEL = config.model
CLASS_NAME = config.class_name
INSTRUMENT_TYPE = config.instrument_type

============================================================
MAIN GOAL
============================================================

Create or update:

- OUTPUT_FILE
- REPORT_FILE

The report file is mandatory. The step is not complete until REPORT_FILE exists.

The output file must be an LLM-optimized reference for later PyMeasure driver planning.

This step must NOT create a complete command inventory.
The complete command inventory belongs to Prompt 05 and must be written to `commands.txt`.

In this step, extract and reorganize only:

- source authority rules,
- document navigation map,
- remote interface notes,
- SCPI / remote command notation rules,
- data transfer and parser-relevant notes,
- command extraction hints for Prompt 05,
- safety and risk hints from the Programming Guide,
- OCR/conversion uncertainty notes.

Do not implement a driver.
Do not create `commands.txt`.
Do not create or fill `command_coverage.md`.
Do not modify `pymeasure/instruments/`.
Do not modify `tests/`.
Do not modify `docs/`.
Do not use VISA.
Do not communicate with real hardware.

Allowed changed paths are exactly:

- OUTPUT_FILE
- REPORT_FILE

If any other path is modified, set STATUS: FAIL.

============================================================
SOURCE AUTHORITY RULES
============================================================

1. Remote command syntax must come only from INPUT_FILE.

2. Do not invent:

   - commands,
   - command forms,
   - query forms,
   - parameters,
   - response formats,
   - value ranges,
   - units,
   - examples,
   - VISA addresses,
   - safety limits.

3. Preserve manufacturer notation:

   - uppercase/lowercase command abbreviations,
   - optional nodes,
   - indexes,
   - suffixes,
   - query markers `?`,
   - documented parameter notation.

4. Documentation brackets are notation, not literal command characters.

5. Mark OCR or Markdown conversion ambiguity as:

   needs-verification

6. Do not claim that the output contains all commands.

7. Do not claim that OCR is perfect unless a full manual-wide consistency audit was performed.
   Prefer:

   No obvious OCR artifacts detected in reviewed sections.

8. Do not provide command examples unless they are explicitly present in the Programming Guide
   or clearly marked as non-authoritative notation examples.

9. Never introduce `*IDN` as a set command unless the Programming Guide explicitly documents it.
   If only `*IDN?` is documented, use only `*IDN?`.

10. If a statement is inferred, mark it as:

    inference-needs-verification

============================================================
OUTPUT STRUCTURE
============================================================

Create `programming_guide_llm.md` with exactly these top-level sections:

1. YAML front matter
2. `LLM_AGENT_CONTRACT`
3. `DOCUMENT ROLE IN WORKFLOW`
4. `DOCUMENT MAP`
5. `REMOTE INTERFACE NOTES`
6. `REMOTE COMMUNICATION FORMAT NOTES`
7. `COMMAND NOTATION GUIDE`
8. `COMMAND EXTRACTION HINTS FOR PROMPT 05`
9. `DATA TRANSFER AND PARSER NOTES`
10. `STATUS, ERROR, AND SYNCHRONIZATION NOTES`
11. `SAFETY AND RISK HINTS FROM PROGRAMMING GUIDE`
12. `DO-NOT-INFER LIST`
13. `OCR_AND_CONVERSION_NOTES`
14. `STEP 05 HANDOFF CHECKLIST`

YAML front matter must include:

title:
source_file:
vendor:
model:
class_name:
instrument_type:
workflow_step: 02
full_command_inventory_created: false
complete_command_extraction_deferred_to: "Prompt 05 commands.txt"
generated_on:
local_artifact: true
upstream_pr: false

`LLM_AGENT_CONTRACT` must state:

- Use this file for retrieval and planning only.
- Use the Programming Guide as the source for command syntax.
- Do not use this file as a full command inventory.
- Full command inventory must be produced in Prompt 05.
- Do not implement code from this file alone.
- Do not run hardware tests from this file alone.

`DOCUMENT ROLE IN WORKFLOW` must contain this table:

| File | Role | Not allowed |
|---|---|---|
| programming_guide.md | authoritative source for remote command syntax | unsafe direct hardware execution |
| programming_guide_llm.md | LLM/RAG planning aid | complete command inventory |
| commands.txt | complete command inventory from Prompt 05 | invented commands |
| command_coverage.md | API/test/status mapping | command syntax not in commands.txt |

`DOCUMENT MAP` must identify likely source regions for:

- table of contents,
- command index,
- command summary tables,
- detailed command reference,
- status/event registers,
- error handling,
- data formats,
- remote interface setup,
- safety warnings.

Use source evidence as headings, table names, or nearby source text.
Do not use line numbers unless they are stable and directly verified.

`REMOTE INTERFACE NOTES` must list only interfaces confirmed in INPUT_FILE.

Use this table:

| Interface | Confirmed? | Setup facts | Termination/EOL | SRQ/status notes | Source evidence | Notes |
|---|---:|---|---|---|---|---|

If a resource string is not documented, write:

not specified

Do not invent USB VID/PID or TCP port values.

`REMOTE COMMUNICATION FORMAT NOTES` must extract facts about:

- command termination,
- response termination,
- EOI,
- CR/LF/CRLF,
- ASCII responses,
- numeric formats,
- string formats,
- CRD/keyword responses,
- binary block data,
- error queue behavior.

`COMMAND NOTATION GUIDE` must describe notation rules without inventing unsupported commands.

Allowed examples:

- Use command examples only if they are explicitly visible in INPUT_FILE.
- Otherwise write notation without examples.

Forbidden example:

- Do not write `*IDN` as a set command unless explicitly documented.

`COMMAND EXTRACTION HINTS FOR PROMPT 05` must identify where Prompt 05 should look for all commands.

It must include this exact warning:

This section is not the command inventory. Prompt 05 must re-read `programming_guide.md` and extract all commands into `commands.txt`.

Use this table:

| Source region | What to extract in Prompt 05 | Authority level | Risk of incompleteness | Notes |
|---|---|---|---|---|

`DATA TRANSFER AND PARSER NOTES` must extract every found statement about:

- ASCII data,
- binary blocks,
- definite length blocks,
- indefinite length blocks,
- REAL / float formats,
- byte order,
- headers,
- point counts,
- arrays,
- lists,
- trace/table/waveform transfers,
- long text responses,
- parser requirements.

Use this table:

| Topic | Fact from Programming Guide | Source evidence | Parser implication | needs-verification |
|---|---|---|---|---|

`STATUS, ERROR, AND SYNCHRONIZATION NOTES` must list concepts such as:

- `*OPC?`,
- `*WAI`,
- status byte,
- event status register,
- service request,
- error/fault queue,
- serial/SRQ limitations.

Only include command names if present in INPUT_FILE.

`SAFETY AND RISK HINTS FROM PROGRAMMING GUIDE` must include safety-relevant statements from INPUT_FILE only.

Use this table:

| Topic | Risk hint | PyMeasure implication | Hardware-test implication | Source evidence |
|---|---|---|---|---|

`DO-NOT-INFER LIST` must include:

- Do not infer command syntax from natural-language function names.
- Do not infer query forms from set forms.
- Do not infer set forms from query forms.
- Do not infer value ranges unless documented.
- Do not infer hardware safety from command names.
- Do not treat interface messages as data commands.
- Do not treat high-value command examples as complete inventory.

`OCR_AND_CONVERSION_NOTES` must be conservative.

Allowed wording:

- No obvious OCR artifacts detected in reviewed sections.
- Some sections may still require verification during Prompt 05.
- Command syntax with unusual symbols must be checked against the source.

Forbidden wording unless fully proven:

- No OCR errors detected.
- Documentation quality is high.
- Needs-verification items: none.

`STEP 05 HANDOFF CHECKLIST` must list the exact checks Prompt 05 must perform:

- re-read `programming_guide.md`,
- extract from index and detailed command reference,
- deduplicate but preserve meaningful variants,
- classify command-only/query-only/command-query,
- mark ambiguous entries `needs-verification`,
- create `commands.txt`,
- do not rely only on high-value commands from `programming_guide_llm.md`.

============================================================
FORBIDDEN OUTPUT PATTERNS
============================================================

The output file and report must not contain these claims unless exactly true and proven:

- "extracted all SCPI command syntax"
- "all source commands preserved"
- "No OCR errors detected"
- "Needs-Verification Items: None"
- "Proceed to driver skeleton"
- "Proceed to protocol development"
- "`*IDN` | Set"
- "`*IDN` as set command"
- "full command inventory"

The phrase `full command inventory` is allowed only when saying exactly:

full command inventory is deferred to Prompt 05

============================================================
MANDATORY REPORT FILE
============================================================

Always create or update REPORT_FILE.

The report file must be created even if the step fails.

If OUTPUT_FILE is created but REPORT_FILE is missing, the step is FAIL.

The report must contain these exact fields:

STATUS: PASS or FAIL
HUMAN_REQUIRED: yes or no
STEP_ID: 02
STEP_NAME: optimize_programming_guide_for_llm
CONFIG_FILE:
FILES_CREATED_OR_UPDATED:
COMMANDS_RUN:
ACCEPTANCE_RESULTS:
COUNTS:
NEEDS_VERIFICATION_ITEMS:
FORBIDDEN_PATTERN_CHECK:
ALLOWED_PATH_CHECK:
PYMEASURE_AGENTS_COMPLIANCE:
BLOCKERS:
NEXT_RECOMMENDED_STEP:

The only valid next-step recommendation is:

Proceed to Step 03: optimize Operator/Operation Manual for LLM/PyMeasure safety planning.

If the operator manual is unavailable, recommend:

Proceed to Step 03 and mark it as skipped only after checking input candidates.

Use `STATUS: FAIL` if:

- CONFIG_FILE is missing,
- INPUT_FILE is missing,
- OUTPUT_FILE was not created,
- REPORT_FILE was not created,
- files outside allowed scope were modified,
- any forbidden output pattern appears,
- output claims complete command extraction,
- output treats high-value commands as complete command inventory,
- `git diff --check` reports whitespace errors,
- next-step recommendation skips to implementation,
- terminal execution is blocked.

============================================================
ACCEPTANCE COMMANDS
============================================================

Run in PowerShell. Use values from CONFIG_FILE, not hard-coded vendor/model paths.

```powershell
$configPath = "assets/workflow_prompts/workflow_config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$assetDir = $config.asset_dir
$output = "$assetDir/programming_guide_llm.md"
$reportDir = $config.workflow_reports_dir
$report = "$reportDir/02_optimize_programming_guide_for_llm_report.md"

Test-Path $configPath
Test-Path $output
Test-Path $report

Get-Content $output -TotalCount 180
Get-Content $report -TotalCount 120

Select-String -Path $output -Pattern `
  "LLM_AGENT_CONTRACT", `
  "DOCUMENT ROLE IN WORKFLOW", `
  "DOCUMENT MAP", `
  "REMOTE INTERFACE NOTES", `
  "COMMAND EXTRACTION HINTS FOR PROMPT 05", `
  "DATA TRANSFER AND PARSER NOTES", `
  "STEP 05 HANDOFF CHECKLIST"

Select-String -Path $output -Pattern `
  "full command inventory is deferred to Prompt 05", `
  "This section is not the command inventory", `
  "Do not infer query forms", `
  "Do not infer set forms"

$forbidden = @(
  "extracted all SCPI command syntax",
  "all source commands preserved",
  "No OCR errors detected",
  "Needs-Verification Items: None",
  "Proceed to driver skeleton",
  "Proceed to protocol development",
  "\*IDN`?\s*\|\s*Set",
  "\*IDN\s+as set command"
)

foreach ($pattern in $forbidden) {
    Select-String -Path $output, $report -Pattern $pattern
}

$changed = git diff --name-only
$changed
$allowed = @(
  ($output -replace "\\", "/"),
  ($report -replace "\\", "/")
)

$unexpected = $changed | Where-Object { $_ -notin $allowed }
if ($unexpected) {
    Write-Output "UNEXPECTED_CHANGED_PATHS:"
    $unexpected
}

git status --short
git diff --check
git diff --stat
```
Important interpretation:
`Test-Path $configPath` must be `True`.
`Test-Path $output` must be `True`.
`Test-Path $report` must be `True`.
The forbidden-pattern `Select-String` calls should return no matches.
`UNEXPECTED_CHANGED_PATHS` must not appear.
If report file is missing, set `STATUS: FAIL`.
============================================================
FINAL CHAT RESPONSE
At the end, report in chat:
config file path,
output file path,
report file path,
source file path,
whether full command inventory was deferred to Prompt 05,
key command-list source sections found,
data-transfer/parser sections found,
any uncertainty or `needs-verification`,
forbidden pattern check result,
allowed path check result,
whether report file exists,
result of `git diff --check`,
result of `git diff --stat`,
`STATUS: PASS` or `STATUS: FAIL`,
`HUMAN_REQUIRED: yes/no`.
```