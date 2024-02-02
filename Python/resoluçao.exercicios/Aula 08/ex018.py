            # *AULA O8 EXERCICIO 18*
            # *SENO, COSSENO E TANGENTE*

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = math.radians(float(input('digite o valor em angulo?')))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O valor de seno é: {:.2f}'.format(seno))
print('O valor de cosseno é: {:.2f}'.format(cosseno))
print('O valor de tangente é: {:.2f}'.format(tangente))
