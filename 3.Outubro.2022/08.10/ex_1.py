# Ser maior de idade(18 anos ou mais) e estar com os pais 
# And, or, not 
    # not V = F
    # not F = V


# 3 versão com melhor legibilidade

idade = int(input("Qual a sua idade?"))
maior_de_idade = idade >=18

esta_com_os_pais = input("Está acompanhada dos pais? S/N?: ")
pais_presentes = esta_com_os_pais.lower() == "s"
pais_ausentes = esta_com_os_pais.lower() == "n"
resposta_invalida = not (pais_presentes or pais_ausentes)

if resposta_invalida:
    print("Resposta inválida")
elif maior_de_idade and pais_presentes:
    print("Seja bem vindo à festa!")
else: 
    print("Você está barrado(a)")

# Versão inicial simplificada

if idade >= 18 and esta_com_os_pais == 'S':
    print("Seja bem vindo à festa!")
else: 
    print("Você está barrado(a)")

# 2 versão com estruturas condicionais aninhadas
    # Estruturas aninhadas não é uma boa prática 

if (esta_com_os_pais.lower() == "s"or esta_com_os_pais.lower == "n") and (len(esta_com_os_pais) == 1):
    if idade >= 18 and esta_com_os_pais == "s":
        print("Seja bem vindo à festa!")
    else: 
        print("Você está barrado(a)")
else: 
    print("Resposta inválida")

