# -*- coding: utf-8 -*-
"""
    Aula 02 Pandas
    
    Analise temperatura média de toda a base de dados da BU
    Excluir linhas nulas e remover colunas
    Saber quando foi a maior e menor temperatura do ano de 2017
    Estudo de correlação entre Umidade x Temperatura x MP10
    
    
    Desafio:    
        Calcular a média de temperatura de todos os anos da base de dados
        
    
"""


import pandas as pd
#%%
df_bu = pd.read_excel(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\MP10_BU.xlsx')

#%%

soma = df_bu['TEMPERATURE'].sum()
tamanho = len(df_bu['TEMPERATURE'])

df_bu = df_bu.dropna()


media = soma / tamanho 
#%% excluir colunas?

df_bu_sem_dias = df_bu.drop(columns = ['DAY'])



#%%
'''Qual a maior e menor temperatura no ano de 2017'''

cnt = 0


for i, temperatura in enumerate(df_bu['TEMPERATURE']):
    
    if df_bu['YEAR'][i] == 2017:
        
        
        if cnt == 0:
            maior_temperatura = temperatura
            menor_temperatura = temperatura        

        else:
            
            if temperatura > maior_temperatura:
                maior_temperatura = temperatura
                
                dia_maior = df_bu['DAY'][i]
                mes_maior = df_bu['MONTH'][i]
                
                
                data = (dia_maior, mes_maior, maior_temperatura)
            
            
        cnt += 1
#%%correlação entre umidade, temperatura, MP10



a = [1, 2, 3]
b = [2, 4, 5]

ab = pd.DataFrame({'a': a,
                   'b': b})



corr_ab = ab.corr()

#%%

temperatura = df_bu['TEMPERATURE']
umidade = df_bu['HUMIDITY']
mp10 = df_bu['MP10']



novo_df = pd.DataFrame({'Temperatura': temperatura,
                        'Umidade': umidade,
                        'MP10': mp10})


corr = novo_df.corr()







