# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:44:31 2021

Criar duas lista de dados.


Descobrir se os dados da lista 2 estão dentro da lista 1 e mostrar quais estão
e quais não estão
@author: User
"""

lista1 = ['UFSC', 'Uva', 5, 5.2, 'Nelson', 'Python', 'Sabonete']
lista2 = ['Uva', 5, 'Vaca', 'Gabriel']


for pos, valor in enumerate(lista2):
    if valor in lista1:
        print(f'O elemento da lista 2: {valor} está na lista 1')
    else:
        print(f'O elemento da lista 2: {valor} nao está na lista 1')
