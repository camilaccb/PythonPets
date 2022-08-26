"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado"""
#Documentação (doc script)
#Documentação do código em formato de script 

VALOR_ALUGUEL_DIA = 60
VALOR_KM = 0.15

quantidadeKm = float(input('Quantidade de Km percorridos'))
quantidadeDeDias = int(input('Quantidade de dias pelos quais o carro foi alugado'))

valorFinal = (quantidadeDeDias * VALOR_ALUGUEL_DIA) + (quantidadeKm * VALOR_KM)

print(f'O preço a pagar é {valorFinal}')
