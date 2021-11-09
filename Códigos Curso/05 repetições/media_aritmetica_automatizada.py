# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:58:33 2021

Fazer um programa que le o nome e nota de n alunos e mostra a sua média aritetica
Armazenar os dados em uma lista 

@author: User
"""
n_alunos = 2
n_notas = 2

nomes = []
medias = []


for aluno in range(n_alunos):
    
    nome = str(input(f'Nome do aluno {aluno + 1}: '))
    nomes.append(nome)
    soma_notas = 0
    
    for nota in range(n_notas):
        nota = float(input(f'Nota {nota + 1} do aluno {aluno + 1}: '))
        
        soma_notas = soma_notas + nota
        
    media = soma_notas / n_notas
    medias.append(media)
    
#%%
for i, media in enumerate(medias):
    print(f'A média do aluno {nomes[i]} foi de {media}')
    