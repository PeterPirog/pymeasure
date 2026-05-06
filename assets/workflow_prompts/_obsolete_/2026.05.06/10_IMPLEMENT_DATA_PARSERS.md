# 10 — Implementacja parserów i transferów danych

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt jest dla komend zwracających tablice, bloki binarne, waveform, trace, raporty, listy plików lub złożone odpowiedzi.

Takich komend nie implementujemy jako proste `Instrument.measurement/control`, tylko jako jawne metody parsera z testami edge cases.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: implement only data-transfer/parser commands from COMMAND_COVERAGE.

Parameters:
COMMAND_IDS = <parser command IDs>

Rules:
1. Do not implement data transfers as Instrument.measurement/control if they return:
   - arrays,
   - binary blocks,
   - waveform data,
   - trace data,
   - reports,
   - complex strings,
   - file lists,
   - calibration reports.
2. Create explicit methods:
   - read_<thing>()
   - fetch_<thing>()
   - parse_<thing>()
   following repository style.
3. If data format depends on another command, document the dependency.
4. Add separate parser tests:
   - ASCII,
   - empty response,
   - malformed response,
   - binary block, if applicable.
5. Hardware tests only for query-only commands and only when no external fixture is required.
6. Do not fetch large data blocks in automatic hardware smoke tests if this can be slow.

Update COMMAND_COVERAGE:
- Parser needed = yes
- Python API
- Protocol test
- Hardware policy
- Status

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
