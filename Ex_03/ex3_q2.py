# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:35:36 2020

@author: hanan
"""
import numpy as np

data = np.genfromtxt("data.txt", delimiter=',')

#Questão 02
def media_N(t_soma, div):
    quociente = (t_soma/div)
    return quociente
    
def media_movel(lista, n):
    i = 0; j = 0
    result = 0
    media = []
    for i in range(0, len(lista)-(n-1)): #(n-1) elimina os indices que não formam o par de N
        soma = 0
        for j in range(i, n+i):
            result = lista[j]
            soma += result
        result = media_N(soma, n)
        media.append(result)

        
    
    return media
#Primeiro teste
print('Teste com uma lista simples')
lista = [10, 20, 40, 45, 55, 61, 70, 11, 99]
result = media_movel(lista, 3)
print(result)
print('\n')

#Programa principal
print('Programa principal - Incidência solar para N=3')
for year in data:
    solar = media_movel(year, 3)
    print(solar)
