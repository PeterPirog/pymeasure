# 04 — Analiza service_manual.md

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt tworzy `service_coverage.md` i przenosi ryzyka z Service Manual do `command_coverage.md`.

Service Manual służy tu do bezpieczeństwa, procedur, warm-up, guard/ground, kalibracji, adjustment, sprzętu pomocniczego i decyzji, czego nie automatyzować.

Nie wolno z niego wymyślać komend SCPI.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: create SERVICE_COVERAGE and transfer service risks into COMMAND_COVERAGE. Do not implement code.

Tasks:
1. Read SERVICE_MANUAL, if it exists.
2. If SERVICE_MANUAL does not exist, create SERVICE_COVERAGE with `service manual not provided` and stop.
3. Do not extract command syntax from SERVICE_MANUAL.
4. Use SERVICE_MANUAL only for:
   - safety,
   - calibration,
   - verification,
   - adjustment,
   - internal service,
   - required equipment,
   - warm-up,
   - guard/ground,
   - output safety,
   - hazardous voltage/current/power,
   - service-only procedures,
   - risk classification.

SERVICE_COVERAGE must contain:

1. Service manual metadata

2. Safety classification:
| Area | Manual section | Operator-safe | Service-only | Hazard | Driver implication | Hardware-test implication | Notes |

3. Service procedures:
| Procedure | Manual section | Requires cover removal | Requires calibration equipment | Affects calibration | Affects NVM/logs/files | Remote command known? | Related command | Policy | Notes |

4. Service-related remote commands:
| Command | Form | Source in Programming Guide | Related service procedure | Risk level | PyMeasure policy | Hardware-test policy | Notes |

5. Do-not-automate list:
| Item | Reason | Allowed only if | Notes |

6. Safe diagnostics list:
| Item | Command | Why safe | Suggested hardware test |

7. Required equipment / fixtures:
| Function | Required equipment | Required load/fixture | Hardware-test implication | Notes |

Then update COMMAND_COVERAGE columns:
- Risk level
- Hardware-test policy
- Requires operator confirmation
- Notes

Risk levels:
- safe-query
- safe-state-readwrite
- safe-display-only
- cautious-output
- cautious-state-change
- long-running
- destructive-file
- destructive-log-clear
- destructive-memory
- calibration
- adjustment
- factory/service
- power-affecting
- network/address-affecting
- hazardous-output
- service-only
- unknown

Hardware-test policies:
- yes
- query-only
- roundtrip-safe
- output-off-only
- operator-confirmed-only
- protocol-only
- never
- skip-unless-option-present
- needs-fixture-or-load
- needs-verification

Rules:
- Calibration, adjustment, disassembly, replacement, fuse work, internal voltages, test points, cover removal -> service-only.
- Do not add new command syntax unless it appears in PROGRAMMING_GUIDE.
- Commands such as delete, format, initialize, clear log, factory reset, password, calibration save, power off, firmware update -> hardware-test policy `never` or `operator-confirmed-only`.

Run:
git diff --check
git diff --stat
```
