#EXERCICIO 60: 
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um numero para ver o seu fatorial: "))
resultado = 1

while num > 0:
    resultado *= num
    num -= 1

print(f"O fatorial do numero digitado é: {resultado}")
