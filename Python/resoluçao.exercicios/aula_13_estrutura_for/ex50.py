            #EXERCICIO 50 
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.

#Minha resolução:
#numeros = []
#soma = 0

#for n in range(0,6):
#    n = int(input("Digite um numero:"))
#    numeros.append(n)
#print("Você digitou os numeros:", numeros)

#for num in numeros:
#    if num % 2 == 0:
#        soma = soma + num
#print("E a soma entre os numeros pares é:", soma)


#RESOLUÇÃO DO PROFESSOR:
soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1       
print(f"Os numeros pares são: {cont} e a soma entre eles é: {soma}")
