
#Aprendendo a usar if/elif/else:

print('Aqui deixamos um exemplo de condições aninhadas:')

nome = str(input('Qual o seu nome?')).capitalize()
if nome == 'Maria':
    print('Que nome bonito você tem!')
elif nome == 'Pedro' or nome == 'Lucas' or nome == 'Gabriel':
    print('No Brasil o seu nome é bem popular')
elif nome in 'Ana claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Nada demais!')
print('Tenha um Bom dia, {}!'.format(nome))
