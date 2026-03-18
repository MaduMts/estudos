#           EXERCICIO 73 

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

#Obs: Como a CHapecoense não está localizada nesta tabela, optei por localizar o santos.

brasileirao = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirasol', 'Fluminense', 'Botafogo', 'Bahia', 
              'São Paulo', 'Gremio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco'
              'EC Vitoria', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport Recife')

print("Os 5 primeiors times que estão na tabela do brasilerão 2025 são:")
print(f"1° {brasileirao[0]}")
print(f"2° {brasileirao[1]}")
print(f"3° {brasileirao[2]}")
print(f"4° {brasileirao[3]}")
print(f"5° {brasileirao[4]}")
print("\n")

print("Os últimos 4 colocados são:")
print(f"17° {brasileirao[15]}")
print(f"18° {brasileirao[16]}")
print(f"19° {brasileirao[17]}")
print(f"20° {brasileirao[18]}")
print("\n")

print("A tabela do brasileirão em ordem alfabetica é:")
print(sorted(brasileirao))
print("\n")

print(f"O Santos está na {brasileirao.index("Santos") + 1}° posição da tabela")
