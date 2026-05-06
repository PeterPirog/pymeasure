# 03 — Utworzenie command_coverage.md

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt przekształca `commands.txt` w roboczy arkusz `command_coverage.md`.

Każda komenda dostaje wiersz z decyzją: forma komendy, transport, kandydat API PyMeasure, ryzyko, polityka testów i status.

Jeszcze nie implementuje kodu.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: create COMMAND_COVERAGE from COMMANDS_TXT and PROGRAMMING_GUIDE. Do not implement code.

Tasks:
1. Read COMMANDS_TXT.
2. For every command, create one row in COMMAND_COVERAGE.
3. If COMMANDS_TXT marks a command as `needs-verification`, preserve that status.
4. Fill details from PROGRAMMING_GUIDE only when explicitly available.

COMMAND_COVERAGE must contain:

1. Metadata:
   - vendor
   - model
   - class name
   - instrument type
   - interface/protocol
   - programming guide path
   - service manual path
   - operators guide path
   - VISA address known: yes/no
   - extraction status

2. Status legend:
   - todo
   - implemented
   - protocol-tested
   - hardware-tested
   - unsafe
   - deferred
   - not-implemented
   - needs-verification
   - needs-operator-decision

3. Command coverage table:
| ID | Subsystem | Manual section | Command | Canonical syntax | Form | SCPI/common/custom | Transport | Parameters | Return format | PyMeasure API decision | Proposed Python API | Validator / mapping | Parser needed | Risk level | Hardware-test policy | Protocol test | Hardware test | Status | Notes |

Initial decisions:
- command/query representing state -> candidate: Instrument.control
- query-only simple value -> candidate: Instrument.measurement
- query-only multi-point/block data -> candidate: method/parser
- command-only action -> candidate: method
- command-only setting without query -> candidate: Instrument.setting, if not an action
- destructive/service/calibration/power/factory -> candidate: not-implemented or explicit method

Do not invent:
- ranges,
- validators,
- value mappings,
- Python API names if not obvious.

4. Implementation batches:
   - Skeleton/Common/Status
   - System/Error/Options
   - Input/Channel
   - Output/Source
   - Trigger/Arm/Initiate
   - Sense/Measure/Acquire
   - Calculate/Trace/Data transfer
   - Display/Marker/Window
   - Memory/MMEM/File/Program
   - Calibration/Test/Service
   - Documentation/final cleanup

Run:
git diff --check
git diff --stat

Report:
- total commands,
- command only,
- query only,
- command/query,
- parser candidates,
- risky/unsafe,
- needs-verification.
```
