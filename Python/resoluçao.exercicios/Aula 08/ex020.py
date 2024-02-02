            # *AULA O8 EXERCICIO 20*
            # *SORTEANDO UM ITEM DA LISTA*

# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = str(input('Aluno um:'))
a2 = str(input('Aluno dois'))
a3 = str(input('Aluno tres)'))
a4 = str(input('Aluno quatro:'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
