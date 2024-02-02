      #AULA 10 EXERCICIO 29
      #RADAR ELETRONICO

# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
carro = int(input('Quantos km o seu carro estava?'))
print('PROCESSANDO...')
sleep(2)
if carro > 80:
  print('VOCE FOI MULTADO!! A multa foi no valor de: {:.2f}'.format(carro * 7,00)) 
print('Muito bem!! Continue andando na velocidade.')