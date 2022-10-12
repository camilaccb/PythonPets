# Tuplas 
 # Tupla tem o mesmo comportamento de uma lista 
    # lista -> []
    # tupla -> ()
 # Diferentemente da lista, uma tupla não pode ser alterada, é uma estrutura mais rígida -> imutabilidade
 # Tem apenas 2 métodos 
 # Exemplos de utilização 

#Exemplo
tupla_numeros = (1,2,3,4,5,6)

#Exemplo de uma mistura de dados
clientes = [
    ("Henrique","22/01/1991","111.222.333-44"),
    ("João","22/01/1990","000.222.333-44"),
    ("Antonio","22/01/2000","555.222.333-44")
]


# Uma string é um objeto imutável 
cpf = "555.222.333-44"

cpfNew = cpf.replace("44","15")

print(cpf)
print(cpfNew)

# Desempacotamento de uma tupla
nome, data_nascimento, cpf = ("Henrique", "22/01/1991", "111.222.333-44")

# Empacotamento
cliente = ("Henrique", "22/01/1991", "111.222.333-444")
print(cliente)
print(nome, data_nascimento, cpf)

# Exemplo de desempactotamento 

sigla_estado = [("MG", "Minas Gerais"), ("SP", "São Paulo"), ("AM", "Amazonas")]
sigla, nome_completo = sigla_estado[0]
print(f'Siga do estado {sigla}, nome completo do estado: {nome_completo}')
