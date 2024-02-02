      #AULA 10 EXERCICIO 30
      #Par ou Ímpar?

# Crie um programa que leia um número inteiro e mostre 
#na tela se ele é PAR ou ÍMPAR.

from time import sleep
num = int(input('Digite um numero:'))
print('PROCESSANDO...')
sleep(1)
resultado = num % 2
if resultado == 0:
  print('Este numero é par')
else:
  print('Este numero é impar')
