# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:03:30 2021

Módulo funções

    Aprender como definir uma função
    Como utilizar

@author: User
"""



#%%

def dobro(numero):
    
    dobrar = numero * 2
    
    return dobrar

    
dobro(2.5)

#%%



'''
formula:
    
    valor =(x / y) * i
    
'''


i = 0

a = 10
b = -2

def formula(x, y, i):
    
    valor = (x/y) * i 
    
    return valor
    
    
while i <= 10:
    
    print(formula(a, b, i))
    
    
    
    i += 1














