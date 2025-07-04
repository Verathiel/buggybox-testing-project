# Testovací plán – BuggyBox

## Cíl testování
Otestovat funkčnost formuláře a API v aplikaci BuggyBox, identifikovat chyby a navrhnout zlepšení.

---

## Testovací scénáře

### 1. Formulář (web)

| Test | Popis | Očekávaný výsledek | Skutečný výsledek | Stav (PASS/FAIL) |
|-------|--------|---------------------|-------------------|------------------|
| 1.1 | Vyplnění všech polí správně | Formulář odeslán, zobrazí se potvrzení | Formulář odeslán, potvrzení se zobrazilo | PASS |
| 1.2 | Prázdné jméno | Formulář neodešle, zobrazí chybu | Formulář odeslán bez chyby | FAIL |
| 1.3 | Nesprávný email (bez @) | Formulář neodešle, zobrazí chybu | Formulář odeslán bez chyby | FAIL |
| 1.4 | Záporný věk | Formulář neodešle, zobrazí chybu | Formulář odeslán bez chyby | FAIL |

---

### 2. API `/api/submit`

| Test | Popis | Očekávaný výsledek | Skutečný výsledek | Stav (PASS/FAIL) |
|-------|--------|---------------------|-------------------|------------------|
| 2.1 | Validní data JSON | API vrátí 200 a data | API vrací 200 a data | PASS |
| 2.2 | Chybějící jméno | API vrátí chybu | API vrací 200 bez chyby | FAIL |
| 2.3 | Prázdný email | API vrátí chybu | API vrací 200 bez chyby | FAIL |
| 2.4 | Záporný věk | API vrátí chybu | API vrací 200 bez chyby | FAIL |

---

## Závěr

- Aplikace obsahuje základní chyby v validaci formuláře i API.
- Automatizované testy tyto chyby odhalují.
- Doporučení: přidat validaci na straně serveru, aby se zabránilo přijetí chybných dat.

---

## Poznámky

- Testy jsou napsané pomocí Python `unittest`.
- Testovací scénáře lze rozšířit o další hraniční případy.
