#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

anoatual = int(input('Qual é o ano atual?'))
anonasc = int(input('Qual o seu ano de nascimento?'))
idade = anoatual - anonasc
print('Sua idade é: {}'.format(idade))

if idade <= 9:
    print('Sua categoria é a: Mirim!!')
elif idade >= 10 and idade <= 14:
    print('Sua categoria é a: Infantil!!')
elif idade >= 15 and idade <= 19:
    print('Sua categoria é a: Junior!!')
elif idade >= 20 and idade <= 25:
    print('Sua categoria é a: Senior!!')
else:
    print('Sua categoria é a: Master!!')