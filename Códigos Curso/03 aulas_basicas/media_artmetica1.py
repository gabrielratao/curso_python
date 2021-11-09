# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:53:46 2021

Fazer um programa que le o nome e nota de 2 alunos e mostrar a 
respectiva media 
@author: User
"""

#%% por os dados em uma lista



























alunos = []
notas = []

#alunos 1
nome_1 = str(input('Nome do aluno 1: '))
nota_1_aluno_1 = float(input('P1 do aluno 1: '))
nota_2_aluno_1 = float(input('P2 do aluno 1: '))

#alunos 2
nome_2 = str(input('Nome do aluno 2: '))
nota_1_aluno_2 = float(input('P1 do aluno 2: '))
nota_2_aluno_2 = float(input('P2 do aluno 2: '))

#adicionando o nome dos alunos na lista
alunos.append(nome_1)
alunos.append(nome_2)

#adicionando as dos alunos na lista
notas.append(nota_1_aluno_1)
notas.append(nota_2_aluno_1)

notas.append(nota_1_aluno_2)
notas.append(nota_2_aluno_2)

media_aluno_1 = (notas[0] + notas[1]) / 2
media_aluno_2 = (notas[2] + notas[3]) / 2

print('')
print('Notas dos alunos')
print(f'A média do aluno {alunos[0]} é {media_aluno_1}')
print(f'A média do aluno {alunos[1]} é {media_aluno_2}')




















































