# Modifique o programa acima para calcular a média ponderada e imprima-a a na tela. Considerar os seguintes pesos:
    # Matemática -> peso 3 
    # Física -> peso 3 
    # Química ->  peso 3
    # Biologia -> peso 2 
    # Geografia -> peso 1

PESO_MATEMATICA = 3 
PESO_FISICA = 3
PESO_BIOLOGIA = 2 
PESO_GEOGRAFIA = 1 

Notas = []
Pesos = (PESO_MATEMATICA, PESO_FISICA, PESO_BIOLOGIA, PESO_GEOGRAFIA)

notaMatematica = input('Digite a nota de matemática')
Notas.append(notaMatematica)

notaFisica = input('Digite a nota de Fisica')
Notas.append(notaFisica)

notaBiologia = input('Digite a nota de Biologia')
Notas.append(notaBiologia)

notaGeografia = input('Digite a nota de Geografia')
Notas.append(notaGeografia)

print(Notas)

#fazer um dicionario para cada 
