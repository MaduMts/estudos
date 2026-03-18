#           EXERCICIO 68 

# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 


#MINHA RESOLUÇÃO:

import random

print(40 * "=")
print(13*" ", "PAR OU IMPAR")
print(40 * "=")
print("Jogue par ou impar com o computador e tente o maximo de vitorias consecutivas!")

cont_win = 0

while True:

    parimpar_user = ' '

    #ESCOLHAS DO USUARIO:
    #par ou impar 
    parimpar_user = input("Escolha par ou impar: P/I").strip().upper()[0]
    while parimpar_user not in 'PI':
        print("Comando invalido")
        parimpar_user = input("Escolha par ou impar: P/I").strip().upper()[0]

    #numero desejado
    num_user = int(input("Digite um numero:"))

    
    #Escolha do Pc:
    num_pc = random.randint(1,10)

    #Soma pro jogo:
    soma_nums = num_user + num_pc


    #Rodando o jogo:
    print(f"O computador escolheu: {num_pc}")
    print(f"A soma deu: {soma_nums}")

    if parimpar_user == 'P' and soma_nums % 2 == 0:
        cont_win =+ 1
        print("Parabens você ganhou!!")
        
    elif parimpar_user == 'I' and soma_nums % 2 != 0:
        cont_win =+ 1
        print("Parabens, você ganhou!")

    else:
        print("Você perdeu!!")
        print(f"Total de vitorias consecutivas foi: {cont_win}")
        break
