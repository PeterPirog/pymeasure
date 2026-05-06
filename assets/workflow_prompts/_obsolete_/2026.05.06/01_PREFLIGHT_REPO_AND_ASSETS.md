# 01 — Preflight repozytorium i materiałów

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt uruchamiasz jako pierwszy w PyCharm/Codex.

Sprawdza, czy Codex pracuje w katalogu głównym repozytorium PyMeasure, czy istnieją wymagane manuale i czy katalog `assets/<vendor>/<model>/` jest gotowy.

Nie tworzy drivera, nie dotyka sprzętu i nie modyfikuje plików PyMeasure poza lokalnym `codex_worklog.md`.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: verify the local PyMeasure repository and prepare the working asset directory. Do not implement a driver.

Tasks:
1. Confirm that the current working directory is the PyMeasure repository root.
2. Confirm whether these files exist:
   - PROGRAMMING_GUIDE
   - SERVICE_MANUAL, if provided
   - OPERATORS_GUIDE, if provided
3. If PROGRAMMING_GUIDE does not exist, stop and report the missing path.
4. Create ASSET_DIR if it does not exist.
5. Create CODEX_WORKLOG if it does not exist.
6. Append a new session to CODEX_WORKLOG with:
   - date/time,
   - vendor,
   - model,
   - class name,
   - instrument type,
   - whether DEVICE_ADDRESS is present,
   - list of source files found.
7. Do not use VISA.
8. Do not communicate with real hardware.
9. Do not modify pymeasure/instruments, tests, or docs.

Run:
git status --short
git diff --check
git diff --stat

Report:
- which input files exist,
- which optional files are missing,
- whether the workflow can continue to Prompt 02.
```
