#Escreva um programa que leia a quantidade de dias, horas, minutos, segundos do usuário. calcule o total em segundos e imprima na tela
# Prática ruim: números mágicos no código (números que brotam no código)
# Boa prática: constantes em maiusculo e no início do código com quebra de linha (F12 altera todas as variáveis no código)

QTD_SEGUNDOS_DIA = 24 * 3600
QTD_SEGUNDOS_HORA = 60 *60
QTD_SEGUNDOS_MINUTO = 60

qtd_dias = int(input("Quantidade de dias: "))
qtd_horas = int(input("Quantidadde de horas: "))
qtd_minutos = int(input("Quantidade de minutos: "))
qtd_segundos = int(input("quantidade de segundos: "))
print(f'A quantidade de segundos é {(qtd_dias * QTD_SEGUNDOS_DIA ) + (qtd_horas * QTD_SEGUNDOS_HORA) + (qtd_minutos * QTD_SEGUNDOS_MINUTO) + qtd_segundos}') 
