# Keysight35670A Hardware Validation Plan (Safe-First)

Branch: `dev/keysight-35670A`  
Target device: `GPIB0::14::INSTR`  
Scope: plan for safe `with_device` validation first; risky operations are **not** run by default.

## Policy summary

- `run-safe`: 25 API entries
- `protocol-only`: 10 API entries
- `manual-opt-in`: 8 API entries
- `skip-with-reason`: 4 API entries (option-gated)

## Excluded risky commands (default with_device run)

These commands stay `protocol-only` or `manual-opt-in` and are not executed by default hardware tests:

- `*CAL?`
- `CALibration:ALL?`
- `TEST:LONG`
- `TEST:LOG:CLEar`
- `SYSTem:FLOG:CLEar`
- `SYSTem:POWer:STATe`
- `MEMory:DELete*`
- `MMEMory:DELete`
- `MMEMory:INITialize`
- `MMEMory:LOAD*`
- `MMEMory:STORe*`
- `PROGram:DELete*`
- `HCOPy:IMMediate`
- `CALCulate:CFIT:IMMediate`
- `CALCulate:SYNThesis:IMMediate`
- `SENSe:TCAPture:DELete`
- `SENSe:TCAPture:MALLocate`
- `SENSe:TCAPture:IMMediate`

## Preconditions for all safe hardware tests

1. Open instrument with `timeout >= 20000`.
2. Force `source_output_enabled = False` at setup and teardown.
3. Drain error queue at setup.
4. After each state-changing test: restore original value and check `SYSTem:ERRor?` queue is empty.
5. Keep risky operations excluded from default `with_device` run.

## Risk matrix

