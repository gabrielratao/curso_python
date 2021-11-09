# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:19:24 2021

função que recebe uma lista, e um argumento bool dizendo se 
esta ou nao com os dados completos, se nao estiver completo, 
fazer a contagem de dados nao nulos. 

Dados de estatura das pessoas de uma turma

Criar 2 funções. 
1 - Uma função que recebe uma base de dados e retorna True se ela tiver dados
nulos
2 - Uma função que recebe esse parametro booleano e faça a contagem dos valores nulos

@author: User
"""

dados_1 = [1.43, 1.56, 0, 1.89, 1.45, 0, 1.67, 1.78, 1.58, 1.56, 0, 1.90, 1.55, 1.53, 1.64]
dados_2 = [1.45, 1.67, 1.9, 1.55, 1.46, 1.56, 1.57, 1.87, 2.00, 1.49, 1.58, 1.59, 1.57, 1.52, 1.63]



#%%
def nulos(dados):
    tem_nulo = False
    for dado in dados:
        if dado == 0:
            tem_nulo = True
    return tem_nulo
        

teste_nulo = nulos(dados_2)


def cont_nulo(nulo, dados):
    if nulo == True:
        cnt_nulos = 0
        for dado in dados:
            if dado == 0:
                cnt_nulos += 1 
    else:
        return 0
    return cnt_nulos

    




