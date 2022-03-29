# Importando Bibliotecas
import pandas as pd
import numpy as np

# Lendo arquivos
cvm = pd.read_excel("data/fundos_cvm.xlsx")
anbima = pd.read_excel("data/fundos_anbima.xlsx")

# Separando apenas as colunas que são de nosso interesse
cvm = cvm[['id_fundo','TRIB_LPRAZO']]
anbima = anbima[['id_fundo', 'tributacao_alvo']]

print(cvm.head(10))

