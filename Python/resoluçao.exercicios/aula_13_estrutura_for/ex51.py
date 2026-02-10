            #Exercício 051
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.

#LEMBRETE:
#PRIMEIRO TERMO: Começa de onde
#RAZAO: + esse numero

#MINHA RESOLUÇÃO:
print("="*40)
print("10 TERMOS DE UMA PA")
print("="*40)


print("Vamos fazer uma Progressão aritmética?")
primeirotermo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão:"))

print("Os 10 termos de sua PA são:")
for c in range(1,11):
    primeirotermo += razao
    print(primeirotermo)
print("="*40)



#RESOLUÇÃO DO PROFESSOR:   
#logica aplicada: pa = (p+(10-1)*r)+r

primeiro = int(input('primeiro termo:'))
razão = int(input('razão:'))
décimo = primeiro + (10 - 1) * razão

for c in range (primeiro, décimo + razão, razão):
    print(c, end=' → ')
print("ACABOU!!")
