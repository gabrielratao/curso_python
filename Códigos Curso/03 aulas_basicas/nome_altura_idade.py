# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:12:00 2021

Fazer um programa que le as informação do usuario:
    nome
    altura
    ano que nasceu
    
Ao final mostrar a idade dessa pessoa


@author: User
"""























nome = str(input('Nome da pessoa: '))
altura = float(input(f'Altura da pessoa {nome}: '))
ano_nasceu = int(input('Ano que que a pessoa nasceu: '))

ano_atual = 2021

idade = ano_atual - ano_nasceu

print(f'A pessoa {nome} tem {idade} anos.')

