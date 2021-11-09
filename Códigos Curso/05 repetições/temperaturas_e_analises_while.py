# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:35:08 2021

Criar um banco de dados com as temperaturas de uma cidade ao longo do tempo 
e perguntar se quer continuar ou nao. Ao final mostrar qual foi a maior 
e menor temperatura e a temperatura media do periodo, e quantas temperaturas foram
adicionadas.


@author: User
"""
temperaturas = []
cnt = 0

#maior = 0
#menor = 0

somatorio = 0

while True:
    
    temperatura = float(input('Digite uma nova temperatura: '))
    temperaturas.append(temperatura)
    
    if cnt == 0:
        maior = temperatura
        menor = temperatura
    cnt +=1
    
    if temperatura > maior:
        maior = temperatura
        
    if temperatura < menor:
        menor = temperatura
    
    somatorio = somatorio + temperatura
    
    continuar = str(input('Voce quer continuar? [S/N]: ')).upper()
    
    if continuar == 'N':
        print(f'Finalizando o programa a um total de {cnt} temperaturas registradas')
        break
 
media = somatorio / cnt

print()
print(f'A maior temperatura registrada foi {maior}°C')
print(f'A menor temperatura registrada foi {menor}°C')
print(f'A temperatura média no período foi de {media:.2f}°C')


