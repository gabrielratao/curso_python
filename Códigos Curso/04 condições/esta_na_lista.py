# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:46:33 2021

Criar uma lista de dados e descobrir se um elemento qqr esta nela ou nao


@author: User
"""



lista = ['Nelson', 'UFSC', 'Carro', '3.687']



teste = input('Teste: ')

if teste in lista:
    print(f'{teste} está na lista')
else:
    print(f'{teste} nao esta na lista')
    