# 08 — Hardware smoke test z adresem VISA

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt używa sprzętu po raz pierwszy.

Ma uruchomić minimalne, bezpieczne testy z adresem VISA: identyfikacja, safe query-only i kolejka błędów. Nie wolno jeszcze włączać wyjść ani robić kalibracji, adjustment, store/delete, power-off, long self-test.

Adres VISA może być znany od początku workflow, ale używany jest dopiero tutaj.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: run a minimal safe hardware smoke test for the existing driver skeleton.

Condition:
- If DEVICE_ADDRESS is empty, do not run hardware tests. Report that hardware tests were skipped.
- If DEVICE_ADDRESS is not empty, use it only for safe-query tests.

Tasks:
1. Run protocol tests.
2. Run hardware tests with DEVICE_ADDRESS.
3. Use timeout >= 20000 ms for older GPIB/VISA unless the manual requires more.
4. Do not send:
   - output enable,
   - operate,
   - calibration,
   - adjustment,
   - save/store,
   - delete/format,
   - firmware,
   - factory,
   - power off/reboot,
   - long self-test.
5. Verify instrument identity.
6. Verify safe query-only properties.
7. Query the error queue if the driver supports it.
8. Update CODEX_WORKLOG:
   - command run,
   - output,
   - IDN response if available,
   - error queue response,
   - final safety state.

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py --device-address "<DEVICE_ADDRESS>" -q -s
git diff --check
git diff --stat

If the hardware test reveals firmware/model/option differences, do not guess. Mark COMMAND_COVERAGE as needs-verification and document the real response.
```
