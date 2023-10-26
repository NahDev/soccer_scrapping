import pandas as pd

# 1. Leitura do CSV
df = pd.read_csv('dados.csv')

# 2. Análise inicial
print(df.head())  # Visualize as primeiras linhas do DataFrame
print(df.describe())  # Resumo estatístico dos dados
