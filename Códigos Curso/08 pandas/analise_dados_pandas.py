# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:56:32 2021


link para estudos da biblioteca pandas: https://pandas.pydata.org/docs/index.html
@author: User
"""
#importando a biblioteca com apelido de "pd"
import pandas as pd



#%% abrindo os arquivos

#lendo os arquivos aqui no python para poder acessar os dados
df_vacina = pd.read_csv(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\people-fully-vaccinated-covid.csv')
df_bu = pd.read_excel(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\MP10_BU.xlsx')



#%% Dando uma primeira analise em toda a tabela

df_bu.head()  # mostra os 5 primeiros elementos do data frame

df_bu.describe() 

#conta nao nulos
#media da coluna
#desvio padrao
#media dos % dos valores

'''Para mais informações dessa função: 
    link: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html'''


df_bu.info() #mostra a quantidade de linhas nao nulas e o tipo de dado


#%% percorrendo o nome de todas as colunas

for coluna in df_bu.columns:
    print(coluna)


# desafio: trocar o nome das colunas


#%% análise temperatura média de toda a base de dados

#desafio: media anual da temperatura para cada ano


soma = df_bu['TEMPERATURE'].sum()

quantidade = len(df_bu['TEMPERATURE']) #sem contar as linhas nulas

df_bu_sem_linhas_nulas = df_bu.dropna()  #exlui as linhas com elemenos nulos

quantidade_sem_as_linhas_nulas = len(df_bu_sem_linhas_nulas['TEMPERATURE'])

temp_media = soma / quantidade_sem_as_linhas_nulas



#%% mas e se eu quiser excluir uma coluna inteira agora?

df_bu_sem_coluna_day = df_bu.drop(2) #esse comando exlui a linha de indice 2 de todas as colunas

df_bu_sem_coluna_day = df_bu.drop(columns = ['DAY']) #removemos a coluna DAY


#%% correlação entre temperatura e umidade

temperatura = df_bu_sem_linhas_nulas['TEMPERATURE']
umidade = df_bu_sem_linhas_nulas['HUMIDITY']

temp_umid = pd.DataFrame({'Temperatura': temperatura,
                          'Umidade': umidade})

correlacao = temp_umid.corr()

#%%

'''
Qual foi a maior e menor temperatures durante no ano 2017 na BU , 
e mostrar qual foi a data desse ocorrido.
'''

temperaturas_2017 = []


cnt = 0


for i, temperatura in enumerate(df_bu_sem_linhas_nulas['TEMPERATURE']):
    
    '''Nesse for estamos percorrendo o nosso banco de dado inteiro
    mais especificamente estamos varrendo a coluna inteira de temperatura
    e pegando a posicao e o valor de cada linha que vai sendo percorrida.
    
    Atravez desse valor de posição, nós conseguimos localizar um dado de uma outra
    coluna, por ex o dia de uma tal temperatura que quisermos olhar.
    Por isso utilizamos a função enumerate que facilita mto isso para nós'''
    
    
    if df_bu_sem_linhas_nulas['YEAR'][i] == 2017:   #o valor do ano na posição i for igual a 2017
        temperaturas_2017.append(temperatura)
        
        if cnt == 0:
            maior_temperatura = temperatura
            menor_temperatura = temperatura
            
        else:
            
            if temperatura > maior_temperatura:
                
                maior_temperatura = temperatura
                
                dia_maior = df_bu_sem_linhas_nulas['DAY'][i]
                mes_maior = df_bu_sem_linhas_nulas['MONTH'][i]
                ano_maior = df_bu_sem_linhas_nulas['YEAR'][i]
                
                data_menor = (dia_maior, mes_maior, ano_maior)
                
            if temperatura < menor_temperatura:
                
                menor_temperatura = temperatura
                
                dia_menor = df_bu_sem_linhas_nulas['DAY'][i]
                mes_menor = df_bu_sem_linhas_nulas['MONTH'][i]
                ano_menor = df_bu_sem_linhas_nulas['YEAR'][i]
                
                data_menor = (dia_menor, mes_menor, ano_menor)
        
        cnt += 1
        
        

























