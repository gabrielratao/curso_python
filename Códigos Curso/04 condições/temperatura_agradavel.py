# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:41:19 2021

Criar um programa que le, nome, n habitantes, temperatura e chuva
de uma cidade. E armazenar tudo em um dicionario
Mostrar qual foi a temperatura registrada
se a temperatura for maior que 32° ta calor, se tiver entre 25 e 32 
ta agradavel e se tiver menos que 25 ta ficando frio

@author: User
"""

cidade = {}

cidade["nome"] = str(input('Qual o nome da cidade? '))
cidade["habitantes"] = int(input('Quantos habitantes? '))
cidade["temperatura"] = float(input('Qual temperatura? '))
cidade['chuva'] = float(input('Quanto choveu? '))

print(f'A temperatura registrada foi {cidade["temperatura"]}°C')
#print(cidade)


if cidade["temperatura"] >= 32:
    print('Ta calor')
elif 25 <= cidade["temperatura"] < 32:
    print('Temperatura agradável')
else:
    print('Ta ficando frio!')
    