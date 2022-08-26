# Faça um programa que calcule o aumento de um salário. O programa deve solicitar o valor do salário e a porcentagem de aumento. Exiba o valor do aumento e do novo salário
#Snake case é uma boa prática em python
# PEP 8 - Style Guide for Python  -https://peps.python.org/pep-0008/
# É possível tratar os casos 
# Firmatação da f string
# {valordoaumento:,.2f}, converter variável em string e depois substituir


CONVERSAO_PORCENTAGEM = 0.01

salarioInicial= float(input('Qual o valor do seu salário em R$?'))
porcentagemDeAumento = float(input('Qual a percentagem de aumento?'))
valorDoAumento = salarioInicial * porcentagemDeAumento * CONVERSAO_PORCENTAGEM
novoSalario = salarioInicial + valorDoAumento
print(f'O valor do aumento é R${valorDoAumento:1000.2f} e o novo salário é R$ {novoSalario: 2f}')