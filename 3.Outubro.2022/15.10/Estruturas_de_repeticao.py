# for e do while 
# variáveis temporárias de repetição 
# Empacotamento/desempacotamento
# Quando usar o for and while 
# Interrompendo fluxo de repetição com break, continue, pass 

for letra in "Henrique":
    print(letra)


# No while não tem uma sequencia
#No python não tem um contador
# ctrl + c interrompe o looping infinito 

numero = 0 

while numero <=10:
    print(numero)
    numero = numero + 1 # atualização da condição


# Exemplo de looping infinito

# numero = 0 
# condicao = numero <=10

# while condicao:
    #print(numero)
    #numero = numero + 1


# Looping infinito acima resolvido 

numero = 0 
condicao = numero <=10

while condicao:
    print(numero)
    condicao = numero <=10