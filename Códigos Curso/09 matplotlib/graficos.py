# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:32:32 2021


Gráficos da base de dados da BU:
    MP10, Temperatura, Umidade no mesmo gráfico
    - Titulo, cores, legenda, nome dos eixos, valores nos eixos,
    
    
    
Para mais informações sobre a biblioteca matplotlib e 
ver muitos exemplos irados de graficos:
    
    https://matplotlib.org/

@author: User
"""


#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% lendo o arquivo da BU e já tirando as linhas nulas


df_bu = pd.read_excel(r'C:\Users\User\Documents\00 UFSC\curso_python\08 pandas\arquivos\MP10_BU.xlsx')

df_bu = df_bu.dropna()

#%%

for coluna in df_bu.columns:
    print(coluna)
    
    
#%% definindo as medias de Temperatura, Umidade, MP10 para plotar diretamente
#por numpy
 
#criando uma matriz numpy com os valores de MP10
mp10 = np.array(df_bu['MP10'])

#vamos criar uma matriz com n linhas onde n é o numero total de dados que tem MP10
# e cada linha vai ter o valor de sua media
media_MP10 = [np.mean(mp10)] * len(mp10)  
'''Essa matriz que criamos é assim:

    O numero de linhas que ela tem é o numero total de dados
    que tem de MP10 na nossa base de dados
    
    E cada valor dentro é a media. Cada linha tem o msm valor 
    de média.
    
    Mas pq estamos fazendo isso?
    
    Isso é um truque para podermos plotar nos gráficos o valor
    da média. E esse valor por ser fixo vai ser uma linha reta
    que vai passar por todo o gráfico.
    
    Mas pq usar uma matriz assim e  nao simplesmente o valor da media
    e pronto?
    
    Basicamente pq a nossa biblioteca matplotlib utiliza os pares ordenados
    para criar as figuras.
    
    Entao se a gente colocar so o valor da média vai ficar apenas 1 ponto 
    no grafico. E nao é isso que queremos. Nós queremos uma reta.
    
    Entao essa reta precisa abrenger todos os pontos da nossa base de dados.
    Por isso fizemos uma matriz com os valores de media pra cada valor na tabela.
    
    Teste depois plotar apenas 1 valore da media para ver oq acontece.
    _____________________________________________________________________________
    Essa parte de matriz pode parecer um poucoestranha no inicio dos estudos,
    caso vc não tenha entendido direito, sugiro que vc abra um novo arquivo
    rascunho e crie matrizes usando listas e utilize essas funções do numpy que 
    utilizamos:
    np.array
    np.mean
    E va executnado esses codigos separadamente para entender oq esta acontecendo'''
    


#agora replicaremos a mesma lógica para as outras variaves:

temperatura = np.array(df_bu['TEMPERATURE'])
media_temperatura = [np.mean(temperatura)] * len(temperatura)
    
umidade = np.array(df_bu['HUMIDITY'])
media_umidade = [np.mean(umidade)] * len(umidade)

#pronto agora bora pros graficos
#%% criando os gráficos!  em subplots do jeito mais simples

'''sub plot de 3 linhas e 1 coluna
Nada mais é que: 3 linhas de gráficos em apenas uma coluna,

se eu quisesse por os 3 na vertical por ex eu faria (1, 3)

o prox comando diz: o grafico que vamos fazer agr esta no formato
de 3x1 e é o primeiro deles. E assim por diante'''

plt.subplot(3, 1, 1)


plt.plot(df_bu['TEMPERATURE'], label = 'Temperatura', color = 'red')
plt.plot(media_temperatura, color = 'black', label= 'Média') #adicionando a linha reta da media
plt.ylabel('°C      ', rotation = 0)

plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df_bu['HUMIDITY'], label = 'Umidade', color = 'blue')
plt.plot(media_umidade, color = 'black', label= 'Média')
plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.ylabel('%', rotation = 0)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df_bu['MP10'], label = 'MP10', color = 'green')
plt.plot(media_MP10, color = 'black', label= 'Média')
plt.xticks([0, 72, 147, 217], ['2014', '2017', '2018', '2019'])
plt.ylabel('ug/m³        ', rotation = 0)
plt.legend(loc='lower left')

plt.suptitle('Análise Temperatura, Umidade, MP10 na BU \n 2014-2019')
plt.show()

'''
Desafio: ajustar os dados para ficar com uma serie temporal mais decente
tecnicamente 

'''
