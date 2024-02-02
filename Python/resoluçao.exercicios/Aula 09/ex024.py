            # *AULA O9 EXERCICIO 24*
    # *Verificando as primeiras letras de um texto*

#Crie um programa que leia o nome de uma cidade diga se 
#ela começa ou não com o nome “SANTO”

cid = str(input('Qual a cidade você mora?')).strip()
print(cid[:5].lower() == 'santo')
