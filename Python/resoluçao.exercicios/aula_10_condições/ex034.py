      #AULA 10 EXERCICIO 34 
      #Aumentos múltiplos

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
#o aumento é de 15%.

salario = float(input('Qual o seu salario?R$'))
if salario <= 1250.00:
  print('Seu salario com 15% de reajuste é:R${:.2f}'.format(salario + (salario * 15 / 100)))
else:
  print('Seu salario com 10% de reajuste é:R${:.2f}'.format(salario + (salario * 10 / 100)))