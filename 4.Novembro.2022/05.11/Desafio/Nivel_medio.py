from random import randint

nivel_de_dificuldade = int(input('Indique o número do nível de dificuldade (1- Fácil, 2- Médio, 3- Difícil: '))

if nivel_de_dificuldade == 1:
    numero_sorteado = randint(1,10)
    maior_valor = 10
elif nivel_de_dificuldade == 2:
    numero_sorteado = randint(1,50)
    maior_valor = 50
else:
    numero_sorteado = randint(1,100)
    maior_valor = 100

#print(f'Número sorteado: {numero_sorteado}')


numero_de_tentativas = 5

for tentativa_da_vez in range(numero_de_tentativas):

    numero_tentativa_adivinhar = int(input(f'Insira a sua {tentativa_da_vez + 1}ª tentativa entre 1 e {maior_valor}:')) 

    if numero_tentativa_adivinhar == numero_sorteado:
        print('Você adivinhou o número! Jogo encerrado')
        break
    else:
        if (tentativa_da_vez + 1) == 5: 
            print('Suas tentativas acabaram! Jogo encerrado!')
        else:
            continue
