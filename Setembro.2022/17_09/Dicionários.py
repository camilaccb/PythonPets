# Dicionário é um estrutura de chave e valor
# Dicionário é um objeto mutável
# É como se fosse um mapeamento
# É possivel colocar qualquer tipo objeto
# A chave não pode estar duplicada

carrinho_compras = {
    "banana": 1, 
    "maçã": 4, 
    "leite": 1
}


# Modificando um valor

carrinho_compras["banana"] = 10

# Buscando um valor 
print(carrinho_compras["banana"]) # Devolve o valor associado a chave

#Acrescentar uma chave
carrinho_compras["macarrão"] = 4 

print(carrinho_compras["macarrão"])

# função dict() -> cria um dicionário 

carrinho_compras2 = dict(banana =1, maça =4, leite = 2)
print(carrinho_compras2)

# Tipagem -> ela é meramente opcional, pois no python existe uma tipagem dinâmica
carrinho_compras3: dict[str, int] = {"banana": 1, "maçã": 4, "leite": 4} # É possível fazer a mesma tipagem em listas 

# Métodos de um dicionário

print(sum(carrinho_compras.values())) # isso é uma função
print(carrinho_compras.items()) # retorna um objeto dict items, dict keys
carrinho_compras.get("carne", 0) # se não tiver o valor ele atribui 0 , é uma forma de tratar um erro /lembrar que uma string é case sensitive

qtd_banana = carrinho_compras.pop("banana") # remove essa chave do dicionario e retorna numa variável, especificando a chave
ultimo = carrinho_compras.popitem() # vai removendo do último pro primeiro





