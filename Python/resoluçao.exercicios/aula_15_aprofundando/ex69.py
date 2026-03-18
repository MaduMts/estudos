#               EXERCICIO 69 
# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

cont_pessoas = 0
sexo = ' '
continuar = ' '

# SOLUÇÃO A:
cont_pessoas18 = 0

# SOLUÇÃO B:
cont_homens = 0

# SOLUÇÃO C:
cont_mulheres = 0

print(f"{20*"="}  BEM VINDO  {20*"="}")

while True:

    cont_pessoas += 1

    print(f"{15 * ' '} CADASTRE A {cont_pessoas}° PESSOA {15 * ' '}")
    print("\n")

    # FAZENDO O CADASTRO
    nome = input("NOME:").lower().strip()
    idade = int(input("IDADE:"))
    sexo = input("SEXO (M/F):").upper().strip()
    while sexo not in('MF'):
        print("Comando invalido!")
        sexo = input("SEXO (M/F):").upper().strip()


    # SOLUÇÃO A:
    if idade >= 18:
        cont_pessoas18 += 1

    #SOLUÇÃO B:
    if sexo == 'M':
        cont_homens += 1

    #SOLUÇÃO C
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    
    print(f"{cont_pessoas}° pessoa cadastrada com sucesso!!")

    continuar = input("Deseja continuar (S/N)?").upper().strip()
    while continuar not in ('SN'):
        print("Comando invalido!")
        continuar = input("Deseja continuar (S/N)?").upper().strip()

    if continuar == 'S':
        print("Reiniciando...")
        print("\n")

    else:
        print('\n')
        print("EM SEU GRUPO DE PESSOA(S): \n")
        print(f"tem {cont_pessoas18} pessoa(s) com mais de 18 anos")
        print(f"Sendo {cont_homens} do sexo masculino")
        print(f"e {cont_mulheres} do sexo feminino com menos de 20 anos")
        print("Até a proxima!")
        break
