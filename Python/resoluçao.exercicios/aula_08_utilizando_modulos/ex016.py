            # *AULA O8 EXERCICIO 16*
            # *QUEBRANDO UM NUMERO*

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# MODO 1
import math
n = float(input('Digite um numero quebrado:'))
ninteiro = math.floor(n)
print('O seu numero inteiro é: {}'.format(ninteiro))

# MODO 2
num = float(input('Digite outro numero quebrado:'))
print('O numero inteiro é: {}'.format(int(num)))

# MODO 3
from math import trunc
nume = float(input('Digite outro numero quebrado:'))
print('O numero inteiro é: {}'.format(trunc(nume)))
