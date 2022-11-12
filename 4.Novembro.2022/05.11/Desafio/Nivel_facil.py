
from random import randint

numero_sorteado = randint(1,10)
print(f'Número sorteado: {numero_sorteado}')

continuar = True

while continuar == True:
    numero_tentativa_adivinhar = int(input('Insira a sua tentativa entre 1 e 10:')) 

    if numero_tentativa_adivinhar == numero_sorteado:
        print('Você adivinhou o número')
        continuar = False
    else:
        jogar_novamente = input('Você não acertou o número! Deseja jogar novamente? [s/n]: ')

        if jogar_novamente == 's':
            continuar = True
        else:
            continuar = False
            print('Jogo encerrado')

        



