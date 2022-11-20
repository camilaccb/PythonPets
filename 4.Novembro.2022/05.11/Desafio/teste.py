from random import randint

print("**************************")
print("BEM-VINDO AO JOGO DO PEDRO")
print("**************************")

nivel_de_dificuldade = int(input('Indique o número do nível de dificuldade (1- Fácil, 2- Médio, 3- Difícil: '))

if nivel_de_dificuldade == 1:
    random = randint(1,10)
    maior_valor = 10
elif nivel_de_dificuldade == 2:
    random = randint(1,50)
    maior_valor = 50
else:
    random = randint(1,100)
    maior_valor = 100

chances = 5
chute = 0

while chute != random:
    chute = input(f'Chute um numero de 1 a {maior_valor} : ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        print("Vc tem {} chances".format(chances))
        if chute == random:
            print("")
            print("Parabêns, vc venceu. O numero era {} e ainda faltava {} chances".format(random, chances))
            print("")
            break;
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break
print(' ### FIM DE JOGO ###')

