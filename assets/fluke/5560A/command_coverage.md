# Command Coverage – Fluke 5560A

## Status Legend

| Status | Meaning |
|--------|---------|
| `todo` | Command not yet addressed |
| `protocol` | Protocol test written with `expected_protocol` |
| `device` | Device test written (requires hardware) |
| `implemented` | Property added to driver |
| `excluded` | Command intentionally excluded (e.g., unsafe, local-only) |

## Hardware-Test Policy

| Test Type | When to Run | Requires Hardware |
|-----------|-------------|-------------------|
| Protocol tests (`_test.py`) | Always run before commit | NO (mocked with `expected_protocol`) |
| Device tests (`_with_device.py`) | Only when hardware available | YES |

## Implementation Batches

| Batch | Scope | Goal |
|-------|-------|------|
| 1 | Core identity & basic status | `*IDN?`, `*RST`, `*STB?`, `status`, `error_queue` |
| 2 | Power & output control | Output enable, range selection |
| 3 | Function configuration | Voltage, current, resistance, etc. |
| 4 | Advanced features | ramps, sweeps, triggers, channels (if applicable) |
| 5 | Safety & compliance | Over-temperature, fault handling |

## Command Coverage Table

| SCPI Command | Category | Status | Batch | Notes |
|--------------|----------|--------|-------|-------|
| `*IDN?` | Identity | todo | 1 | Vendor, model, serial, firmware |
| `*RST` | Control | todo | 1 | Reset instrument |
| `*STB?` | Status | todo | 1 | Status byte |
| `*ESE?` / `*ESE` | Event | todo | 1 | Event register enable |
| `*ESR?` | Status | todo | 1 | Event register status |
| `*OPC?` | Synchronization | todo | 1 | Operation complete query |
| `*TST?` | Self-test | todo | 1 | Self-test result |
| `*SRE?` / `*SRE` | Status | todo | 1 | Service request enable |
| `*CLS` | Control | todo | 1 | Clear status |
| `OUTPUT:STATE?` | Output | todo | 2 | Output state query |
| `OUTPUT:STATE` | Output | todo | 2 | Output enable/disable |
| `FUNCTION?` | Function | todo | 3 | Current function query |
| `FUNCTION` | Function | todo | 3 | Set function (VOLT, CURR, RES, etc.) |
| `RANGE?` | Range | todo | 2 | Range query |
| `RANGE` | Range | todo | 2 | Set range |
| `LEVEL?` | Level | todo | 3 | Level (voltage/current/resistance) query |
| `LEVEL` | Level | todo | 3 | Set level |
| `SOURCE:DC:VOLTAGE?` | Source | todo | 3 | DC voltage query |
| `SOURCE:DC:VOLTAGE` | Source | todo | 3 | Set DC voltage |
| `SOURCE:DC:CURRENT?` | Source | todo | 3 | DC current query |
| `SOURCE:DC:CURRENT` | Source | todo | 3 | Set DC current |
| `SENSE:RESISTANCE?` | Sense | todo | 3 | Resistance measurement |
| `MEASURE:VOLTAGE?` | Measure | todo | 3 | Voltage measurement |
| `MEASURE:CURRENT?` | Measure | todo | 3 | Current measurement |
| `TRIGGER:IMMEDIATE` | Trigger | todo | 4 | Immediate trigger |
| `READ?` | Measure | todo | 4 | Synchronized read |
| `SYSTEM:AUTOZERO:STATE?` | Advanced | todo | 5 | Auto-zero state |
| `SYSTEM:AUTOZERO:STATE` | Advanced | todo | 5 | Set auto-zero |
| `SYSTEM:TEMPERATURE?` | Safety | todo | 5 | Internal temperature |
| `SYSTEM:FAULT?` | Safety | todo | 5 | Fault condition |

## Implementation Batches – Planned Order

| Batch | Commands to Implement | Testing Approach |
|-------|----------------------|------------------|
| 1 | `*IDN?`, `*RST`, `*CLS`, `*STB?`, `*ESR?` | Protocol-only; verify strings |
| 2 | `OUTPUT:STATE`, `RANGE` | Protocol + simple device test |
| 3 | `FUNCTION`, `LEVEL`, `SOURCE:DC:*` | Protocol + device test |
| 4 | `READ?`, `TRIGGER` | Protocol test; device test if timing critical |
| 5 | `SYSTEM:AUTOZERO`, `SYSTEM:TEMPERATURE`, `SYSTEM:FAULT` | Device-only (read-only safety) |

## Final PR Checklist

Before submitting the driver upstream:

- [ ] All `todo` commands mapped to properties or excluded with justification
- [ ] Protocol tests pass with `pytest` (no hardware)
- [ ] Device tests run successfully on local instrument (if available)
- [ ] Docstrings follow PEP257 (imperative summary + period)
- [ ] All properties use `control`, `measurement`, or `setting` creators
- [ ] No public `get_*` or `set_*` methods
- [ ] Validators applied only where ranges/sets are confirmed in manual
- [ ] Line length ≤ 100 characters
- [ ] No comments explaining obvious code; only non-obvious rationale
- [ ] `git diff --check` shows no whitespace errors
- [ ] No `assets/`, `AGENTS.md`, or local logs in the final PR
- [ ] Manual PDFs or local logs not committed

---

*Worklog entries linked from `codex_worklog.md`*
