

#APRENDIZADO REFERENTE AS AULAS 01 a 07 do curso em video de Gustavo Guanabara:
    
    #sobre tipos primitivos:
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
 

    #Sobre Operadores:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
svezes = n1 * n2
sdivisao = n1 / n2
sdivisaoi = n1 // n2
sdivisaor = n1 % n2
sexponente = n1 ** n2
print('='*40)
print('A soma é: \n {}'.format(n1+n2)) #Desta forma não precisa criar uma variavel para a soma.
print('='*40) # podemos multiplicar strings 
print('A subtração é: \n {}'.format(n1-n2)) #Cria-se uma variavel apenas se for utilizalá para algo posteriormente.
print('='*40)
print('A multiplicação entre {} e {} é: \n {}'.format(n1, n2, svezes)) #Exemplo criando uma variavel
print('='*40)
print('A divisao entre {} e {} é: \n {}'.format(n1, n2, sdivisao))
print('='*40)
print('A divisão inteira entre {} e {} é: \n {}'.format(n1, n2, sdivisaoi))
print('='*40)
print('O resto da divisao entre {} e {} é: \n {}'.format(n1, n2, sdivisaor))
print('='*40)
print('A exponenciação entre {} e {} é: \n {}'.format(n1, n2, sexponente))
print('='*40)

#  *INFORMAÇÕES IMPORTANTES*

# \n  - é usada para pular uma linha no print
#  =  - significa que um alemento RECEBE algo
# == - Significa o resultado

#Ordem de precedencia da programação (oque DEVE ser calculado primeiro no algoritimo):
#01 - ()  {parenteses}
#02 - **  {Exponenciação}
#03 - *  /  //  %  {Multiplicação, Divisao, Divisao inteira, e Resto da divisao}
#04 - +  -  {Mais, Menos}