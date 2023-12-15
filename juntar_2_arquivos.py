import pandas as pd

# Carregue os dois arquivos CSV
df2 = pd.read_csv('dados/static_serie_a_13_11_2023.csv')
df1 = pd.read_csv('dados/eficiencia_finalizacoes.csv')

# Remover espaços em branco extras nos valores da coluna "TIME"
df1['TIME'] = df1['TIME'].str.strip()
df2['TIME'] = df2['TIME'].str.strip()

# Normalizar os caracteres para evitar discrepâncias
df1['TIME'] = df1['TIME'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df2['TIME'] = df2['TIME'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# Juntando os DataFrames usando a coluna "TIME" como chave
df_final = pd.merge(df1, df2, on='TIME')

# Exibindo o DataFrame resultante
print(df_final)
df_final.to_csv('dados/combinado.csv', index=False)
git remote add origin https://github.com/NahDev/soccer_scrapping.git