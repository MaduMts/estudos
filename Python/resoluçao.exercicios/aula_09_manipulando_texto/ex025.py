            # *AULA O9 EXERCICIO 25*
      # *Procurando uma string dentro de outra*

#Crie um programa que leia o nome de uma pessoa e diga se 
#ela tem “SILVA” no nome.

nome = str(input('Escreva o seu nome completo:')).strip()
print('Existe "Silva" no seu nome? {}'.format('silva' in nome.lower()))