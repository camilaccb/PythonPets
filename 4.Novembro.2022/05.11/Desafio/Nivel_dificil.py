QTD_PONTOS_INICIAL = 10
QTD_PONTOS_ACERTO = 10
QTD_PONTOS_ERRO = 2 


from random import randint


nivel_de_dificuldade = int(input('Indique o número do nível de dificuldade (1- Fácil, 2- Médio, 3- Difícil:) '))

def sorteando_numero(nivel: int) -> tuple[int]:

    """Função que sorteia o valor de acordo com o nível de dificuldade escolhido pelo jogador"""

    if  nivel == 1:
        maior_valor = 10
    elif nivel == 2:
        maior_valor = 50
    else:
        maior_valor = 100

    numero_sorteio = randint(1,maior_valor)
    return (numero_sorteio, maior_valor)
    

def continuar_jogo(pontos: int) -> bool:

    """Função que define se o jogo deve continuar ou não com base na quantidade de pontos (vencedor >= 50 pontos e perdedor = 0 pontos) """

    if not pontos == 0:
        if pontos >=50:
            print('Você atingiu 50 pontos e venceu o jogo')
            continuar_jogo = False
        else:
            continuar_jogo = True        
    else:
        print('Você atingiu 0 pontos e perdeu o jogo')
        continuar_jogo = False
        
    return  continuar_jogo
        

qtd_pontos = QTD_PONTOS_INICIAL
condicao_continuar = qtd_pontos < 50 and qtd_pontos > 0

while condicao_continuar == True:

    numero_sorteado = sorteando_numero(nivel_de_dificuldade)[0]
    valor_maximo_intervalo = sorteando_numero(nivel_de_dificuldade)[1] 
    print(f'Número sorteado: {numero_sorteado}')

    numero_tentativa_adivinhar = int(input(f'Insira a sua tentativa entre 1 e {valor_maximo_intervalo}:')) 

    if numero_tentativa_adivinhar == numero_sorteado:
        print(f'Você adivinhou o número e ganhou mais {QTD_PONTOS_ACERTO} pontos')
        qtd_pontos = qtd_pontos + QTD_PONTOS_ACERTO
    else:
        print(f'Você errou o número e perder {QTD_PONTOS_ERRO} pontos')
        qtd_pontos = qtd_pontos - QTD_PONTOS_ERRO

    print(f'Quantidade de pontos: {qtd_pontos}')    

    condicao_continuar =  continuar_jogo(qtd_pontos)
    
       
    





    
      
        

      



