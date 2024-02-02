            # *AULA O9 EXERCICIO 27*
      # *Primeira e última ocorrencia de uma string*

#Faça um programa que leia o nome completo de uma pessoa, mostrando 
#em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo:')).strip().split()
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu ultimo nome é: {}'.format(nome[-1])) #O "-1" se refere ao ultimo elemento de uma lista
