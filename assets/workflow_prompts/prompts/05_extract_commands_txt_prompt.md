# Prompt 05 - Extract `commands.txt` from Programming Guide

Version: v11 - self-contained Qwen Coder execution prompt, config-driven, source-readonly

---

## 1. ROLE

You are an execution-oriented coding agent working inside the local PyMeasure repository.

Your task is to create a reliable command inventory artifact for a PyMeasure instrument-driver workflow.

This is not a planning task. This is not a discussion task. This is a repository file-generation task.

Your first substantive action must be to inspect the repository and create or update the required Step 05 files.

---

## 2. OBJECTIVE

Create a complete, auditable command inventory from the instrument Programming Guide.

The command inventory must be written to:

```text
config.asset_dir + "/commands.txt"
```

A Step 05 execution report must be written to:

```text
config.workflow_reports_dir + "/05_extract_commands_txt_report.md"
```

Both paths must be derived from:

```text
assets/workflow_prompts/workflow_config.json
```

Do not hard-code the vendor, model, or asset directory.

---

## 3. CONFIGURATION SOURCE

Read this file first:

```text
assets/workflow_prompts/workflow_config.json
```

Use only this config for repository paths and metadata.

Required config fields:

```text
vendor
model
class_name
instrument_type
pymeasure_vendor_package
model_lower
visa_address_example
asset_dir
manuals.programming_guide
manuals.operator_manual_candidates
manuals.service_manual
workflow_reports_dir
```

Derived runtime variables:

```text
ASSET_DIR = config.asset_dir
PROGRAMMING_GUIDE = config.manuals.programming_guide
PROGRAMMING_GUIDE_LLM = config.asset_dir + "/programming_guide_llm.md"
OPERATORS_MANUAL_LLM = config.asset_dir + "/operators_manual_llm.md"
SERVICE_MANUAL_LLM = config.asset_dir + "/service_manual_llm.md"
COMMANDS_FILE = config.asset_dir + "/commands.txt"
REPORT_FILE = config.workflow_reports_dir + "/05_extract_commands_txt_report.md"
PROMPT_FILE = assets/workflow_prompts/prompts/05_extract_commands_txt_prompt.md
```

---

## 4. SOURCE AUTHORITY

Only `PROGRAMMING_GUIDE` is authoritative for command syntax.

`PROGRAMMING_GUIDE_LLM` may be used only as a navigation aid.

`OPERATORS_MANUAL_LLM` and `SERVICE_MANUAL_LLM` may be used only for risk hints. They must not introduce commands into `COMMAND INVENTORY` unless the same command is confirmed in `PROGRAMMING_GUIDE`.

---

## 5. REQUIRED OUTPUT FILES

You must create or update exactly these Step 05 artifacts:

```text
COMMANDS_FILE
REPORT_FILE
```

The final answer in chat is not the deliverable. The repository files are the deliverables.

---

## 6. READ-ONLY INPUTS

Do not modify:

```text
PROGRAMMING_GUIDE
PROGRAMMING_GUIDE_LLM
OPERATORS_MANUAL_LLM
SERVICE_MANUAL_LLM
config.manuals.service_manual
all paths in config.manuals.operator_manual_candidates
```

Do not modify any file under:

```text
pymeasure/instruments/
tests/
docs/
```

Do not create or modify:

```text
command_coverage.md
```

Do not use VISA or real hardware.

Physical instrument access is not required for this step.

---

## 7. FORBIDDEN ACTIONS

These actions are forbidden:

```text
Do not read, copy, move, rename, delete, or modify files under obsolete/ or _obsolete_/.
Do not use obsolete/commands.txt.
Do not use Move-Item from obsolete/commands.txt.
Do not use an obsolete command inventory as a source.
Do not leave helper scripts inside the repository.
Do not create driver code.
Do not create protocol tests.
Do not create hardware tests.
Do not create Sphinx documentation.
Do not claim a driver was implemented.
Do not claim hardware safety.
```

Temporary scripts are allowed only outside the repository, for example under `%TEMP%`.

If any obsolete or `_obsolete_` path is already modified before the run, do not repair it silently. Create `REPORT_FILE` with:

```text
STATUS: FAIL
HUMAN_REQUIRED: yes
```

and list the modified obsolete path as a blocker.

---

## 8. EXECUTION DIRECTIVES

Follow this execution order.

### 8.1 Preflight

1. Read `workflow_config.json`.
2. Resolve all derived paths.
3. Check that `PROGRAMMING_GUIDE` exists.
4. Check Git status for modified paths under `obsolete/` or `_obsolete_/`.

If `PROGRAMMING_GUIDE` is missing, create `REPORT_FILE` with `STATUS: FAIL` and stop.

If obsolete paths are modified, create `REPORT_FILE` with `STATUS: FAIL` and stop.

### 8.2 Create required files early

Before deep extraction, create both files:

```text
COMMANDS_FILE
REPORT_FILE
```

`COMMANDS_FILE` may initially contain only the required skeleton.

`REPORT_FILE` must initially contain:

```text
STATUS: FAIL
HUMAN_REQUIRED: yes
STEP_ID: 05
STEP_NAME: extract_commands_txt
BLOCKERS:
- extraction not completed yet
```

