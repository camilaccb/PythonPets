
# Boas práticas
# Argumentos nomeados e posicionais 
    # Os exemplos abaixo são de argumentos posicionais
# Documentação
    # Tipagem
        # O python tem uma tipagem dinâmica. No exemplo abaixo eu estou definidoo num1 como inteiro, mas se passar outro tipo para o python, ele roda 
# Docstring é uam string de documentação
    # Quando passa o mouse em cima da função, aparece o texto da doc string


def executa_operacoes_basicas(num1: int, num2: int) -> tuple[int] :

    """Retorna a soma, diferença, multiplicação e divisão e retorna"""

    soma = num1 + num2
    dif = num1 - num2
    multi = num1 * num2
    divisao = num1/num2

    print(f"Soma:{soma}")
    print(f"Diferença:{dif}")
    print(f"Multiplicação:{multi}")
    print(f"Divisão:{divisao}")

    return (soma, dif, multi, divisao) # por padrão retorna um objeto (tupla)

resultado1 = executa_operacoes_basicas(1.4,6) # é uma tupla
resultado2 = executa_operacoes_basicas(10,4)

# resultado vai ser igual a none se a função não tiver um retorno 
#x= print("Olá mundo")
#print(x) # é none porque a função print não retorna nada

# Retornando um dicionário

def executa_operacoes_basicas_dicionario(num1: int, num2: int) -> dict[str,int] :

    """Retorna a soma, diferença, multiplicação e divisão e retorna"""

    soma = num1 + num2
    dif = num1 - num2
    multi = num1 * num2
    divisao = num1/num2

    print(f"Soma:{soma}")
    print(f"Diferença:{dif}")
    print(f"Multiplicação:{multi}")
    print(f"Divisão:{divisao}")

    dicionario_saida = {
        "soma": soma, 
        "diferença": dif,
        "multiplicacao": multi, 
        "divisao": divisao
    }

    return dicionario_saida
 
# na tipagem do retorno poderia escrever: dict[str,int]