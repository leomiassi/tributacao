# Importando Bibliotecas
import pandas as pd
import numpy as np

# Lendo arquivos
cvm = pd.read_excel("data/fundos_cvm.xlsx")
anbima = pd.read_excel("data/fundos_anbima.xlsx")

# Separando apenas as colunas que são de nosso interesse
cvm = cvm[['id_fundo','TRIB_LPRAZO']]
anbima = anbima[['id_fundo', 'tributacao_alvo']]

# Função que retira os caracteres especiais
def limpaCNPJ(cnpj):
    return ''.join(c for c in cnpj if c.isalnum())

cvm['id_fundo'] = cvm['id_fundo'].apply(limpaCNPJ)

print(cvm.head(10))
