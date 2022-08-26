#Lista
# É uma estrutura de dados que é possivel armazenar muitas coisas (vários itens)
# A lista também é um objeto
# Indexação no python começa com 0 

lista = [1,2,3,4,5,6,7,8]
string = "Camila Caldas Correia Borges"

print(type(lista))
print (lista[2])
print(string[2]) # colchete slice

# start:stop:step
# O último não é inclusivo, sempretrás o anterior ao stop 
print (lista[0:3]) 
print (lista[:3]) #começa do 0
print(lista[1:4:2])
#Uso de índices negativos