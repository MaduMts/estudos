#Exercício 048 
#Faça um programa que calcule a soma entre todos os números que são 
#múltiplos de três e que se encontram no intervalo de 1 até 500.


#MINHA RESOLUÇÃO:
#listamultiplos = []
#for n3 in range(0, 501):
#    if n3 % 3 == 0:
#        listamultiplos.append(n3)

#print("Os numeros multiplos de 3 são:")
#print(listamultiplos)


#soma = 0
#for multiplos3 in listamultiplos:
#    soma = soma + multiplos3

#print("E a soma entre eles é:")
#print(soma)

#RESOLUÇÃO DO PROFESSOR:
soma = 0
cont = 0

for n3 in range(0, 501):
    if n3 % 3 == 0:
        cont = cont + 1 #Quantos numeros foram somados
        soma = soma + n3

print(cont)
print(soma)
