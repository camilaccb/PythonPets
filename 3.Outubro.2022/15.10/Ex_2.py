
notas = []

qtd_notas = 5

for indice in range( qtd_notas):
    nota = int(input(f"Digite uma nota {indice+ 1}: "))
    notas.append(nota)

media = sum(notas)/len(notas)

print(f"A média final é {media}")


# 2 forma de fazer 

notas = []

qtd_notas = 5

for indice in range( 1, qtd_notas + 1): # 1 até 11 (11 não inclui)
    nota = int(input(f"Digite uma nota {indice}: "))
    notas.append(nota)

media = sum(notas)/len(notas)

print(f"A média final é {media}")

