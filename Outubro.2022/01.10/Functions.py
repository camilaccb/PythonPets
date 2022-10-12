# Funções 
    # Sintaxe 
    # Argumentos 
    # Retorno ou não retorno. O questionamento é: vou precisar ou não dessa variável depois
    # Boas práticas (como documentar)
# Todo método é uma função. É uma função atrelada a um tipo de objeto
# Nem toda função é um método. Função é genérica 


notas = [] #lista
nota1 = int(input("Digite a primeira nota: "))
notas.append(nota1)

nota2 = int(input("Digite a segunda nota: "))
notas.append(nota2)

nota3 = int(input("Digite a terceira nota: "))
notas.append(nota3)

media = sum(notas)/len(notas)

print(f"A média final é {media}")

# funções: int, input, sum, len


