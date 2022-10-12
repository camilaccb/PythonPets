# escreva um programa que gere um dicionário em que cada chave seja um caractere de uma dada string, e seu valor seja a quantidade de vezes que aquele caractere aparece
# não é preciso criar uma função, já existe no método 

# Entrada: CAMILA 

# Saida: {'C': 1, 'A': 2, 'M':1, 'I': 1, 'L': 1}

# solução 1 - utilizando lações de repetição

nome = input('Digite a palavra: ')
letras = set(nome)

dic_saida = {}
for letra in letras:
    dic_saida[letra] = nome.count(letra)
       
print(dic_saida)

# solução 2 - utiliza uma classe já pronta

from collections import Counter
print(Counter(nome))






