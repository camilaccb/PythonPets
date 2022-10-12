# sintaxe de uma função 
# num1, num2: argumentos
# Argumentos são variáveis de escopo local: só existem a partir do momento em que a função é chamada e só perdura enquanto eu estiver executando a função

def soma(num1, num2): 
    return num1 + num2

resultado1 = soma(4,6)
resultado2 = soma(10,4)


print(resultado1,resultado2)

# Debugando 
    # Continue
    # Step Over: vai para a próxima linha sem entrar na função 
    # Step Into: vai para a próxima linha entrando na função

# Parei no 33