#              EXERCICIO 67
# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 


#MINHA RESOLUÇÃO:
print(40 * "=")
print(13*" ", "CALCULADORA")
print(40 * "=")

multiplicador = 0

num = int(input("Digite um numero inteiro para ver sua tabuada:"))

while True:
    if num < 0:
        break

    multiplicador += 1
    print(f"{num} x {multiplicador} = {num * multiplicador}")
    

    if multiplicador == 10:
        multiplicador = 0
        print( 93 * "=")
        num = int(input("Digite OUTRO numero para ver sua tabuada:"))
    
print("PROGRAMA ENCERRADO!!")
    
  



#RESOLUÇÃO DO PROFESSOR:
while True:
    n = int(input("Quer ver a tabuada de qual valor?"))
    print("-" * 30)

    if n < 0:
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
    print("-" * 30)

print("TABUADA ENCERRADO. VOLTE SEMPRE!")
