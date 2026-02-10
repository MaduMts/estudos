            #Exercício 054: 
#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

#MINHA RESOLUÇÃO:
from datetime import date #importando a biblioteca de tempo para usar na linha 9

for pessoa in range(1,8):
    anonasc = int(input(f"{pessoa}° pessoa, qual o ano do seu nascimento?"))
    if date.today().year - anonasc >= 18:
        print(pessoa,"° pessoa é maior de 18 anos")
    else:
        print(pessoa,"° pessoa não é maior de 18 anos")
