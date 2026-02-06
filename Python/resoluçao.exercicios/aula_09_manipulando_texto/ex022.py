            # *AULA O9 EXERCICIO 22*
            # *ANALISADOR DE TEXTO*

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
 
nome = str(input('Qual o seu nome?')).strip() # pedi para não contar os espaços dado no começo e no final
print('Seu nome maiusculo é:{}'.format(nome.upper()))
print('Seu nome em minusculo é:{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#O ultimo exercicio pode ser feito de duas formas:
# Modo 01
print('Seu primeiro nome tem {} letras:'.format(nome.find(' '))) #codigo manda procurar o primeiro espaço.

#Modo 02
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0]))) #Manda ler o primeiro bloco do nome splitado
