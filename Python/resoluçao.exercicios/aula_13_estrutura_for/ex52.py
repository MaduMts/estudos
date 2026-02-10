        #Exercício 052
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#numero primo = dividido por 1 e por ele mesmo

num = int(input("Digite um numero inteiro:"))
contador = 0

for n in range(1,num + 1):
    if num % n == 0:
        contador +=1

if contador == 2:
    print("O numero", num, "é primo!")
else:
    print("O numero", num, "não é primo!")
