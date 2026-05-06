# Keysight35670A Test Coverage Audit

Branch: `dev/keysight-35670A`  
Driver: `pymeasure/instruments/keysight/keysight35670A.py`  
Protocol tests: `tests/instruments/keysight/test_keysight35670A.py`  
Hardware tests: `tests/instruments/keysight/test_keysight35670A_with_device.py`

## Audit checklist

| Area | Audit result |
|---|---|
| loops (`for`) | Covered broadly in protocol tests; complex unreferenced helpers listed below. |
| if/else branches | Covered broadly in protocol tests; complex unreferenced helpers listed below. |
| except branches | 4 methods contain `except`; 3 are directly referenced by tests, `_raise_if_errors` is covered indirectly through `drain_errors` tests. |
| early return | Present in many parser/normalizer helpers; major paths covered via parser tests and protocol method tests. |
| raw=True/raw=False | 25 methods expose `raw=`; all referenced in tests except `_encode_program_block` helper (indirect path). |
| confirmed=True/False | 49 `confirmed=False` methods in driver; all 49 referenced by protocol tests (`requires confirmation` and `confirmed=True`). |
| parser coverage | Core parser/serializer helpers covered (`_parse_*`, `_format_limit_segment_data`, `_coerce_bytes`, `_encode_definite_block`, `_parse_definite_block`). |
| dynamic `{ch}` commands | 298 channelized command templates in driver; channel APIs are exercised extensively in protocol tests (`inst.ch*`, `inst.trace*`, `inst.display*`, `inst.sense_window*`, `inst.order_track*`). |
| `"0"`/`"1"` bool handling risk | No `BOOL_VALUES + map_values=True` definitions without `cast=int`; protocol file has extensive bool-mapping tests (51). |

## Key coverage metrics

- Protocol tests currently passing: `653`.
- Hardware safe suite: `10` tests, skipped without address, passing with device.
- `confirmed` methods in driver: `49`.
- `confirmed` methods without protocol reference: `0`.
- Methods with `raw=` parameter: `25`.
- `raw=` methods without protocol reference: `1` (`_encode_program_block`, helper-level indirect coverage).
- Methods containing `except`: `4`.

## Complex helper/method gaps (direct-name reference)

These functions are not directly referenced by name in protocol tests and are candidates for additional focused unit coverage:

1. `_encode_program_block`
2. `_normalize_mass_memory_program_format`
3. `_normalize_mass_memory_trace_selector`
4. `_parse_ascii_or_definite_block_text`
5. `_trace_data_register_selector`
6. `_trace_waterfall_register_selector`
7. `_raise_if_errors` (covered indirectly by `drain_errors` tests)

`__init__` was excluded from this gap list due to constructor nature and broad runtime coverage through many tests.

## Expected protocol audit

After adding protocol tests for `clear()` (`*CLS`) and `reset()` (`*RST`):

- API without expected_protocol in command coverage matrix: `0`.
- Risky operations remain protocol-only/manual and are not auto-run in hardware suite.
