
# Set também determinado por chaves
# O set não tem posições definidas 
# Se torna interesante quando queremos comparar elementos
    # Relação com a teoria dos conjuntos    
# Uma lista que armazena posições


lista: list[int] = [1,1,2,2,2,3,4,4,5,6,7,8]

conjunto = set(lista)
#print(conjunto) # remove as duplicatas 

nome = "Camila Caldas Correia Borges" 
letras = set(nome)
#print(letras)

print(conjunto.intersection(letras)) # acho que vai dar um erro porque os sets são diferentes 
#interseção
#união 
#diferença -> a ordem importa
#diferença simétrica  
# método 1 = método 2 (retorna é um booleano )

print(dir(conjunto)) # consultar os métodos de um determinado objeto

#len(lista_produto) = len(set(lista_produtos)) exemplo do mundo real 