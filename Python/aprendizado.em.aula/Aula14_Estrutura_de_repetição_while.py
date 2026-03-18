#                  ****ESTRUTURA DE REPETIÇÃO WHILE****

# While é uma estrutura de repetição usada quando
# NÃO sabemos quantas vezes o loop vai executar,
# pois ele depende de uma condição lógica.
   
#       🎯 REGRA DE OURO PARA USAR 
# O while só roda quando a condição é **TRUE**.
     
#       🎯 CONCEITO IMPORTANTE
#Toda validação pode ser pensada de duas formas:
# - Repetir enquanto estiver errado
# - Repetir até ficar certo


# Vamos ver na pratica suas variações:
# Usando um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


            #EXEMPLO 01 - basico(while and)

#É Mais usado quando:
# - Exercício é simples
# - Validações diretas
# - Condição clara e pequena
# - Quando você já tem o valor antes do loop

# Característica:
#O controle está na entrada do loop.
#Ele só entra se estiver errado.

# Ideal para:
#Listas de exercício
#Primeiros contatos com while
#Quando a condição é simples

sexo = input("Qual o seu sexo?(M/F)").strip().upper()

while sexo != "M" and sexo != "F":  #obs: quando entra o valor que precisamos (M ou F), o while se torna falso, saindo assim do looping.
    sexo = input("Valor inválido! Digite apenas M ou F: ").strip().upper()

if sexo == "M":
    print("Sexo masculino cadastrado com sucesso!")
else:
    print("Sexo feminino cadastrado com sucesso!")




            #EXEMPLO 02 - intermediario(while not)

#Mais usado quando:
# - Você quer trabalhar melhor lógica booleana
# - Está estudando Leis de De Morgan
# - Precisa inverter uma condição maior

#Característica:
#É logicamente equivalente ao AND anterior.
#É mais uma questão de treinar lógica do que necessidade prática.

#Ideal para:
#Aprender manipulação de lógica
#Melhorar raciocínio booleano
#Situações onde já existe uma condição positiva e você quer negar     
sexo2 = input("Qual o seu sexo?(M/F)").strip().upper()

while not (sexo2 == "M" or sexo2 == "F"): #obs: o not está invertendo a condição, então quando m ou f entram, vira true e not transforma em false, saindo assim do lopping.
    sexo2 = input("Valor inválido! Digite apenas M ou F: ").strip().upper()

print("Sexo registrado com sucesso!")




            #EXEMPLO 03 - Mais usado(while true)
  
#Mais usado quando:
# - Criando menus
# - Sistemas interativos
# - Fluxos maiores
# - Muitas validações diferentes
# - Sistemas que precisam sair por múltiplos motivos

#Por que ele é tão usado em sistemas reais?#Porque ele permite:
#Múltiplas saídas (break em lugares diferentes)
#Código mais organizado
#Fluxo mais flexível
#Tratamento de erros mais detalhado

while True:
    sexo3 = input("Qual o seu sexo? (M/F): ").strip().upper()

    if sexo3 in ("M", "F"):
        print("Parabens! Sexo registrado com sucesso!")
        break
    
    print("Valor inválido! Digite apenas M ou F.")




#       RESUMO FINAL:
# while condição → controla a entrada do loop
# while True → controla a saída do loop
