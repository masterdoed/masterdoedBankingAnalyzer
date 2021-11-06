import csv
import pandas
from tabulate import tabulate

#CAMT to CSV Format
#Auftragskonto
#Buchungstag
#Valutadatum
#Buchungstext
#Verwendungszweck
#Glaeubiger ID
#Mandatsreferenz
#Kundenreferenz (End-to-End)
#Sammlerreferenz
#Lastschrift Ursprungsbetrag
#Auslagenersatz Ruecklastschrift
#Beguenstigter/Zahlungspflichtiger
#Kontonummer/IBAN
#BIC (SWIFT-Code)
#Betrag
#Waehrung
#Info


df=pandas.read_csv('/Users/masterdoed/Downloads/test.csv',encoding='ISO-8859-1', error_bad_lines=False, sep=';', decimal=',')
df['Betrag']=pandas.to_numeric(df['Betrag'])
df['Betrag']=df['Betrag'].astype(float)

summe=0
for index,row in df.iterrows():
    summe=summe + row['Betrag']
    print(row['Buchungstag'] + "|" +  row['Auftragskonto'] + "|" +  row['Verwendungszweck'] + "|" + str(row['Betrag']))

print(summe)
