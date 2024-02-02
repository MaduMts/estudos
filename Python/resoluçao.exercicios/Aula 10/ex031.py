      #AULA 10 EXERCICIO 31
      #Custo da Viagem

# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep
viagem = float(input('Qual a distancia da viagem em km?'))
print('PROCESSANDO...')
sleep(1)
if viagem > 200:
  print('Sua passagem irá custar:R$ {:.2f}'.format(viagem * 0.45))
else:
  print('Sua passagem irá custar:R$ {:.2f}'.format(viagem * 0.50))
