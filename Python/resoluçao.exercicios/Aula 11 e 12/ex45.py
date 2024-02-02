#Crie um programa que faça o computador jogar Jokenpô com você.  
            #probabilidades:
#1 e 1, 2 e 1, 3 e 1   pc ganhar:[1e3,2e1,3e2]
#1 e 2, 2 e 2, 3 e 2   jog ganhar:[1e2,2e3,3e1]
#1 e 3, 2 e 3, 3 e 3   empate: [1e1,2e2,3e3]           

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')

print('Bem vindo ao jogo:')
print('{:=^40}'.format('JOKENPÔ'))
print('''OPÇÕES:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')

jog = int(input('Qual a sua jogada? 0, 1 ou 2?'))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

pc = randint(0, 2)
print('O computador jogou: {} e você: {}!!'.format(itens[pc], itens[jog]))

if pc == 0 and jog == 2 or pc == 1 and jog == 0 or pc == 2 and jog == 1:
    print('Infelizmente você perdeu!!')
elif pc == 2 and jog == 0 or pc == 0 and jog == 1 or pc == 1 and jog == 2:
    print('PARABENS!! Você Ganhou!!')
elif pc == 0 and jog == 0 or pc == 1 and jog == 1 or pc == 2 and jog == 2:
    print('Deu empate!')
else:
    print('Opção invalida!!')
print(40 * '=')
