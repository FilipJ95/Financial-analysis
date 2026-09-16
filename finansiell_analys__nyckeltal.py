import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://username:password@localhost/bokslut_nyckeltal')


def get_financial_data(engine):
    query = "SELECT * FROM v_financial_reporting"
    return pd.read_sql(query, con=engine)

df = get_financial_data(engine)

#Separerar resultat och balansräkning
df_profit_loss = df[df['report'] == 'Profit and Loss']
df_balance_sheet = df[df['report'] == 'Balance Sheet']


#Funktion för att beräkna resultaträkningar
def calculate_profit_loss(df_profit_loss):
    
    #Identifierar intäkter och kostnader i två olika listor
    revenues = ['Sales', 'Interest Income', 'Dividend Income'
            ,'Gain/Loss on Sales of Asset', 'Exchange Loss/Gain']
    expenses = ['Cost of Sales', 'Operating Expenses',
            'Depreciation & Amortization', 'Interest Expense', 'Taxation']

    #Lista för att spara resultat
    annual_results = []

    #En loop där resultatet samt nyckeltal sparas i listan ovan.
    for year in [2018, 2019, 2020]:
        #Resultatposter för aktuellt år lagras 
        df_profit_loss_year= df_profit_loss[df_profit_loss[
        'transaction_date'].dt.year == year]


        #Dataframes för intäkter/kostnader  
        df_rev = df_profit_loss_year[df_profit_loss_year['sub_class'].isin(revenues)]
        df_exp = df_profit_loss_year[df_profit_loss_year['sub_class'].isin(expenses)]


        #Totala intäkter/kostnader
        total_rev = df_rev['amount'].sum()
        total_exp = df_exp['amount'].sum()

        #Omsättning samt kostnad sålda varor
        sales = df_rev[df_rev['sub_class'] == 'Sales']['amount'].sum()
        cost_of_sales = df_exp[df_exp['sub_class'] == 'Cost of Sales']['amount'].sum()

        #Bruttovinst
        gross_profit= sales + cost_of_sales

        #Nettorestultat
        net_income = total_rev + total_exp

        #Vinstmarginal
        profit_margin = (net_income/sales)

        #lägg in all info i en lista
        annual_results.append({
            "År": year,
            "Omsättning": sales,
            "Nettoresultat": net_income,
            "Bruttovinst": gross_profit,
            "Vinstmarginal": profit_margin})

    #Lägger in alla resultat i en dataframe
    df_results = pd.DataFrame(annual_results)
    
    return df_results


    
#Funktionen för att beräkna balansräkningar
def calculate_balance_sheet(df_balance_sheet):
    
    #Lista för att spara balansräkningar
    annual_balance_sheet = []

    #Loop för beräkning av balansräkning samt dess nyckeltal
    for year in [2018, 2019, 2020]:
        #Balansräkningsdata för aktuellt år lagras
        df_balance_sheet_year = df_balance_sheet[
            df_balance_sheet['transaction_date'].dt.year == year]
        
        #Dataframes för tillgånger/skulder/EK/kortfristiga skulder
        df_assets = df_balance_sheet_year[df_balance_sheet_year['sub_class'] == 'Assets']
        df_liabilities = df_balance_sheet_year[df_balance_sheet_year['sub_class'] == 'Liabilities']
        df_owners_equity = df_balance_sheet_year[df_balance_sheet_year['sub_class'] == 'Owners Equity']

         #Kortfristiga skulder
        df_current_liabilities = df_balance_sheet_year[df_balance_sheet_year['sub_class_2'] == 'Current Liabilities']
        #Omsättningstillgångar
        df_current_assets = df_balance_sheet_year[df_balance_sheet_year['sub_class_2'] == 'Current Assets']
       
        #Totalen av tillgånger/skulder/EK
        total_assets = df_assets['amount'].sum()
        total_liabilities = df_liabilities['amount'].sum()
        total_owners_equity = df_owners_equity['amount'].sum()

        #Totalen av kortfristiga skulder/omsättningstillgångar
        total_current_liabilities = df_current_liabilities['amount'].sum()
        total_current_assets = df_current_assets['amount'].sum()

        #Soliditet
        equity_ratio = (total_owners_equity/total_assets)
        
        #Balanslikviditet
        current_ratio = (total_current_assets/total_current_liabilities)

        #Lägger in info i listan
        annual_balance_sheet.append({
            "År": year,
            "Tillgångar": total_assets,
            "Skulder": total_liabilities,
            "Eget Kapital": total_owners_equity,
            "Soliditet": equity_ratio,
            "Balanslikviditet" : current_ratio})
        

    #Lägger in alla balansräkningar i en dataframe
    df_balance_sheets = pd.DataFrame(annual_balance_sheet)
    
    return df_balance_sheets


#Kör funktionerna för att beräkna balans/resultatäkning för åren
df_results = calculate_profit_loss(df_profit_loss)
df_balance_sheets = calculate_balance_sheet(df_balance_sheet)


#Slå ihop resultat och balansräkning utifrån kolumnen År
df_final = pd.merge(df_results, df_balance_sheets, on = "År")

# Snygga till ordningen på kolumnerna
df_final = df_final[[
    "År", "Omsättning", "Bruttovinst", "Nettoresultat", "Vinstmarginal",
    "Tillgångar", "Eget Kapital", "Skulder", "Soliditet", "Balanslikviditet"
]]


#Formatera vissa nyckeltal till procent
df_final["Vinstmarginal"] = df_final["Vinstmarginal"].map('{:.2%}'.format)
df_final["Soliditet"] = df_final["Soliditet"].map("{:.2%}".format)

#Spara mina resultat i en excel-fil
df_final.to_excel("Finansiell_Analys_2018_2019_2020.xlsx", index=False)
print("Analysen är färdig och sparad till Excel.")

                                




                                     