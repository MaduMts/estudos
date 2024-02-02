#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

print('{:=^50}'.format('COMPRAS')) # {:=^50} - config para deixar algo centralizado
valorproduto = float(input('Qual o valor do produto?R$'))
a = valorproduto - (valorproduto * 0.10)
b = valorproduto - (valorproduto * 0.05)
c = valorproduto
d = valorproduto * 1.20

print(''' FORMAS DE PAGAMENTO:
[ a ]- à vista dinheiro/cheque com 10% de desconto
[ b ] - à vista no cartão com 5% de desconto
[ c ] - em até 2x no cartão, preço formal 
[ d ] - 3x ou mais no cartão: 20% de juros''') # ''' - para um codigo que usa mais de uma linha

forma_pagamento = input('Qual sua forma de pagamento? a, b, c ou d?')

if forma_pagamento == 'a':
    print('O valor final ficou de R${:.2f}'.format(a))
elif forma_pagamento == 'b':
    print('O valor final ficou de R${:.2f}'.format(b))
elif forma_pagamento == 'c':
    print('O valor final ficou de R${:.2f}'.format(c))
elif forma_pagamento == 'd':
    parcela = int(input('Em quantas vezes você pretende pagar?'))
    print('O valor final ficou de R${:.2f} por {} meses.'.format(d / parcela, parcela))
else:
    print('Opção inválida!')
    
print('Volte sempre!!')
print(50 * '=')
