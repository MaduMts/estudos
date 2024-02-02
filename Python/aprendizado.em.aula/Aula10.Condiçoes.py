      # Aula 10 - Condições

print('Nesta aula vamos ver as condições do "if" e "else"')

print('CONDIÇÕES SIMPLES:')
print('A condição simples é aquela que utiliza apenas o "if" \n EXEMPLO:')
no = str(input('Qual o seu nome?'))
if no == 'maria':
  print('que nome lindo você tem!')
print('Bom dia, {}!'.format(no))
print('')

print('CONDIÇÃO COMPOSTA:')
print('A condição composta é quando utilizamos o "if" e o "else" \n EXEMPLO:')
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('digite a sugunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
  print('Sua média foi boa! PARABÉNS!')
else:
  print('Sua média foi ruim! ESTUDE MAIS!')
print('')

print('CONDIÇÃO SIMPLIFICADA:')
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!')
