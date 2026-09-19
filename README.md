# Finansiell Analys & ETL-Pipeline (2018–2020)
I detta projekt har jag arbetat med en finansiell analys från en Excel-fil hämtad från Kaggle. Detta har jag gjort med hjälp av en **ETL-pipeline (Extract, Transform, Load)** .

## 🏗️ Arkitektur & Dataflöde
I projektet har data transformerats och framställts genom tresteg för att gå från rådata till färdig finansiell information: 

*   **Rådata (xlsx):** Excel-fil som innehåller transaktions data ('GL')samt kontoplan (`Chart of Accounts`).
*   **Python (Datatvätt & ETL):** Ett skript som hämtar data från Excel-filen. Data transformeras genom att rätt formatering samt rensning av tomma rader. Sedan laddas data automatiskt upp till MySQL. 
*   **MySQL (Lagring & Vy):** Data lagras i två tabeller: dim_accounts (kontoplan) och fact_transactions (transaktioner). En vy skapas sedan där tabellerna slås ihop och visar transaktionerna, transaktionernas  belopp samt deras kontotyp.
*   **Python (Finansiell Analys):** Vyn hämtas i ett python-skript. Resultat- och balansräkning beräknas för åren 2018-2020 samt olika nyckeltal. 

---

## 🏆 Resultat & Utdata
*   **Automatiserade beräkningar:** Systemet gör automatiska beräkningar för finansiella poster, vilket sparar mycket tid jämfört med manuellt arbete i Excel.
*   **Genererad Excel-rapport:**  När beräkningarna är utförda laddas informationen automatiskt upp till en excel-fil: `Finansiell_Analys_2018_2020.xlsx`.

### Sammanställda nyckeltal i rapporten
Analysen visar följande nyckeltal i den slutgiltiga rapporten:
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