Then continue. Do not stop after writing the initial report.

### 8.3 Extraction

Extract remote-control command candidates from `PROGRAMMING_GUIDE`.

Use all relevant regions:

```text
command index
command summary
table of contents command entries
common commands section
subsystem command sections
detailed command reference sections
appendices containing command lists
status/error/reference sections containing remote commands
```

Detailed command-reference sections are higher authority than summaries or TOC entries.

Deduplicate exact duplicate commands, but preserve meaningful variants when they differ by:

```text
query form
command-only form
optional path
index notation
channel/trace/window/address parameter
subsystem
response/data-transfer behavior
model or option dependency
```

Do not invent commands, query forms, parameters, ranges, validators, or safety policies.

### 8.4 Exact command-form semantics

Use exact literal form semantics.

Rules:

```text
CMD  -> command only
CMD? -> query only
```

If the manual documents both `CMD` and `CMD?`, list them as two rows:

```text
Subsystem | CMD  | command only | ...
Subsystem | CMD? | query only   | ...
```

Do not mark separate literal rows as `command/query`.

Use `command/query` only when the `Command` cell explicitly combines both forms in one row, for example:

```text
CMD / CMD? | command/query
```

Prefer separate literal rows over combined rows.

### 8.5 Source evidence

Every inventory row must include source evidence.

Source evidence must point to `PROGRAMMING_GUIDE`, preferably in this form:

```text
assets/.../programming_guide.md:L<number>; <nearby heading or table name>
```

Never use `obsolete/commands.txt` or any non-programming source as evidence for command syntax.

### 8.6 Reporting

After extraction, overwrite `REPORT_FILE` with final PASS/FAIL status.

Do not leave final report with any of these placeholders:

```text
pending
provisional
generation in progress
extraction not completed yet
```

---

## 9. `commands.txt` REQUIRED STRUCTURE

`COMMANDS_FILE` must contain exactly these top-level sections:

```text
# HEADER
# SOURCE RULES
# COMMAND FORM LEGEND
# COMMAND INVENTORY
# COMMAND COUNTS
# COMMAND GROUPS FOR NEXT WORKFLOW STEP
# PARSER CANDIDATES
# RISK HINTS FOR LATER HARDWARE TEST DESIGN
# COMMAND-LIKE REFERENCES FROM NON-PROGRAMMING SOURCES
# PYMEASURE NOTES FOR NEXT PROMPT
# COMPLETENESS AND TRACEABILITY NOTES
```

### 9.1 HEADER

Include:

```text
vendor:
model:
class_name:
instrument_type:
asset_dir:
programming guide source:
auxiliary sources used:
generated_on:
local_artifact: true
upstream_pr: false
command_inventory_created: true
source_authority: programming_guide.md
```

### 9.2 SOURCE RULES

State explicitly:

```text
Command syntax authority is PROGRAMMING_GUIDE only.
Operator/service LLM artifacts may add risk hints only.
Unconfirmed command-like tokens from non-programming sources must not enter COMMAND INVENTORY.
Do not use this file alone to implement a driver without command_coverage.md and API design review.
```

### 9.3 COMMAND FORM LEGEND

Allowed `Form` values:

```text
command only
query only
command/query
unknown
needs-verification
```

### 9.4 COMMAND INVENTORY

The first non-empty inventory line must be exactly:

```text
Subsystem | Command | Form | Short description | Source evidence | Notes
```

Each inventory row must have exactly six cells:

```text
<Subsystem> | <Command> | <Form> | <Short description> | <Source evidence> | <Notes>
```

Allowed `Subsystem` values:

```text
Common
Status
System
Output
Source
Input
Sense
Measure
Trigger
Arm
Initiate
Calculate
Trace
Marker
Display
Memory
MMEMory
Format
Calibration
Diagnostic
Test
Communication
Data
Other
```

### 9.5 COMMAND COUNTS

Include:

```text
Total unique inventory rows:
command only:
query only:
command/query:
unknown:
needs-verification:
counts by subsystem
commands with model/option notes:
commands with risk hints:
parser candidates:
```

Counts must be internally consistent.

### 9.6 PARSER CANDIDATES

Create table:

```text
Command | Reason | Source evidence | Notes
```

Include commands that return or accept:

```text
binary blocks
ASCII tables
lists
arrays
reports
traces
waveforms
status bitfields
error queue messages
option lists
calibration reports
file/memory data
```

If none are found, write a valid placeholder row.

### 9.7 RISK HINTS FOR LATER HARDWARE TEST DESIGN

Create table:

```text
Command or topic | Risk hint | Suggested later hardware-test policy | Source evidence | Notes
```

Allowed hardware-test policies:

```text
query-only
output-off-only
roundtrip-safe
operator-confirmed-only
protocol-only
never
needs-verification
```

Risk hints do not prove safety. They are only inputs for later hardware-test design.

### 9.8 COMMAND-LIKE REFERENCES FROM NON-PROGRAMMING SOURCES

Create table:

```text
Token | Source artifact | Context | Confirmed in Programming Guide? | Decision | Notes
```

