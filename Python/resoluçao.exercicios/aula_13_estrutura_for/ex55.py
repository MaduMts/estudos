            #EXERCICIO 055
#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos

#MINHA RESOLUÇÃO:
pesos = []

for pessoa in range(1,6):
    peso = float(input(f"{pessoa}° pessoa, qual o seu peso?"))
    pesos.append(peso)

print(f"O maior peso entre as pessoas é: {max(pesos)}Kg")
print(f"O menor peso entre as pessoas é: {min(pesos)}Kg")


#RESOLUÇÃO DO PROFESSOR:
maior = 0
menor = 0

for p in range(1,6):
    peso2 = float(input(f"peso da {p}° pessoa:"))
    if p == 1:
        maior = peso2
        menor = peso2
    else:
        if peso2 > maior:
            maior = peso2
        if peso2 < menor:
            menor = peso 
print(f"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")
