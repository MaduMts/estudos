            #EXERCICIO 056 
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: 
#- A média de idade do grupo 
#- Qual é o nome do homem mais velho
#- Quantas mulheres têm menos de 20 anos.


#MINHA RESOLUÇÃO:

#Solução média do grupo:
soma_idade = 0

#Solução nome do homem mais velho:
maior_idade = 0
nome_homem = ''

#Solução Quantas mulher com menos de 20 anos:
cont_mulher = 0


for pessoa in range (1,3):
    print(f"{20*"="} CADASTRO {pessoa}° PESSOA {20*"="}")

    nome = input("NOME:")
    idade = int(input("IDADE:"))
    sexo = input("SEXO: (F/M)").lower()

    print(60*"=")

    #Solução média do grupo:
    soma_idade += idade

    
    #Solução nome do homem mais velho:
    if sexo == "m":
        if idade > maior_idade:
            maior_idade = idade  
            nome_homem = nome
    

    #Solução Quantas mulher com menos de 20 anos:
    if sexo == "f" and idade < 20:
        cont_mulher += 1

#Solução média do grupo:
media = soma_idade/pessoa
 
print(f"A média do grupo é: {media}")
print(f"O nome do homem mais velho é: {nome_homem}")
print(f"Existem {cont_mulher} mulheres com menos de 20 anos!")
    