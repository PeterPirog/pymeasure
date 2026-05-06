# Gdzie umieścić pliki z paczki PyMeasure_Assistant

## 1. Pliki dla projektu ChatGPT

### `new_system_prompt.md`

Użyj jako głównego promptu systemowego / instrukcji projektu `PyMeasure_Assistant`.

Nie wkładaj tego pliku do repozytorium PyMeasure.

### `prompt_architekt_pymeasure_improved.md`

Dodaj jako plik wiedzy projektu `PyMeasure_Assistant`.

Nie wkładaj tego pliku do finalnego pull requestu PyMeasure.

## 2. Pliki dla lokalnego repozytorium PyMeasure w PyCharm

### `AGENTS.md`

Skopiuj do katalogu głównego lokalnego repozytorium:

```text
C:\Users\Ila\PycharmProjects\pymeasure\AGENTS.md
```

Ten plik ma być czytany przez Codexa.

Nie dodawaj go do finalnego PR, chyba że maintainerzy PyMeasure wyraźnie tego chcą.

### `command_coverage_template.md`

Skopiuj jako:

```text
assets/<vendor>/<model>/command_coverage.md
```

Przykład:

```text
assets/keysight/35670A/command_coverage.md
```

Codex powinien aktualizować ten plik po każdej paczce implementacji.

### `codex_worklog_template.md`

Skopiuj jako:

```text
assets/<vendor>/<model>/codex_worklog.md
```

Wklejaj tam prompty do Codexa i wyniki testów.

## 3. Zalecane lokalne wykluczenia z Git

W lokalnym repozytorium PyMeasure uruchom:

```powershell
Add-Content .git\info\exclude "`nAGENTS.md`nAgents.md`nassets/`n"
```

To wyklucza pliki tylko lokalnie i nie zmienia `.gitignore`.

## 4. Minimalna struktura robocza

```text
pymeasure/
├── AGENTS.md
├── assets/
│   └── <vendor>/
│       └── <model>/
│           ├── programming_guide.md
│           ├── operation_manual.md
│           ├── commands.txt
│           ├── command_coverage.md
│           └── codex_worklog.md
├── pymeasure/
│   └── instruments/
│       └── <vendor>/
│           ├── __init__.py
│           └── <model>.py
├── tests/
│   └── instruments/
│       └── <vendor>/
│           ├── test_<model>.py
│           └── test_<model>_with_device.py
└── docs/
    └── api/
        └── instruments/
            └── <vendor>/
                ├── index.rst
                └── <model>.rst
```

## 5. Najkrótszy cykl pracy

1. Architekt analizuje manuale.
2. Architekt przygotowuje mały prompt dla Codexa.
3. Codex implementuje jedną paczkę komend.
4. Codex uruchamia testy bez sprzętu.
5. Operator uruchamia testy z urządzeniem.
6. Operator wkleja wyniki do architekta.
7. Architekt koryguje następny prompt.
8. Po pełnym coverage następuje final cleanup i przygotowanie PR.

## 6. Co nie powinno trafić do PR

```text
AGENTS.md
assets/
manual PDFs
local logs
temporary scripts
worklog files
command coverage files
```

Do PR mają trafić tylko właściwe pliki PyMeasure:

```text
pymeasure/instruments/<vendor>/<model>.py
pymeasure/instruments/<vendor>/__init__.py
tests/instruments/<vendor>/test_<model>.py
tests/instruments/<vendor>/test_<model>_with_device.py
docs/api/instruments/<vendor>/<model>.rst
docs/api/instruments/<vendor>/index.rst
```
