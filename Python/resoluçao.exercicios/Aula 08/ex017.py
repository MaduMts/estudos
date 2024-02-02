            # *AULA O8 EXERCICIO 17*
            # *CATETOS E HIPOTENUSA*
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# MODO 1
oposto = float(input('Qual o valor do cateto oposto?'))
adjacente = float(input('Qual o valor do cateto adjacente?'))
print('O valor da hipotenusa será de: {:.2f}'.format((oposto ** 2 + adjacente ** 2) ** (1/2)))

# MODO 2 
import math
oposto2 = float(input('Qual outro valor do cateto oposto?'))
adjacente2 = float(input('Qual outro valor do cateto adjacente?'))
hipotenusa = math.hypot(oposto2, adjacente2)
print('O valor da hipotenusa será de: {:.2f}'.format(hipotenusa))
