

#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anoatual = int(input('Qual o ano atual?'))
anon = int(input('Qual o seu ano de nascimento? aaaa'))
idade = anoatual - anon

print('Quem nasceu em {} tem {} anos em {}!'.format(anon,idade,anoatual))

if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento!'.format(18 - idade))
    print('Seu alistamento será em {}!'.format(anoatual + (18 - idade)))

elif idade > 18:
    print('Passou {} anos da data do seu alistamento!'.format(idade - 18))
    print('Seu alistamentos era pra ter sido no ano: {}!'.format(anoatual - (idade - 18)))

else:
    print('Está na data do seu alistamento, entre no site e faça sua avaliação!')
print('Volte sempre!')
