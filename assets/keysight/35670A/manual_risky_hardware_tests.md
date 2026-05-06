# Keysight35670A Manual Risky Hardware Tests (Local Only)

Branch: `dev/keysight-35670A`  
Device (manual): `GPIB0::14::INSTR`

## Scope

Ten plik opisuje **manualne** testy operacji ryzykownych.  
Nie są to testy do uruchamiania automatycznego.

## Hard guard before any risky action

Operator uruchamia operacje ryzykowne tylko gdy jednocześnie:

1. podano `--device-address "<VISA_ADDRESS>"`, oraz
2. ustawiono zmienną środowiskową  
   `PYMEASURE_35670A_ALLOW_RISKY=I_UNDERSTAND`.

Bez obu warunków test/manual workflow ma być przerwany (`skip` / abort).

## Minimal safe fixture for manual runs

1. Dedykowane stanowisko laboratoryjne (nie produkcyjne).
2. Dedykowany nośnik/dysk testowy (nie używać nośników z danymi użytkownika).
3. Zrzut stanu przed testem: `*IDN?`, `*OPT?`, `SYSTem:VERSion?`, `SYSTem:ERRor?`.
4. `timeout >= 20000`.
5. `source_output_enabled = False` przed i po każdej operacji.
6. Opróżnienie kolejki błędów przed i po każdej operacji.
7. Zamknięcie adaptera/połączenia na końcu sesji.

## Manual operator confirmation template

Przed każdą operacją operator potwierdza ręcznie (np. wpis do logu):

- "Rozumiem skutki komendy `<COMMAND>`."
- "Używam środowiska testowego i nośnika testowego."
- "Posiadam kopię danych i akceptuję możliwość utraty danych."
- "Zmienna `PYMEASURE_35670A_ALLOW_RISKY=I_UNDERSTAND` jest ustawiona."

## Risky operations checklist

### 1) `run_self_calibration` / `*CAL?`
- Co może się stać: długotrwała kalibracja, blokada instrumentu na czas operacji.
- Możliwa utrata danych: pośrednia (zmiana stanu kalibracyjnego/konfiguracji).
- Bezpieczne przygotowanie: stabilne zasilanie, brak aktywnych kampanii pomiarowych.
- Potwierdzenie operatora: jawna zgoda na self-cal i downtime.

### 2) `run_calibration` / `CALibration:ALL?`
- Co może się stać: pełna kalibracja, długi czas, możliwe zmiany stanu.
- Możliwa utrata danych: pośrednia (zmiany konfiguracji/kalibracji).
- Bezpieczne przygotowanie: osobne okno serwisowe, brak krytycznych zadań.
- Potwierdzenie operatora: jawna zgoda na full calibration.

### 3) `run_long_test` / `TEST:LONG`
- Co może się stać: długi test diagnostyczny, zajęcie instrumentu.
- Możliwa utrata danych: zwykle brak, ale możliwe wpisy/logi testowe.
- Bezpieczne przygotowanie: okno serwisowe, monitoring czasu.
- Potwierdzenie operatora: zgoda na długie zajęcie instrumentu.

### 4) `clear_test_log` / `TEST:LOG:CLEar`
- Co może się stać: wyczyszczenie logu testowego.
- Możliwa utrata danych: usunięcie historii testów.
- Bezpieczne przygotowanie: eksport/zapis logu przed czyszczeniem.
- Potwierdzenie operatora: zgoda na trwałą utratę logu testowego.

### 5) `clear_fault_log` / `SYSTem:FLOG:CLEar`
- Co może się stać: wyczyszczenie logu usterek.
- Możliwa utrata danych: utrata historii błędów/faultów.
- Bezpieczne przygotowanie: snapshot logu fault przed operacją.
- Potwierdzenie operatora: zgoda na utratę danych diagnostycznych.

### 6) `power_off` / `SYSTem:POWer:STATe`
- Co może się stać: wyłączenie urządzenia.
- Możliwa utrata danych: utrata niezapisanej sesji/stanu.
- Bezpieczne przygotowanie: zakończyć aktywne zadania, potwierdzić bezpieczny shutdown.
- Potwierdzenie operatora: jawna zgoda na wyłączenie urządzenia.

### 7) `memory_delete_all`
- Co może się stać: usunięcie wszystkich alokacji pamięci.
- Możliwa utrata danych: utrata danych tymczasowych/roboczych.
- Bezpieczne przygotowanie: backup/snapshot listy pamięci (`MEMory:CATalog?`).
- Potwierdzenie operatora: zgoda na pełne czyszczenie pamięci.

### 8) `memory_delete`
- Co może się stać: usunięcie wybranego obiektu pamięci.
- Możliwa utrata danych: utrata wskazanych danych.
- Bezpieczne przygotowanie: potwierdzić identyfikator celu i backup.
- Potwierdzenie operatora: zgoda na usunięcie konkretnego zasobu.

