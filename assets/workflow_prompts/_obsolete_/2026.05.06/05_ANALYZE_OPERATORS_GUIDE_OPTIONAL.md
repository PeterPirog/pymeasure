# 05 — Analiza operators_guide.md opcjonalnie

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt jest opcjonalny. Użyj go, jeśli masz `operators_guide.md`.

Operators Guide pomaga nazwać funkcje po ludzku, zrozumieć złącza, tryby pracy, bezpieczny stan końcowy i zależności opcji/modeli. Nie jest źródłem składni komend zdalnych, chyba że zawiera jawny remote command reference.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: analyze OPERATORS_GUIDE and create OPERATOR_COVERAGE. Do not implement code.

Tasks:
1. If OPERATORS_GUIDE does not exist, create a short OPERATOR_COVERAGE stating `operators guide not provided` and stop.
2. If it exists, use it for:
   - user-facing function names,
   - front-panel terminology,
   - safe operating sequence,
   - safe standby/output-off sequence,
   - model/option dependencies,
   - connector names,
   - user-level warnings,
   - normal operating modes.
3. Do not extract remote command syntax from OPERATORS_GUIDE unless it is explicitly a remote command reference. Otherwise treat it as a semantic and safety source only.

OPERATOR_COVERAGE must contain:

1. Operator manual metadata

2. User-facing function map:
| User function | Front-panel term | Remote command candidate | Programming guide confirmation | PyMeasure API implication | Notes |

3. Connector and output safety:
| Connector/output | Function | Hazard | Safe final state | Hardware-test implication | Notes |

4. Normal operation sequences:
| Sequence | Steps | Remote automation candidate | Risk | Notes |

5. Model/option dependencies:
| Feature | Models/options | Driver implication | Hardware-test implication | Notes |

Update COMMAND_COVERAGE only in:
- Proposed Python API
- Notes
- Hardware-test policy
- Requires operator confirmation

Do not implement code.

Run:
git diff --check
git diff --stat
```
