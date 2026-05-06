# 06 — Plan architektury drivera

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt tworzy `architecture_plan.md`.

Codex ma przejrzeć coverage, manuale i styl istniejących driverów w repozytorium, a następnie zaproponować architekturę klas: jedna klasa, kanały, trace/window, source/output helper itd.

Nadal bez implementacji kodu.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: create ARCHITECTURE_PLAN from coverage files and existing repository style. Do not implement code.

Tasks:
1. Read:
   - COMMAND_COVERAGE
   - SERVICE_COVERAGE
   - OPERATOR_COVERAGE, if present
   - PROGRAMMING_GUIDE
2. Inspect existing directories:
   - pymeasure/instruments/<VENDOR>/
   - tests/instruments/<VENDOR>/
3. Propose an architecture consistent with PyMeasure style.

ARCHITECTURE_PLAN must contain:

1. Instrument classification:
   - instrument type
   - supported interfaces
   - SCPI/IEEE-488.2/custom status
   - required mixins
   - connection defaults
   - timeout/terminators

2. Class architecture:
Choose one or more:
   - single Instrument class
   - Instrument + Channel
   - Instrument + Source/Output helper
   - Instrument + Trace
   - Instrument + Window
   - ChannelCreator / MultiChannelCreator
   - subsystem classes only if justified by existing PyMeasure style

3. Inheritance:
   - if SCPI/common commands confirmed: class <CLASS_NAME>(SCPIMixin, Instrument)
   - never includeSCPI=True

4. API mapping:
   - command/query -> Instrument.control
   - query-only -> Instrument.measurement or read method
   - command-only -> method
   - setting-only -> Instrument.setting
   - data transfer -> parser method
   - unsafe/service -> explicit method or not implemented

5. Implementation batches:
| Batch | Name | Command IDs | Subsystems | Risk | Protocol tests | Hardware tests | Dependencies | Notes |

6. Minimal first PR scope:
   - common/status/system,
   - safe output-off configuration,
   - safe query-only diagnostics,
   - no destructive/service/calibration commands unless protocol-only.

7. Unsafe/deferred list.

8. Required files for PR.

Do not implement code.

Run:
git diff --check
git diff --stat
```
