# If-else-elif
# sintaxe 
# O que é uma condição no código?
    # Uma expressão que retorna um booleano
    # = é usado para atribuição 
    # == é usado para comparação
    # resultado = 1 ==1
        # retorna true e é do tipo booleano
# Tipo booleano 
# Ordem das condições 
# Combinação entre condições 

notas = []

nota_matematica = float(input("Nota de matemática: "))
notas.append(nota_matematica)

nota_quimica = float(input("Nota de quimica: "))
notas.append(nota_quimica)

nota_fisica = float(input("Nota de fisica: "))
notas.append(nota_fisica)

media = sum(notas) / len(notas)

# Condição
    # limite nota inferior = 7 
    # recuperação entre 5 e 6.9
    # abaixo disso reprovação

if 7 <= media:                    # A inversão da ordem aqui não altera, é mais sobre a legibilidade
    print("Aluno Aprovado")
elif 5 <= media:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado!")