| Subsystem | Command/API | Risk class | Hardware test policy | State restore needed | Error queue check needed | Notes |
|---|---|---|---|---|---|---|
| Common | `id` (`*IDN?`) | read-only | run-safe | no | no | Verify contains `35670A`; call `check_id()`. |
| Common | `options()` (`*OPT?`) | read-only | run-safe | no | no | Parse options string for feature gating (AY6 / 1D0 / 1D1 / 1D2). |
| System | `system_version` (`SYSTem:VERSion?`) | read-only | run-safe | no | no | Query-only smoke test. |
| System | `power_source` (`SYSTem:POWer:SOURce?`) | read-only | run-safe | no | no | Query-only smoke test. |
| System | `system_error()` (`SYSTem:ERRor?`) | read-only | run-safe | no | no | Accept `0,No error` variants. |
| Common | `status_byte` (`*STB?`) | read-only | run-safe | no | no | Query-only smoke test. |
| Status | `operation_condition` | read-only | run-safe | no | no | Query-only smoke test. |
| Status | `questionable_condition` | read-only | run-safe | no | no | Query-only smoke test. |
| Status | `device_condition` | read-only | run-safe | no | no | Query-only smoke test. |
| Memory | `mass_memory_filesystem` (`MMEMory:FSYStem?`) | read-only | run-safe | no | no | Query-only; no file mutation. |
| Memory | `memory_catalog()` (`MEMory:CATalog?`) | read-only | run-safe | no | no | Query-only; avoid `ALL?` if latency becomes high. |
| Memory | `memory_free()` (`MEMory:FREE?`) | read-only | run-safe | no | no | Query-only; no allocation changes. |
| Format | `data_format` getter (`FORMat:DATA?`) | read-only | run-safe | no | no | Getter only in this row. |
| Instrument | `selected_instrument_number` getter (`INSTrument:NSELect?`) | read-only | run-safe | no | no | Query-only smoke test. |
| Instrument | `instrument_mode` getter (`INSTrument:SELect?`) | read-only | run-safe | no | no | Query-only smoke test. |
| Trigger | `tachometer_rpm` getter (`TRIGger:TACHometer:RPM?`) | read-only | run-safe | no | no | Accept no-signal outcomes (`0`, near-zero, or instrument-specific NaN-like reply). |
| Output | `source_output_enabled` (`OUTPut:STATe`) | output-affecting | run-safe | yes | yes | Roundtrip allowed; always end with `False`. |
| Source | `source_function` (`SOURce:FUNCtion:SHAPe`) | output-affecting | run-safe | yes | yes | Read initial state, set safe value, restore. |
| Source | `source_frequency` (`SOURce:FREQuency:FIXed`) | output-affecting | run-safe | yes | yes | Read initial state, set safe value, restore. |
| Source | `source_voltage_offset` (`SOURce:VOLTage:LEVel:IMMediate:OFFSet`) | output-affecting | run-safe | yes | yes | Execute only with output off; restore original offset. |
| Input CH1 | `ch1.coupling` (`INPut1:COUPling`) | safe-roundtrip-restore | run-safe | yes | yes | Toggle AC/DC and restore original. |
| Input CH1 | `ch1.autorange_enabled` (`INPut1:RANGe:AUTO`) | safe-roundtrip-restore | run-safe | yes | yes | Toggle and restore original. |
| Display | `display_enabled` (`DISPlay:ENABle`) | safe-roundtrip-restore | run-safe | yes | yes | Restore original (or `True` if policy requires visible display). |
| System | `beeper_enabled` (`SYSTem:BEEPer:STATe`) | safe-roundtrip-restore | run-safe | yes | yes | Toggle and restore original. |
| Format | `data_format` setter/getter (`FORMat:DATA`) | safe-roundtrip-restore | run-safe | yes | yes | Set temporary value, restore original format. |
| Option gating | CH3/CH4 APIs (`INPut3/4`, `CALCulate3/4`, etc.) | option-dependent | skip-with-reason | yes | yes | Run only when `*OPT?` indicates AY6 (4-channel). Otherwise `pytest.skip("Option AY6 not installed")`. |
| Option gating | Order-analysis APIs (`INST:SEL ORD`, `SENSe:ORDer:*`) | option-dependent | skip-with-reason | yes | yes | Run only when order option token is present. Restore mode afterwards. |
| Option gating | Octave-analysis APIs (`INST:SEL OCT`, octave-only controls) | option-dependent | skip-with-reason | yes | yes | Run only when octave option token is present. Restore mode afterwards. |
| Option gating | Swept-sine APIs (`INST:SEL SINE`, swept-sine controls) | option-dependent | skip-with-reason | yes | yes | Run only when swept-sine option token is present. Restore mode afterwards. |
| Calibration | `*CAL?` (`run_self_calibration`) | calibration | manual-opt-in | no | yes | Long-running calibration; require explicit operator opt-in. Keep protocol tests as baseline. |
| Calibration | `CALibration:ALL?` (`run_calibration`) | calibration | manual-opt-in | no | yes | Long-running full calibration; explicit opt-in only. |
| Test | `TEST:LONG` | long-running | manual-opt-in | no | yes | Long confidence test; not in default hardware suite. |
| Test | `TEST:LOG:CLEar` | destructive | protocol-only | no | no | Keep `expected_protocol` + confirmation guard coverage only. |
| System | `SYSTem:FLOG:CLEar` | destructive | protocol-only | no | no | Keep protocol-only; do not clear live fault log by default. |
| System | `SYSTem:POWer:STATe` | power/control-risk | protocol-only | no | no | Never run in automated hardware suite; shutdown risk. |
| Memory | `MEMory:DELete*` | destructive | protocol-only | no | no | Keep protocol-only; mutates volatile allocations. |
| Mass memory | `MMEMory:DELete` | file-system-destructive | protocol-only | no | no | Deletes files/directories; no default hardware execution. |
| Mass memory | `MMEMory:INITialize` | file-system-destructive | protocol-only | no | no | Disk format operation; protocol-only. |
| Mass memory | `MMEMory:LOAD*` | active-controller-required | protocol-only | no | no | External file dependency and state mutation; protocol-only. |
| Mass memory | `MMEMory:STORe*` | active-controller-required | protocol-only | no | no | Writes files; protocol-only. |
| Program | `PROGram:DELete*` | destructive | protocol-only | no | no | Deletes Instrument BASIC programs; protocol-only. |
| Hardcopy | `HCOPy:IMMediate` | active-controller-required | manual-opt-in | no | yes | Side-effectful output routing; run only with explicit operator intent. |
| Curve fit | `CALCulate:CFIT:IMMediate` | long-running | manual-opt-in | no | yes | Currently exposed without `confirmed` guard; keep out of default hardware run. |
| Synthesis | `CALCulate:SYNThesis:IMMediate` | long-running | manual-opt-in | no | yes | Currently exposed without `confirmed` guard; keep out of default hardware run. |
| Time capture | `SENSe:TCAPture:DELete` | destructive | protocol-only | no | no | Keep protocol-only in default suite. |
| Time capture | `SENSe:TCAPture:MALLocate` | active-controller-required | manual-opt-in | no | yes | Currently exposed without `confirmed` guard; explicit opt-in only. |
| Time capture | `SENSe:TCAPture:IMMediate` | active-controller-required | manual-opt-in | no | yes | Starts acquisition; currently no `confirmed` guard. |

## Planned execution order (safe-only now)

1. Run existing safe `with_device` tests only.
2. Add/adjust safe roundtrip tests with explicit restore and queue checks where missing.
3. Add option-gated tests with `pytest.skip` reasons for missing options.
4. Keep risky APIs out of default hardware execution (`protocol-only` or `manual-opt-in`).

## Ambiguities detected (no test edits yet)

1. Option-token mapping needs one canonical parser rule (`AY6` vs legacy strings like `A6J`, and mode options `1D0/1D1/1D2`).
2. Some APIs in risky list are currently missing a `confirmed=True` guard in driver (`run_curve_fit`, `run_synthesis`, `start_time_capture`, `allocate_time_capture_memory`).
