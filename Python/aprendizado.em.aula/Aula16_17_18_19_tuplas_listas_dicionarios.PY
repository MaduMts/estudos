"""     
             LISTAS, TUPLAS E DICIONÁRIOS

São estruturas usadas para armazenar múltiplos valores
Mas cada uma tem um objetivo e comportamento diferente.

**🎯 REGRA DE OURO PARA ESCOLHER**

Lista → quando os dados PODEM mudar
Tupla → quando os dados NÃO DEVEM mudar
Dicionário → quando você precisa associar CHAVE e VALOR      


️1 - LISTA [list]

Lista é uma estrutura:
- Ordenada
- Mutável (pode alterar)
- Permite valores repetidos
- Usa índice numérico

Ideal para:
Notas de alunos
Carrinho de compras
Resultados de cálculos
Armazenar entradas do usuário

É criada com colchetes []""" 
#EXEMPLO DE LISTA:
#  SISTEMA DE NOTAS (usando LISTA)  
notas = []

print("Digite 5 notas do aluno:")

for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

print("\nNotas cadastradas:", notas)

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")



"""     2 - TUPLA (tuple)

Tupla é uma estrutura:
- Ordenada
- Imutável (NÃO pode alterar)
- Permite repetição
- Usa índice numérico

Mais usada quando:
- Os dados são fixos
- Você quer segurança
- Representa algo que não deve mudar
É criada com parênteses ()"""
#EXEMPLO DE TUPLA
#SORTEIO (usando TUPLA)

import random

numeros = tuple(sorted(random.sample(range(1, 61), 6)))

print("Números sorteados:")
print(numeros)

print("\nPrimeiro número sorteado:", numeros[0])



"""     3 - DICIONÁRIO {dict}
Dicionário é uma estrutura:
- Mutável
- Organizada por chave:valor
- Não usa índice numérico
- Acessa pelo nome da chave
É criado com chaves {}

Mais usado quando:
- Você precisa dar nome para cada valor
- Está modelando algo mais real
- Trabalhando com cadastro
- Quer dados organizados"""
#EXEMPLO DE DICIONARIO
#CADASTRO DE USUÁRIO (usando DICIONÁRIO)==

usuario = {}

usuario["nome"] = input("Digite seu nome: ")
usuario["idade"] = int(input("Digite sua idade: "))
usuario["email"] = input("Digite seu email: ")

print("\n===== DADOS CADASTRADOS =====")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")

if usuario["idade"] >= 18:
    print("Status: Maior de idade")
else:
    print("Status: Menor de idade")
    
