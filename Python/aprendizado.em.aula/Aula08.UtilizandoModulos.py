#APRENDIZADO REFERENTE A 08

print('=' * 120)
print('')

print('MODULOS/BIBLIOTECAS:')
print('')

print('MODULOS: são extensões da linguagem, utilizados para facilitar o desenvolvimento. temos diversos tipo de modulos.')
print('')

print('BIBLIOTECAS:São conjuntos de módulos relacionados que são organizados para atender a um propósito específico. Em outras palavras, uma biblioteca é uma coleção de módulos que fornecem funcionalidades para resolver problemas ou realizar tarefas específicas.')
print('')

print('PS: Para usar esses modulos usamos a ferramneta *import*')
print('')

print('Exemplo de modulos da biblioteca Numeric and Mathematical Modules:')
print('')

print('01 - MATH:')
print('Math é um exemplo de modulo contendo funções matematicas. Dentro deste modulo temos as funções: \n CEIL: Arredonda N° para cima \n FLOOR: Arrendonda N° para baixo \n TRUNC: Elimina da virgula para frente \n POW: Funciona como exponenciação \n SQRT: Funciona como uma raiz quadrada\n fACTORIL: Fatora um N° \n E assim vai... \n EXEMPLO:')
import math  
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Para importar uma ferramenta expecifica da biblioteca MATH:
'''from math import sqrt, floor
num = int(input('digite um numero?'))
raiz = sqrt(num)
print('A raiz de { é igual a {:;2f}}'.format(nu, floor(raiz)))'''
print('')

print('02 - RANDOM')
print('O Random tambem é um modulo da biblioteca Numeric and Mathematical Modules. A função deste modulo é sortear N° aleatorio. \n EXEMPLO:')
import random
num = random.random() #Assim gera um numero aleatorio entre 0 e 1
print(num)
# Para gerar um numero inteiro basta usar o *num = random.randint(1, 10)*
print('')

print('Mas não fica só por isso, podemos importar modulos de pessoas que programam por conta propria, esses modulos são chamados de "PyPi", basta acessar o site "python.org" para achar diversos modulos "PyPi". \n Segue exemplo de como importa-las:')
# No visual Studio Code basta digitar "CMD" no iniciar do windowns para abrir o prompt de comando, logo em seguida basta digitar "pip install + o nome do modulo". Depois use o "import" no VSC para para importar o modulo PyPi desejado
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print('')

print('=' * 120)