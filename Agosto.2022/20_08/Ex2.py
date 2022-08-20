#Escreva um programa que leia um valor em metros e o exiba convertido em milimetros
# O python não reconhece a vírgula, ex: 3,5. O separador decimal é o "."

valorInicial = input("Digite o valor em metros")
#print(type(valorInicial))
valorInicial = float(valorInicial.replace(',','.')) # permite a aceitação de valores com com ponto e virgula
print(f"O valor em milimetros é : {valorInicial*1000}")