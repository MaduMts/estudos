                #EMPRESTIMO 02

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário 
# ou então o empréstimo será negado.

valorcasa = float(input('Qual o valor da casa que voce deseja comprar?'))
salario = float(input('Quanto você recebe?'))
pagamento = int(input('Em quantas vezes voce pretente pagar?'))
valormes = valorcasa / pagamento

if valormes > 0.30 * salario:
    print('Infelizmente esse emprestimo consome mais de 30% do seu salario mensal e por isso seu credito não foi aprovado')
else:
    print('Seu emprestimo foi APROVADO e ficou em R${} por mês'.format(valormes))
    