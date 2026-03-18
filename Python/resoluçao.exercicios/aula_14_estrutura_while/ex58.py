#                   EXERCICIO 58: 
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

ncont = 1

ncomputador = random.randint(1, 10)
njogador = int(input('Entre 0 e 10, que numero estou pensando:'))
print('PROCESSANDO...')
sleep(2)

while ncomputador != njogador:
    sleep(1)
    print("Você errou!!")
    njogador = int(input("Tente novamente:"))
    ncont += 1

sleep(1)
print(f"Parabens!! Você acertou na {ncont}° tentativa!!")