Allowed `Decision` values:

```text
confirmed-in-programming-guide
not-found-in-programming-guide
programming-guide-missing
needs-verification
```

Do not add unconfirmed tokens to `COMMAND INVENTORY`.

If no non-programming command-like references were used, write this exact six-column placeholder row:

```text
None | not used | No non-programming sources were used for command extraction | n/a | needs-verification | Placeholder row; no tokens added to inventory
```

### 9.9 PYMEASURE NOTES FOR NEXT PROMPT

Include:

```text
use SCPIMixin, Instrument if Programming Guide confirms IEEE-488.2/SCPI common commands
do not use includeSCPI=True
query-only may later become Instrument.measurement or explicit method
command-only action becomes a method
command/query combined rows may later become Instrument.control after API design
separated command-only and query-only rows may later be paired into one property by command_coverage.md
block/table/report transfer needs method plus parser
no public get_* or set_* methods
hardware tests must skip without VISA address
destructive commands must be protocol-only, operator-confirmed-only, never, or deferred
validators require confirmed ranges/discrete sets from Programming Guide
values/map_values require confirmed token mappings
```

---

## 10. REPORT REQUIRED STRUCTURE

`REPORT_FILE` must contain:

```text
STATUS: PASS or FAIL
HUMAN_REQUIRED: yes or no
STEP_ID: 05
STEP_NAME: extract_commands_txt
CONFIG_FILE:
INPUT_FILE_USED:
AUXILIARY_FILES_USED:
FILES_CREATED_OR_UPDATED:
COMMANDS_RUN:
ACCEPTANCE_RESULTS:
COUNTS:
FORM_VALUE_CHECK:
FORM_SEMANTIC_CHECK:
SUBSYSTEM_VALUE_CHECK:
SOURCE_EVIDENCE_CHECK:
COMMAND_COUNTS_CONSISTENCY_CHECK:
DUPLICATE_COMMAND_CHECK:
COMMAND_LIKE_REFERENCE_CHECK:
PARSER_CANDIDATE_CHECK:
RISK_HINT_CHECK:
HELPER_SCRIPT_CHECK:
GIT_VISIBILITY_CHECK:
OBSOLETE_PATH_CHECK:
FORBIDDEN_MEANING_CHECK:
REPORT_CONSISTENCY_CHECK:
SOURCE_INTEGRITY_CHECK:
LINE_ENDING_WARNING:
PROMPT_MAINTENANCE:
ALLOWED_PATH_CHECK:
PYMEASURE_AGENTS_COMPLIANCE:
BLOCKERS:
NEXT_RECOMMENDED_STEP:
```

`NEXT_RECOMMENDED_STEP` must be exactly:

```text
Proceed to Step 06: create command_coverage.md from commands.txt and PyMeasure API planning.
```

---

## 11. PASS / FAIL RULES

Set:

```text
STATUS: PASS
HUMAN_REQUIRED: no
```

only if all checks pass.

Set:

```text
STATUS: FAIL
HUMAN_REQUIRED: yes
```

if any condition below is true:

```text
COMMANDS_FILE does not exist.
REPORT_FILE does not exist.
COMMANDS_FILE has no inventory rows.
Any inventory row has empty Source evidence.
Any literal command ending in ? has Form different from query only.
Any literal command not ending in ? has Form = query only.
Any separate literal command row has Form = command/query.
Any Form value is outside the allowed set.
Any Subsystem value is outside the allowed set.
Form counts do not sum to Total unique inventory rows.
Subsystem counts do not sum to Total unique inventory rows.
REPORT_FILE counts do not match COMMANDS_FILE counts.
Any obsolete or _obsolete_ path changed.
Any source manual or previous LLM artifact changed.
Any file under pymeasure/instruments/, tests/, docs/, or command_coverage.md changed.
Any helper script remains inside the repository.
git diff --check reports real whitespace errors.
```

LF/CRLF warnings are non-blocking if `git diff --check` exits with code 0.

---

## 12. VERIFICATION COMMANDS

Run these commands after file generation and include the results in the final chat response:

```powershell
Test-Path $commandsFile
Test-Path $reportFile
Test-Path "$assetDir/_build_commands.ps1"

Get-Content $reportFile -TotalCount 280

git status --short --untracked-files=all
git diff --check
git diff --stat
```

---

## 13. FINAL CHAT RESPONSE

After execution, respond only with:

```text
commands.txt exists: true/false
05_extract_commands_txt_report.md exists: true/false
_build_commands.ps1 exists: true/false
STATUS:
HUMAN_REQUIRED:
BLOCKERS:
git status --short --untracked-files=all:
git diff --check:
git diff --stat:
```

Do not claim Step 05 passed unless the report contains:

```text
STATUS: PASS
HUMAN_REQUIRED: no
FORM_SEMANTIC_CHECK: PASS
SOURCE_EVIDENCE_CHECK: PASS
COMMAND_COUNTS_CONSISTENCY_CHECK: PASS
OBSOLETE_PATH_CHECK: PASS
HELPER_SCRIPT_CHECK: PASS
BLOCKERS: none
```
