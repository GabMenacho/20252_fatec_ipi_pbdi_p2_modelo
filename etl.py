import pandas as pd
import psycopg2

# #extracao

df = pd.read_csv('dados/vgsales_CSV.csv', sep=';')
print(df.head())