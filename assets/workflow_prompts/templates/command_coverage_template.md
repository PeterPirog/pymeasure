# Command coverage template

Instrument: `<vendor> <model>`  
Branch: `dev/<vendor>-<model>`  
Manual source: `<manual title / file>`  
Operator: `<name or initials>`  
Last updated: `<YYYY-MM-DD>`

## Status legend

| Status | Meaning |
|---|---|
| `todo` | Not yet implemented |
| `implemented` | Driver API exists |
| `protocol-tested` | `expected_protocol` test exists |
| `hardware-tested` | Safe test passed on physical device |
| `unsafe` | Not suitable for normal hardware tests |
| `deferred` | Intentionally postponed |
| `not-implemented` | Intentionally not implemented |
| `needs-verification` | Manual/OCR/firmware ambiguity |

## Command coverage table

| Subsystem | Manual section | Command | Form | Python API | Type | Validator / mapping | Protocol test | Hardware test | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Common | 3 | `*IDN?` | query only | `id` / `check_id()` | SCPIMixin | n/a | yes | yes | protocol-tested | Accept vendor variants |
| Common | 3 | `*CLS` | command only | `clear()` | SCPIMixin/method | n/a | yes | safe | todo | Clear status before controlled sequences |
| Common | 3 | `*RST` | command only | `reset()` | SCPIMixin/method | n/a | yes | cautious | todo | Avoid in broad hardware tests |
| System | 21 | `SYSTem:ERRor?` | query only | `system_error()` or `next_error` | measurement/method | parse string | yes | yes | todo | Read error queue after hardware configuration |
| Input | 12 | `INPut[1|2|3|4]:COUPling` | command/query | `ch<n>.coupling` | control | `AC`, `DC` | yes | yes | todo | Indexed channel |
| Input | 12 | `INPut[1|2|3|4]:BIAS[:STATe]` | command/query | `ch<n>.bias_enabled` | control | bool map | yes | cautious | todo | ICP/bias supply; turn off if changed |
| Source | 19 | `SOURce:FREQuency:FIXed` | command/query | `source_frequency` | control | manual range | yes | yes | todo | Roundtrip safe with output off |
| Source | 19 | `SOURce:FUNCtion[:SHAPe]` | command/query | `source_function` | control | map values | yes | yes | todo | Use semantic names |
| Output | 16 | `OUTPut[:STATe]` | command/query | `source_output_enabled` | control | bool map | yes | yes | todo | Always end hardware tests with False |
| Trigger | 24 | `TRIGger:SOURce` | command/query | `trigger_source` | control | discrete set | yes | cautious | todo | Avoid external trigger dependencies |
| Calculate | 6 | `CALCulate[1|2|3|4]:DATA?` | query only | `trace<n>.read_data()` | method/parser | ASCII/binary parser | yes | cautious | todo | Validate data format |
| Calculate | 6 | `CALCulate[1|2|3|4]:X:DATA?` | query only | `trace<n>.read_x_data()` | method/parser | ASCII/binary parser | yes | cautious | todo | X-axis data |
| Memory | 15 | `MMEMory:INITialize` | command only | not implemented or explicit method | unsafe | n/a | no | no | unsafe | Formats disk |
| Memory | 15 | `MMEMory:DELete` | command only | not implemented or explicit method | unsafe | n/a | no | no | unsafe | Deletes files |
| Test | 22 | `TEST:LONG` | command only | explicit method only | unsafe/duration | n/a | protocol only | no | unsafe | Long self-test |
| Calibration | 7 | `CALibration[:ALL]?` | query only | explicit method only | unsafe | n/a | protocol only | no | unsafe | Calibration changes/time |

## Implementation batches

| Batch | Subsystems | Planned commands | Done | Protocol tests | Hardware tests | Notes |
|---|---|---:|---:|---:|---:|---|
| 1 | Skeleton/Common/System | 0 | 0 | 0 | 0 | |
| 2 | Input channels | 0 | 0 | 0 | 0 | |
| 3 | Source/Output | 0 | 0 | 0 | 0 | |
| 4 | Trigger/Arm/Initiate | 0 | 0 | 0 | 0 | |
| 5 | Sense/Frequency/Average/Sweep | 0 | 0 | 0 | 0 | |
| 6 | Calculate/Trace/Data | 0 | 0 | 0 | 0 | |
| 7 | Display/Marker/Units | 0 | 0 | 0 | 0 | |
| 8 | Memory/MMEM/Program/Test | 0 | 0 | 0 | 0 | |
| 9 | Docs/final cleanup | 0 | 0 | 0 | 0 | |

## Final review checklist

- [ ] Driver file exists.
- [ ] Class exported in vendor `__init__.py`.
- [ ] RST documentation exists.
- [ ] Vendor `index.rst` updated.
- [ ] Protocol tests pass.
- [ ] Safe hardware tests pass or are documented as skipped.
- [ ] `git diff --check` is clean.
- [ ] No `assets/` files in final PR diff.
- [ ] No `AGENTS.md` in final PR diff.
- [ ] No getters/setters.
- [ ] No `includeSCPI=True`.
- [ ] Destructive commands are not run in hardware tests.
- [ ] Source/output is left disabled after hardware tests.
