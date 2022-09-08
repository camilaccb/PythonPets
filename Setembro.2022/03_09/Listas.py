#Listas: [1,2,3,4,"6"] 
 #Armazenam vários objetos
 #É possível misturar diferentes tipos de dados dentro da lista
#Empacontamento /desempacotamento

# Listas
nome = "CAMILA CALDAS CORREIA BORGES"
outra_estrutura = nome.split() # retorna uma lista
print(type(outra_estrutura))

print(outra_estrutura)

#Pegando um pedaço da lista
#Indexação em python começa por 0
print(outra_estrutura[0]) #Colchete de fateamento
print(outra_estrutura[0:2]) #Pega até o elemento de indexação 1, não é inclusivo
print(outra_estrutura[-1]) # Indexação reversa (da direita para a esquerda)

#Manipular uma lista - Inserir, modificar, remover 
# Métodos de inserção

outra_estrutura.append("Lira") # Inclui um único elemento no final da lista
print(outra_estrutura)

outra_estrutura.extend("Lira") # Inclui cada caractere da string no final da lista (elemento iterável), só é válido para adicionar string
print(outra_estrutura)

outra_estrutura.insert(0,"Maria") # Insere um único elemento numa determinada posição(um de cada vez)
print(outra_estrutura)

outra_estrutura_copia = outra_estrutura.copy()

#Métodos de reordenação

outra_estrutura.reverse() # Espelha
outra_estrutura.sort() # Ordena de acordo com algum parâmetro

#Métodos de deleção

outra_estrutura.clear() #Limpa toda a lista
outra_estrutura.pop(0) # Remove o último elemento da lista por default se não inserido nenhum parâmetro, baseado em índice, o retorno pode ser armazenado numa variável (por definição da documentação), diferentemente do remove
valor_armazenado_pop = outra_estrutura.pop(0)
print(valor_armazenado_pop) #Armazenou numa variável o valor que foi removido
del outra_estrutura[0] # mesmo efeito de fazer um pop, mas também não pode ser armazenado numa variável 
outra_estrutura.remove("Caldas") # Baseado em posição, remove o elemento 

# Método index - buscador
indice = outra_estrutura.index("CAMILA")
print(indice)

# Método count - conta o número de vezes que um objeto aparece na lista
outra_estrutura.count("CAMILA")

# Função len - não é um método mas sim uma função. Um método é atrelado a um determinado objeto. 
len(outra_estrutura)





