# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:36:13 2021

Criação de gráficos!

aula 01


@author: User
"""

#%%

import matplotlib.pyplot as plt

#%%


cidade = ['Floripa', 'Rio de Janeiro','Palhoça', 'São José']
kg = [20, 50, 18, 29]
cor = ['green', 'dimgray', 'coral', 'aqua']

plt.bar(cidade, kg, color = cor)

plt.suptitle('Analise de resíduos nas cidades')

plt.ylabel('KG residuo')

plt.grid()

plt.show()

plt.savefig(r'C:\Users\User\Documents\00 UFSC\curso_python\09 matplotlib\figuras\\'+'teste_figura.png')




