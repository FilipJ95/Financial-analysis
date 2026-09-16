# Finansiell Analys & ETL-Pipeline (2018–2020)

Detta projekt demonstrerar en komplett **ETL-pipeline (Extract, Transform, Load)** och finansiell analys. Processen sträcker sig från relationsdatabaser i SQL till datatvätt, automatisering och beräkning av ekonomiska nyckeltal i Python.

## 🏗️ Arkitektur & Dataflöde
I detta projekt har data transformerats och strukturerats genom en robust trestegskedja för att gå från rådata till färdiga finansiella insikter:

*   **Rådata (xlsx):** Excel-fil innehållande rå transaktionsdata samt kontoplan (`Chart of Accounts`).
*   **Python (Datatvätt & ETL):** Skript (`etl_upload.py`) som använder Pandas för att rensa bort tomma kolumner, hantera saknade värden samt konvertera datatyper. Datan migreras sedan automatiskt till databasen via SQLAlchemy.
*   **MySQL (Lagring & Vy):** Den tvättade datan lagras i en stjärnstruktur bestående av dimensionstabeller (`dim_accounts`) och faktatabeller (`fact_transactions`). En SQL-vy (`v_financial_reporting`) har skapats för att effektivt samla transaktionsdatan.
*   **Python (Finansiell Analys):** Skript (`financial_analysis.py`) som hämtar datan från SQL-vyn, separerar resultat- och balansräkning, samt beräknar centrala nyckeltal för åren 2018–2020.

---

## 🏆 Resultat & Utdata
*   **Automatiserade beräkningar:** Systemet separerar automatiskt transaktionerna och räknar ut komplexa finansiella poster per år, vilket eliminerar manuella formler i Excel.
*   **Genererad Excel-rapport:** All sammanställd data och formaterade nyckeltal exporteras till en slutgiltig rapport: `Finansiell_Analys_2018_2020.xlsx`.

### Sammanställda nyckeltal i rapporten
Analysen levererar följande nyckeltal i den slutgiltiga rapporten:
*   **Omsättning & Nettoresultat**
*   **Bruttovinst & Vinstmarginal (%)**
*   **Soliditet (%)**
*   **Balanslikviditet**

---

## 🔒 Säkerhetsnotis gällande databasuppgifter
> **Viktigt:** Av säkerhetsskäl har de faktiska inloggningsuppgifterna (användarnamn och lösenord) till MySQL-databasen ändrats till platsmarkörer (`username:password`) i de publicerade skripten. 
> 
> För att köra projektet lokalt på din egen dator behöver du byta ut dessa mot dina egna, lokala databasuppgifter i följande rad i Python-skripten:
> ```python
> engine = create_engine('mysql+mysqlconnector://DITT_ANVÄNDARNAMN:DITT_LÖSENORD@localhost/bokslut_nyckeltal')
> ```

---

## 🚀 Hur man kör projektet lokalt

1. **Klona repot:**
   ```bash
   git clone https://github.com
   cd Financial-analysis
   ```


2. **Sätt upp databasen:**
   Kör SQL-skriptet i din lokala MySQL-instans för att skapa tabeller och vyer.

3. **Installera nödvändiga Python-bibliotek:**
   ```bash
   pip install pandas sqlalchemy mysql-connector-python openpyxl
   ```

4. **Konfigurera inloggning:**
   Uppdatera anslutningssträngen med dina egna databasuppgifter enligt säkerhetsnotisen ovan.

5. **Exekvera pipeline och analys:**
   Kör först skriptet för datatvätt och uppladdning, och därefter analysskriptet för att generera Excel-rapporten.
