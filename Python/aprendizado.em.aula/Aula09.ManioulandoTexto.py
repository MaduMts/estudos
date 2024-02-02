      # Aula 09 - Manipulando strings

print('As strings quando colocadas dentro de variáveis acabam ocupando mini espaços na memória numerados crescentemente de 0 até o final da frase contando os espaços.')
print('Exemplo:')
print('')

frase = 'Curso em vídeo python'
print(frase)
print('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20')
print('')

print('Agora vamos as formas de manipulação da string:')
print('')

print('*Fatiamento:')
print('Dentro dos [] adicionamos em ordem onde queremos começar, onde termina, e de quantas casas pulamos. EXEMPLO:')
print(frase[1:13]) 
print(frase[1:13:2])
print(frase[:13])
print(frase[1:])
print(frase[1::2])
print('')

print('*Análise:')
print('Podemos buscar algumas informações da string como: seu comprimento, qual letra começa ou termina, e etc… EXEMPLO:')
print(len(frase)) #Informa o comprimento em caracteres.
print(frase.count('o')) #Quantas vezes aparece o "o",
print(frase.count('o',0,13)) #Entre 0 e 13.
print(frase.find('deo')) #Onde começa o "deo".
print(frase.rfind('deo')) #Onde começa o "deo" da direita para a esquerda.
print('curso' in frase) #Informa se existe "curso" dentro da variável "frase".
print('')

print('*Transformação:')
print('podemos moldar as strings através de métodos:')
print(frase.replace('python','android')) #Troca o python por Android.
print(frase.upper()) #Deixa tudo em maiúsculo.
print(frase.lower()) #Deixa tudo em minúsculo. 
print(frase.capitalize()) #Deixa apenas a primeira letra em maiúsculo.
print(frase.title()) #Deixa toda palavra com a 1° letra maiúscula.
frase.strip() #Remove espaços inúteis no começo e no final
frase.rstrip() #Remove apenas os espaços da direita.
frase.lstrip() #Remove apenas os espaços da esquerda.
print('')

print('*Divisão/Junção')
print('Podemos dividir strings em elementos. Cada palavra vira 1 elemento com numeração de 0 a fim da palavra.EXEMPLO:')
dividido = frase.split()
print(dividido[2] [3]) #Mostrar no 2° elemento qual é a 3° letra. 
print('')

print('Podemos colocar letras/símbolos no lugar dos espaços . EXEMPLO:')
print('-'.join(frase))