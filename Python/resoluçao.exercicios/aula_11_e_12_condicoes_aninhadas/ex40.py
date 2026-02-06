#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

n1 = float(input('qual foi a nota da primeira prova?'))
n2 = float(input('Qual foi a nota da segunda prova?'))
m = (n1 + n2) / 2
print('Sua média foi de: {}'.format(m))
if m < 5.0:
    print('Você foi REPROVADO!')
elif m >= 5.0 and m <= 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('você está APROVADO!')
print('Volte sempre!!')
    