# Importando Bibliotecas
import pandas as pd
import numpy as np

# Lendo arquivos
cvm = pd.read_excel("data/fundos_cvm.xlsx")
anbima = pd.read_excel("data/fundos_anbima.xlsx")

print(cvm.head(10))
