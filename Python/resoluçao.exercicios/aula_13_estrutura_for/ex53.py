        #Exercício 053
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços.

#Minha Resolução:
frase = input("Digite uma frase:").lower().replace(" ","")

frase_invertida = frase[::-1]

if frase_invertida == frase:
    print("Isso é um palindro:", frase_invertida )
else:
    print("Isso não é um palindro:", frase_invertida)


#Resolução do professor:
frase = input("Digite uma frase: ").lower().replace(" ", "")

invertida = ""

for i in range(len(frase) - 1, -1, -1):
    invertida += frase[i]

if invertida == frase:
    print("Isso é um palíndromo!")
else:
    print("Isso não é um palíndromo!")
