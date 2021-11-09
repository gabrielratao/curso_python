# -*- coding: utf-8 -*-

'''
    Análise de dados com Pandas!
    Aula 01 

    Importar pandas
    Ler arquivos excel e csv
    Ter as primeiras impressões e informações sobre os dados
    
    
'''

#%%

import pandas as pd


#%%

df_vacina = pd.read_csv(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\people-fully-vaccinated-covid.csv')
df_bu = pd.read_excel(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\MP10_BU.xlsx')



#%%

df_bu.head()
df_bu.describe()
df_bu.info()

#%%

for coluna in df_bu.columns:
    print(coluna)
    
    
    
    
    
    
    
    
    