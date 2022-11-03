#Exercicio 1 
# faça um programa que peça 2 números inteiros. Imprima a soma deles na tela 
# Dica: não colocar ponto no nome do arquivo para não confundir com a extensão do arquivo
# Input é uma função que retorna uma string
# Pergunta: Porque não poderia utilizar num1.int -> o int é uma função e não um método, não existe um método de uma string que converte em inteiro 

num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
soma = num1 + num2
print('A soma  dos números é: ', num1 + num2)

#print ('A soma dos números {} e {} é {}'.format(num1, num2, soma))
#Na linha acima pode usar um único format 
#print (f"A soma do número {num1} e número {num2} é {soma}")
#print (f"A soma do número {num1} e número {num2} é {num1+num2}")
