# PyMeasure Driver Workflow Prompts — Programming Guide + Service Manual + optional Operators Guide

Wersja: 2026-05-06

## Cel paczki

Ta paczka zawiera spójny zestaw promptów do przeprowadzenia całego workflow tworzenia drivera PyMeasure w lokalnym repozytorium PyCharm/Codex na podstawie:

- `programming_guide.md` — jedyne źródło składni komend zdalnych,
- `service_manual.md` — źródło bezpieczeństwa, ryzyk, kalibracji, adjustment, procedur service-only,
- `operators_guide.md` — opcjonalne źródło semantyki użytkowej, nazw funkcji, złączy i bezpiecznych sekwencji pracy,
- opcjonalnie znanego adresu VISA urządzenia.

Workflow prowadzi od ekstrakcji komend, przez coverage i architekturę, aż do drivera PyMeasure, testów `expected_protocol`, testów sprzętowych i final cleanup przed PR.

## Jak używać paczki

1. W lokalnym repozytorium PyMeasure utwórz katalog:

```text
assets/<vendor>/<model>/
```

2. Włóż tam pliki:

```text
programming_guide.md
service_manual.md
operators_guide.md        # opcjonalnie
```

3. Wypełnij plik `00_PROJECT_CONTEXT_TEMPLATE.md`.

4. Na początku rozmowy z ChatGPT wklej wypełniony blok `PROJECT CONTEXT FOR CHATGPT` i napisz:

```text
Zapamiętaj ten kontekst dla bieżącego workflow. W kolejnych odpowiedziach używaj tych wartości jako domyślnych, chyba że je zmienię.
```

Jeżeli chcesz, żeby ChatGPT zapamiętał te dane także między rozmowami, użyj jawnej formuły:

```text
Zapamiętaj w pamięci: pracuję nad driverem PyMeasure dla <vendor> <model>, repozytorium jest w <repo_root>, a robocze materiały są w assets/<vendor>/<model>.
```

Nie zapisuj w pamięci haseł, tokenów ani prywatnych danych. Adres VISA można podać jako lokalny parametr workflow, ale nie musi być zapisywany długoterminowo.

5. Do Codexa w PyCharm wklejaj prompty po kolei. W każdym promptcie najpierw wklej sekcję `SOURCE DATA FOR CODEX` z wypełnionymi wartościami, a potem treść promptu.

## Zalecana kolejność

```text
00_PROJECT_CONTEXT_TEMPLATE.md  -> wypełnij raz i trzymaj jako konfigurację
01_PREFLIGHT_REPO_AND_ASSETS.md
02_EXTRACT_COMMANDS_TXT.md
03_BUILD_COMMAND_COVERAGE.md
04_ANALYZE_SERVICE_MANUAL.md
05_ANALYZE_OPERATORS_GUIDE_OPTIONAL.md
06_ARCHITECTURE_PLAN.md
07_IMPLEMENT_SKELETON_COMMON_STATUS.md
08_HARDWARE_SMOKE_TEST.md
09_IMPLEMENT_ONE_SAFE_BATCH.md      -> powtarzaj dla kolejnych subsystemów
10_IMPLEMENT_DATA_PARSERS.md
11_RISKY_COMMANDS_DECISION.md
12_SPHINX_DOCUMENTATION.md
13_COMPLETENESS_AUDIT.md
14_HARDWARE_REGRESSION.md
15_FINAL_CLEANUP_BEFORE_PR.md
```

## Najważniejsze zasady

- Składnia komend pochodzi tylko z `programming_guide.md` albo jawnego Remote Programmers Manual.
- `service_manual.md` nie tworzy komend; służy do klasyfikacji ryzyka i polityki testów sprzętowych.
- `operators_guide.md` nie tworzy komend; służy do semantyki użytkowej i bezpiecznych sekwencji.
- Dla SCPI używaj `SCPIMixin, Instrument`, nie `includeSCPI=True`.
- Nie twórz `get_*` ani `set_*`.
- Każda zaimplementowana komenda ma mieć test `expected_protocol`.
- Testy sprzętowe muszą być pomijane bez adresu VISA.
- Komendy destrukcyjne, kalibracyjne, adjustment, format/delete/store/power-off/firmware/factory/long self-test nie są uruchamiane automatycznie na sprzęcie.
- Po testach sprzętowych przyrząd ma zostać w stanie bezpiecznym: output/source off lub standby, jeśli dotyczy, oraz odpytana kolejka błędów, jeśli dostępna.

## Co po każdym promptcie wkleić do Chata/Architekta

```text
git diff --stat
git diff --check
wynik pytest
fragment command_coverage.md dla zmienionej paczki
fragment codex_worklog.md z odpowiedziami urządzenia, jeśli był hardware test
```

## Pliki, które nie powinny wejść do finalnego PR

```text
AGENTS.md
assets/
manual PDFs
local logs
codex_worklog.md
command_coverage.md
service_coverage.md
operator_coverage.md
architecture_plan.md
```

Do PR powinny wejść tylko właściwe pliki PyMeasure:

```text
pymeasure/instruments/<vendor>/<model_lower>.py
pymeasure/instruments/<vendor>/__init__.py
tests/instruments/<vendor>/test_<model_lower>.py
tests/instruments/<vendor>/test_<model_lower>_with_device.py
docs/api/instruments/<vendor>/<model_lower>.rst
docs/api/instruments/<vendor>/index.rst
```
