#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
                

n1 = int(input('Digite um numero?'))
n2 = int(input('Digite outro numero?'))
if n1 < n2: 
    print('O primeiro numero {} é menor que o segundo numero {}!'.format(n1,n2))
elif n1 > n2:
    print('O primeiro numero {} é maior que o segundo numero {}!'.format(n1,n2))
else:
    print('Os numeros {} e {} são iguais!'.format(n1,n2))
print('Obrigada por jogar!!')
