from menu import solicita_opcao_do_usuario
from json import dumps, loads


def ler_contato() -> list:
    """Le nome, sobrenome e telefone informado pelo usuario.

    Returns
    -------
    list
        Lista com nome, sobrenome e telefone fonecidos pelo usuario.
    """
    print("Informações do novo contato:")
    nome = input("Digite o nome: ")
    print("Para o telefone, digite neste formato: DDD (sem o zero) + somente números")
    print("Exemplo: 9933332222 ou 11912345678")

    # Corrigir o formato de entrada do telefone para inteiro
    # TODO: validar se o telefone informado contém apenas números
    # TODO: validar se tem 10 ou 11 dígitos
    telefone = int(input("Digite o telefone: "))

    contato = [nome,telefone]

    return contato


def atualizar_arquivo_json(base_de_contatos: dict):
    json_output_file = "agenda.json"
    json_string = dumps(base_de_contatos, indent=1)
    with open(json_output_file, mode = "w", encoding= "utf-8") as f:
        f.write(json_string)
        

def adicionar_contato_na_agenda(contato: list, base_de_contatos: dict):
    
    nome = contato[0]
    telefone = contato[1] 
    base_de_contatos[nome] = telefone
    atualizar_arquivo_json(base_de_contatos)
    
    # TODO: dar uma mensagem de erro quando tiver um contato repetido
    
    
    print("Contato adicionado com sucesso.")

    

def mostrar_todos_os_contatos(base_de_contatos: dict):

    lista_nomes = list(base_de_contatos) 

    for nome_contato in lista_nomes:
        telefone = base_de_contatos[nome_contato]
        print(f'{nome_contato}: {telefone}')


def recebe_nome_do_contato():
    
    nome_contato = input('Digite o nome do contato? ')
    return nome_contato


def procurar_o_nome_do_contato(nome_contato_procurado: str, base_de_contatos: dict):

    mensagem_contato_não_encontrado = 'O contato não foi encontrado na agenda, tente novamente'
    numero_contato = base_de_contatos.get(nome_contato_procurado)
    
    if numero_contato == None:
        print(mensagem_contato_não_encontrado)
        nome_contato_procurado = None
    else:
        print(f'{nome_contato_procurado}: {numero_contato}')
    
    return nome_contato_procurado
        


def excluir_contato(nome_contato_para_excluir: str, base_de_contatos: dict):

    mensagem_contato_não_encontrado = 'O contato não foi encontrado na agenda, tente novamente'
    base_de_contatos.pop(nome_contato_para_excluir,mensagem_contato_não_encontrado)
    atualizar_arquivo_json(base_de_contatos)


def executar_operacao(operacao, base_de_contatos: dict):

    nome_contato = recebe_nome_do_contato()
    operacao(nome_contato, base_de_contatos)
    

    



    





    

    

    



    












    
    
