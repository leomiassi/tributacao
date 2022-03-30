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

# Funcao que compara os valores de tributação das bases
def comparaTributacao(tabela):
    tabelaAuxiliar = tabela.copy()  #Copiando a tabela para manter os valores originais de tributacao
    tabelaAuxiliar['TRIB_LPRAZO'] = tabelaAuxiliar['TRIB_LPRAZO'].replace(['S'],'Longo Prazo')
    tabelaAuxiliar['TRIB_LPRAZO'] = tabelaAuxiliar['TRIB_LPRAZO'].replace(['N/A'],'Não Aplicável')
    tabelaAuxiliar['TRIB_LPRAZO'] = tabelaAuxiliar['TRIB_LPRAZO'].replace([np.nan],'Indefinido')
    return np.where((tabelaAuxiliar['TRIB_LPRAZO'] == tabelaAuxiliar['tributacao_alvo']),'igual','diferente')

# Recebendo o resultado em uma nova coluna
tabelaFinal['resultado'] = comparaTributacao(tabelaFinal)

# Convertendo o cnpj para string, permitindo que o excel mostre corretamente o valor dessa coluna
tabelaFinal['id_fundo'] = tabelaFinal['id_fundo'].astype(str)

print(tabelaFinal.head(10))
