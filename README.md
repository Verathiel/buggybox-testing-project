![Tests](https://github.com/Verathiel/buggybox-testing-project/actions/workflows/tests.yml/badge.svg)
# BuggyBox – projekt pro testování aplikace

## Popis

BuggyBox je jednoduchá Flask aplikace s formulářem, která obsahuje záměrné chyby v validaci vstupních dat.  
Cílem projektu je ukázat schopnost identifikovat a automaticky testovat chyby v aplikaci.

## Struktura projektu

- `app/` – zdrojový kód aplikace a šablony
- `tests/` – automatizované testy a testovací plán
- `.github/workflows/tests.yml` – workflow pro GitHub Actions, které automaticky spouští testy

## Jak spustit projekt

### Lokálně

1. Nainstaluj Python 3.10+  
2. Nainstaluj Flask:

   ```bash
   pip install flask
Spusť aplikaci:

bash
Zkopírovat
Upravit
python app/app.py
Otevři v prohlížeči:

cpp
Zkopírovat
Upravit
http://127.0.0.1:5000/
Spuštění testů
Spustíš příkazem:

bash
Zkopírovat
Upravit
python -m unittest discover -s tests
Co projekt ukazuje
Základní Flask aplikaci s formulářem

Automatizované testy formuláře a API

Detekci chyb v aplikaci

GitHub Actions pro automatické spouštění testů (CI/CD)

Kontakt
Veronika Flachsová
veronikaflachsova186@gmail.com
