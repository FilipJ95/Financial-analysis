CREATE DATABASE bokslut_nyckeltal;

USE  bokslut_nyckeltal;

#Tabell för kontotyper
CREATE TABLE dim_accounts (
account_key INT,
report VARCHAR (50),
class VARCHAR (50),
sub_class VARCHAR (50),
sub_class_2 VARCHAR (50),
account_type VARCHAR (50),
sub_account VARCHAR (50),
PRIMARY KEY (account_key )
);

#Tabell för alla transaktioner
CREATE TABLE fact_transactions (
transaction_id INT AUTO_INCREMENT,
entry_no VARCHAR (50) ,
transaction_date DATETIME,
territory_key INT,
account_key INT,
details VARCHAR (50),
amount DECIMAL (15,2),
PRIMARY KEY (transaction_id),
FOREIGN KEY (account_key) REFERENCES dim_accounts(account_key),
FOREIGN KEY (territory_key) REFERENCES dim_territory (territory_key)
);


#Vy som innehåller information om transaktioner
CREATE VIEW v_financial_reporting AS
SELECT 
f.transaction_date, 
f.amount,
 d.report, 
 d.class, 
 d.sub_class, 
 d.sub_class_2,
 d.account_type, 
 d.sub_account 
 FROM fact_transactions AS f
INNER JOIN dim_accounts AS d
ON f.account_key = d.account_key;

























