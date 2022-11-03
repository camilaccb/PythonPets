# Repetir a solicitação de uma resposta até que as entradas sejam válidas
# O que é um decimal: elementos de string que estão na base decimal (0-9)
    # Existem outras bases
    # A base do computador é binária. Ele só entende base binária 
    # 0.1 + 0.2 == 0.3 
        # Resultado falso

idade = (input("Qual a sua idade?"))

idade_valida = idade.isdecimal() and int(idade) > 0

while not idade_valida:
    print("Idade inválida! Por favor digite um valor válido")
    idade = (input("Qual a sua idade novamente ?"))
    idade_valida = idade.isdecimal() and int(idade) > 0

idade = int(idade)

maior_de_idade = idade >=18 # Regra de negócio 

esta_com_os_pais = input("Está acompanhada dos pais? S/N?: ")
pais_presentes = esta_com_os_pais.lower() == "s" # Regra de negócio 
pais_ausentes = esta_com_os_pais.lower() == "n" # regra de negócio 
resposta_invalida = not (pais_presentes or pais_ausentes)

if resposta_invalida:
    print("Resposta inválida")
elif maior_de_idade and pais_presentes: # regra de negócio 
    print("Seja bem vindo à festa!")
else: 
    print("Você está barrado(a)")







