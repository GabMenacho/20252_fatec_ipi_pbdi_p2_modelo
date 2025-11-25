import pandas as pd
import psycopg2

# #extracao

df = pd.read_csv('dados/vgsales_CSV.csv', sep=';')
print(df.head())

#transformação
df["jogo_key"] = df["Name"].astype('category').cat.codes + 1
 
df["ano_key"] = df["Year"]
 
df["plataforma_key"] = df["Platform"].astype('category').cat.codes + 1
 
df["genero_key"] = df["Genre"].astype('category').cat.codes + 1
 
df["editora_key"] = df["Publisher"].astype('category').cat.codes + 1

print(df.shape)
print(df.dtypes)
print(df.head())

#conexao com o banco de dados
conexao = psycopg2.connect(
    host='localhost',
    database = 'p2_video_game_sales',
    user='postgres',
    password='123456'
)

print(conexao)

cur = conexao.cursor()


dim_jogo = df[["jogo_key", "Name", "Rank"]].drop_duplicates()

for index, row in dim_jogo.iterrows():
    cur.execute("""
        INSERT INTO dim_jogo (jogo_key, nome, rank)
        VALUES (%s, %s, %s)
        ON CONFLICT (jogo_key) DO NOTHING;
    """, (row["jogo_key"], row["Name"], row["Rank"]))
 
dim_tempo = df[["ano_key", "Year"]].drop_duplicates()
for index, row in dim_tempo.iterrows():
    cur.execute("""
        INSERT INTO dim_tempo (data_key, ano)
        VALUES (%s, %s)
        ON CONFLICT (data_key) DO NOTHING;
    """, (row["ano_key"], row["Year"]))
 
dim_plataforma = df[["plataforma_key", "Platform"]].drop_duplicates()
for index, row in dim_plataforma.iterrows():
    cur.execute("""
        INSERT INTO dim_plataforma (plataforma_key, nome)
        VALUES (%s, %s)
        ON CONFLICT (plataforma_key) DO NOTHING;
    """, (row["plataforma_key"], row["Platform"]))
 
dim_genero = df[["genero_key", "Genre"]].drop_duplicates()
for index, row in dim_genero.iterrows():
    cur.execute("""
        INSERT INTO dim_genero (genero_key, genero)
        VALUES (%s, %s)
        ON CONFLICT (genero_key) DO NOTHING;
    """, (row["genero_key"], row["Genre"]))
 
dim_editora = df[["editora_key", "Publisher"]].drop_duplicates()
for index, row in dim_editora.iterrows():
    cur.execute("""
        INSERT INTO dim_editora (editora_key, nome)
        VALUES (%s, %s)
        ON CONFLICT (editora_key) DO NOTHING;
    """, (row["editora_key"], row["Publisher"]))
 
fato = df[[
    "jogo_key", "ano_key", "plataforma_key", "genero_key", "editora_key",
    "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"
]]

for index, row in fato.iterrows():
    cur.execute("""
        INSERT INTO fato_vendas_vg (
            jogo_key, ano_key, plataforma_key, genero_key, editora_key,
            vendas_na, vendas_eu, vendas_jp, vendas_outras, vendas_global
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        row["jogo_key"],
        row["ano_key"],
        row["plataforma_key"],
        row["genero_key"],
        row["editora_key"],
        row["NA_Sales"],
        row["EU_Sales"],
        row["JP_Sales"],
        row["Other_Sales"],
        row["Global_Sales"]
    ))

conexao.commit()
print(f"\n Carga da Tabela Fato (fato_vendas_vg) concluída!") 
# Fecha o cursor e a 
# cur.close() 
# conexao.close()