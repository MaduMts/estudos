#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = float(input('Primeiro lado:'))
b = float(input('Segundo lado:'))
c = float(input('Terceiro lado:'))

if a + b >= c and a + c >= b and b + c >= a:
  print('Com esses valores você pode formar um triangulo!!')
  if a == b == c:
    print('O seu triangulo é EQUILÁTERO: todos os lados iguais')
  elif a == b or a == c or b == c:
    print('O seu triangulo é ISÓSCELES: dois lados iguais, um diferente')
  else:
    print('O seu triangulo é ESCALENO: todos os lados diferentes')
else:
  print('Infelizmente voce não pode formar um triangulo!!')
  
print('Volte sempre!!')