### 9) `mass_memory_delete`
- Co może się stać: usunięcie pliku/katalogu na nośniku.
- Możliwa utrata danych: trwała utrata plików.
- Bezpieczne przygotowanie: tylko nośnik testowy, potwierdzenie ścieżki.
- Potwierdzenie operatora: zgoda na kasowanie wskazanej ścieżki.

### 10) `mass_memory_initialize`
- Co może się stać: format/init nośnika.
- Możliwa utrata danych: całkowita utrata danych na nośniku docelowym.
- Bezpieczne przygotowanie: wyłącznie dedykowany nośnik testowy.
- Potwierdzenie operatora: podwójna weryfikacja nośnika i zgoda na format.

### 11) `mass_memory_load_*`
- Co może się stać: załadowanie stanu/danych z pliku do instrumentu.
- Możliwa utrata danych: nadpisanie aktywnej konfiguracji lub buforów.
- Bezpieczne przygotowanie: pliki testowe, weryfikacja pochodzenia i wersji.
- Potwierdzenie operatora: zgoda na modyfikację aktywnego stanu.

### 12) `mass_memory_store_*`
- Co może się stać: zapis stanu/danych instrumentu na nośnik.
- Możliwa utrata danych: nadpisanie istniejących plików.
- Bezpieczne przygotowanie: unikalne nazwy plików, nośnik testowy.
- Potwierdzenie operatora: zgoda na zapis i możliwe nadpisanie.

### 13) `delete_all_programs`
- Co może się stać: usunięcie wszystkich programów Instrument BASIC.
- Możliwa utrata danych: pełna utrata programów użytkownika.
- Bezpieczne przygotowanie: eksport/backup programów.
- Potwierdzenie operatora: zgoda na trwałe usunięcie wszystkich programów.

### 14) `delete_selected_program`
- Co może się stać: usunięcie aktualnie wybranego programu.
- Możliwa utrata danych: utrata pojedynczego programu.
- Bezpieczne przygotowanie: weryfikacja, który program jest selected, backup.
- Potwierdzenie operatora: zgoda na usunięcie wskazanego programu.

### 15) `hardcopy` / `HCOPy:IMMediate`
- Co może się stać: natychmiastowy hardcopy/print/plot do skonfigurowanego celu.
- Możliwa utrata danych: zwykle brak kasowania, ale możliwe niepożądane wyjście do systemu.
- Bezpieczne przygotowanie: jawnie ustawić bezpieczny target i nazwę pliku.
- Potwierdzenie operatora: zgoda na emisję hardcopy.

### 16) `run_curve_fit`
- Co może się stać: uruchomienie obliczeń curve fit i modyfikacja rejestrów/stanów analizy.
- Możliwa utrata danych: nadpisanie wyników tabel/rejestrów fit.
- Bezpieczne przygotowanie: snapshot rejestrów i konfiguracji analizy.
- Potwierdzenie operatora: zgoda na nadpisanie wyników fit.

### 17) `run_synthesis`
- Co może się stać: uruchomienie syntezy i modyfikacja rejestrów syntezy.
- Możliwa utrata danych: nadpisanie wyników syntezy.
- Bezpieczne przygotowanie: snapshot tabel syntezy.
- Potwierdzenie operatora: zgoda na zmianę danych syntezy.

### 18) `delete_time_capture`
- Co może się stać: usunięcie bufora time capture.
- Możliwa utrata danych: utrata nagranych danych czasowych.
- Bezpieczne przygotowanie: eksport bufora jeśli potrzebny.
- Potwierdzenie operatora: zgoda na trwałe usunięcie bufora.

### 19) `allocate_time_capture_memory`
- Co może się stać: realokacja pamięci dla time capture.
- Możliwa utrata danych: możliwe wyczyszczenie/zmiana bieżącego bufora.
- Bezpieczne przygotowanie: backup danych time capture, brak aktywnej akwizycji.
- Potwierdzenie operatora: zgoda na realokację pamięci.

### 20) `start_time_capture`
- Co może się stać: rozpoczęcie akwizycji time capture.
- Możliwa utrata danych: możliwe nadpisanie poprzednich danych zależnie od konfiguracji.
- Bezpieczne przygotowanie: potwierdzić tryb akwizycji i cel testu.
- Potwierdzenie operatora: zgoda na uruchomienie akwizycji.

## Execution policy

- Te czynności uruchamia się tylko ręcznie, świadomie, z operatorem obecnym przy stanowisku.
- Nie włączać ich do domyślnego `pytest` ani do CI.
- Każda operacja musi być logowana z timestampem i podpisem operatora.
