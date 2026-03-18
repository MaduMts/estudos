#               EXERCICIO 057 
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Qual o seu sexo?(M/F)").strip().upper()

while sexo != "M" and sexo != "F":  #obs: quando entra o valor que precisamos (M ou F), o while se torna falso, saindo assim do looping.
    sexo = input("Valor inválido! Digite apenas M ou F: ").strip().upper()

if sexo == "M":
    print("Sexo masculino cadastrado com sucesso!")
else:
    print("Sexo feminino cadastrado com sucesso!")

