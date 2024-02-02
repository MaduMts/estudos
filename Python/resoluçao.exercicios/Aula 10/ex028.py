      #AULA 10 EXERCICIO 28
      #JOGO DA ADIVINHAÇÃO

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randint(1, 5)
num2 = int(input('Entre 0 e 5, que numero estou pensando:'))
print('PROCESSANDO...')
sleep(2)
if num == num2:
  print('Parabéns, você acertou!!')
else:
  print('Não foi desta vez!!')
