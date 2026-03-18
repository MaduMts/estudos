        #EXERCICIO 046
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for cont in range(10, 0, -1):
   sleep(0.5)
   print(cont)
print ("BUUUM!! FOGOS!! KABUM!!")


contador = 11

while contador >= 1:
    contador = contador - 1 
    
    sleep(0.5)
    print(contador)
 

print("BUUUM!! FOGOS!! KABUM!!")  