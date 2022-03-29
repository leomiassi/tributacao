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

# Retirando caracteres especiais do cnpj
cvm['id_fundo'] = cvm['id_fundo'].apply(limpaCNPJ)

# Convertendo os valores para numerico
cvm['id_fundo'] = pd.to_numeric(cvm['id_fundo'])
anbima['id_fundo'] = pd.to_numeric(anbima['id_fundo'])

# Juntando as bases pela chave em comum 'id_fundo'
tabelaFinal = pd.merge(cvm, anbima, how='inner', on='id_fundo')

print(tabelaFinal.head(10))
print(tabelaFinal.info())
