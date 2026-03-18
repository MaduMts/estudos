#               EXERCICIO 59: 
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

print(40 * "=")
print(13*" ", "CALCULADORA")
print(40 * "=")


num = int(input("Digite um numero:"))
num2 = int(input("Digite o segundo numero:"))

while True:

    print(18*"=", "MENU", 18*"=")
    print("[ 1 ] somar")
    print("[ 2 ] multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")

    opcao = int(input("O´que você quer fazer com os dois numeros?"))

    if opcao == 1:
        print(f"A soma entre {num} e {num2} é: {num + num2}")

    elif opcao == 2:
        print(f"A multiplicação entre {num} e {num2} é: {num * num2}")

    elif opcao == 3:
        if num == num2:
            print("Os dois números são iguais")
        else:
            print(f"O maior número entre {num} e {num2} é: {max(num, num2)}")

    elif opcao == 4:
        num = int(input("Digite um novo numero:"))
        num2 = int(input("Digite o segundo numero:"))

    elif opcao == 5:
        print("Até a proxima!!")
        break

    else:
        print(f"Opção invalida")
    