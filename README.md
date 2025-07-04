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
