# 12 — Dokumentacja Sphinx i przykłady bezpiecznego użycia

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt uzupełnia dokumentację Sphinx dla drivera.

Dokumentacja ma pokazywać bezpieczne użycie, ostrzegać przed ryzykownymi komendami i nie wciągać lokalnych plików `assets/` ani manuali PDF do PR.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: complete Sphinx documentation for the driver.

Modify:
- DOC_FILE
- DOC_INDEX
- DRIVER_FILE only if docstrings require correction
- COMMAND_COVERAGE only for documentation status

Documentation must include:
1. Short instrument description.
2. Supported interfaces.
3. Safe output/final-state warning.
4. Connection example.
5. Safe query example.
6. Safe parameter-setting example with output disabled, if applicable.
7. Risky/service-related commands section, if such methods exist.
8. Statement that destructive/calibration/service commands are not run in automatic hardware tests.
9. Autodoc class entry following repository style.

Do not add:
- manual PDFs,
- assets,
- local workflow notes,
- worklogs.

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
