# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:23:20 2021

atividade dict

criar um dicionario com os dados de uma cidade:
    nome
    quantos habitantes
    maior temperatura do ano
    maior indicie de chuva
    

Ao final mostrar qual foi a maior temperatura registrada



@author: User
"""





















cidade = {}

cidade["nome"] = str(input('Qual o nome da cidade? '))
cidade["habitantes"] = int(input('Quantos habitantes? '))
cidade["temperatura"] = float(input('Qual foi temperatura registrada? '))
cidade['chuva'] = float(input('Qual foi o índicie pluviométrico? '))

print(f'A maior temperatura registrada foi {cidade["temperatura"]}°C')
print(cidade)