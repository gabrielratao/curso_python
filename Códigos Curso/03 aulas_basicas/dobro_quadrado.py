# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:38:50 2021

Exercicio:
    ler um numero e mostrar ao usuário:
        Dobro, triplo, raíz quadrada, resto da divisão por 5

@author: User
"""





























n = int(input('Digite um valor: '))

dobro = n*2
quadrado = n**2
raiz = n**(1/2)
resto = n % 5

print(f' dobro {dobro}\n quadrado {quadrado}\n raiz {raiz:.2f}\n resto da divisão por 5 é {resto}')
    
print('fim')