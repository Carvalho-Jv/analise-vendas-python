import pandas as pd

dados = pd.read_csv("dados_vendas.csv")

# Estatísticas
total_vendas = dados["valor"].sum()
media_vendas = dados["valor"].mean()

print("Total de vendas:", total_vendas)
print("Média de vendas:", media_vendas)

# Vendas por região
vendas_regiao = dados.groupby("regiao")["valor"].sum()

print("\nVendas por região:")
print(vendas_regiao)
