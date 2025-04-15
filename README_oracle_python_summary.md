
# Postup práce

- Založila jsem **Oracle Cloud DB (Free Tier)**, přes SQL Developer vytvořila tabulky, vložila dummy data a vytvořila view.
- SQL skripty jsem uložila do **GitHub repozitáře**.
  - Repozitář jsem inicializovala pomocí `git init`, napojila na GitHub a pushnula pomocí CLI.
- Vytvořila jsem **Python skript pro připojení k DB pomocí `oracledb`**.
  - **Problém:**
    - Thin klient nefungoval (nepodporuje wallet – autentizační balíček)
    - Musela jsem přejít na thick klient (Oracle Instant Client)
    - Při použití thick režimu ale Oracle ignoroval moji složku s walletem → hledal `tnsnames.ora` ve výchozím `network/admin`
      - Vyřešeno pomocí `os.environ["TNS_ADMIN"] = wallet_location`

- **Klíčový bod:** `cursor` mi ukázal konkrétní chybu a díky tomu jsem během 5 minut vyřešila to, co bez kurzoru nešlo hodinu odhalit.  
  `Cursor` „zná kontext“ a zobrazí skutečnou odpověď databáze.

## Výsledek

- Skript funguje s walletem v thick režimu
- Připojení, dotaz i výpis dat fungují
- Celý postup si můžu snadno zopakovat nebo předat dál
