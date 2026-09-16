import pandas as pd

from sqlalchemy import create_engine

#Läser in excel_fil som ett dictionary
df_dict = pd.read_excel("Data file for students.xlsx", sheet_name = None)


gl = df_dict['GL']
accounts = df_dict['Chart of Accounts']


engine = create_engine('mysql+mysqlconnector://username:password@localhost/bokslut_nyckeltal')

#rensa rader utan account key
accounts = accounts.dropna(subset=['Account_key']) 
accounts['Account_key'] = pd.to_numeric(accounts['Account_key'], errors='coerce').astype('Int64')

accounts.columns = ['account_key','report',
                    'class', 'sub_class', 'sub_class_2',
                    'account_type', 'sub_account']



accounts.to_sql(
    name="dim_accounts",
    con=engine,
    if_exists="append",
    index=False
)



##Tvättning/resning av data i GL-flik:

#rätt datumformat
gl['Date'] = pd.to_datetime(gl['Date'])

#rensa rader utan datum
gl = gl.dropna(subset = ['Date'])

#redarer alla kolumner som är helt tomma
gl = gl.dropna(axis =1, how= 'all')

##Rensar bort namnlösa kolumner
gl = gl.loc[: ,~gl.columns.str.contains('^Unnamed', na = False)]

#Omvandlar värden till rätt format
gl['Amount'] = pd.to_numeric(gl['Amount'], errors='coerce').astype(float)
gl['Account_key'] = pd.to_numeric(gl['Account_key'], errors='coerce').astype('Int64')
gl['Territory_key'] = pd.to_numeric(gl['Territory_key'], errors='coerce').astype('Int64')


gl.columns = ['entry_no','transaction_date', 'territory_key',
              'account_key','details', 'amount']


gl.to_sql(
    name="fact_transactions",
    con=engine,
    if_exists="append",
    index=False
)

print('Värderna har laddats upp till MySQL.')









