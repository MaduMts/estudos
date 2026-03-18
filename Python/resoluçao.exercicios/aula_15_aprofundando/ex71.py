#                   EXERCICIO 71 
# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#Minha logica:
#entrada: 280

# 280 // 50 = 5 (Quantas notas são necessarias)
#resto: 30 (Oque sobrou pra imprimir)

# 30 // 20 = 1
#resto:10

# 10 // 10 = 1
#resto: 0

nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

print(40 * "=")
print(16*" ", "ATM")
print(40 * "=")

sacar = int(input("Qual valor você gostaria de sacar?"))

while True:
    nota50 = sacar // 50
    sacar %= 50

    nota20 = sacar // 20
    sacar %= 20

    nota10 = sacar // 10
    sacar %= 10

    nota1 = sacar // 1
    sacar %= 1

    break

print("IMPRIMINDO...")
print(f"{nota50} NOTA(s) DE 50")
print(f"{nota20} NOTA(S) DE 20")
print(f"{nota10} NOTA(S) DE 10")
print(f"{nota1} NOTA(S) DE 1")
