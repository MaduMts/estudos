      #AULA 10 EXERCICIO 35 
      #Analisando Triângulo v1.0

# Desenvolva um programa que leia o comprimento de três retas e 
#diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeiro lado:'))
b = float(input('Segundo lado:'))
c = float(input('Terceiro lado:'))
if a + b >= c and a + c >= b and b + c >= a:
  print('Com esses valores você pode formar um triangulo')
else:
  print('Infelizmente voce não pode formar um triangulo.')
  