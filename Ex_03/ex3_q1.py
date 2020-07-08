# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:37:54 2020

@author: hanan
"""

#Questão 01
def fatorial(n):
    if n < 0:
        print('fatorial não admite número negativo')
        return 0
    if n == 0: 
        result = 1
        return result
    fat = 1
    for i in range(1, n+1):
        fat = fat*i
        
    return fat

for i in range(0, 21):
    x = fatorial(i)
    print('fatorial de %d: %d' %(i ,x))
