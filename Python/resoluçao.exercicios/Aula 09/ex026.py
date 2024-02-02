            # *AULA O9 EXERCICIO 26*
      # *Primeira e última ocorrencia de uma string*

# Faça um programa que leia uma frase pelo teclado e:
# *mostre quantas vezes aparece a letra “A”, 
# *Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase:')).lower().strip()
print('A letra "a" aparece {} vezes.'.format(frase.count('a')+1))
print('O primeiro "a" está na posição: {}'.format(frase.find('a')+1))
print('O ultimo "a" está na posição: {}'.format(frase.rfind('a')+1))
