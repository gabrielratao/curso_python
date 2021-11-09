# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:32:28 2021

1 - realizar um unpacking de uma variável qualquer que você escolher
2- criar uma lista de tupla e mostrar o ultimo valor da terceira lista

@author: User
"""
#%%
dados = (28, 9, 1999, 'Gabriel', 'UFSC')

dia, mes, ano, nome, faculdade = dados

print(nome, faculdade)

#%%

dados = [
    (37, 1.87, 'Nelson'),
    ('ENS', 'INE', 'ECV'),
    ('Uva', 'Morango', 'Banana', 'Maça', 'Limao'),
    ('Carro', 'Moto', 'Bicicleta', 'Buzao', 98, 5.6)
    ]

#          lista x posição
print(dados[2][-1])
