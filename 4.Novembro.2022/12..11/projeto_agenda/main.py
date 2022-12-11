# Criar um menu com as opções abaixo.
# Ler a opção do usuário.

# O que é possível de ser feito com uma agenda?
# 1. Criar contato
# 1.1 Informações do contato:
#       - Nome, telefone.
# 2. Alterar contato
# 3. Excluir contato
# 4. Pesquisar contato
# 5. Mostrar todos contatos

from menu import solicita_opcao_do_usuario
from opcoes import ler_contato, adicionar_contato_na_agenda,mostrar_todos_os_contatos, recebe_nome_do_contato, procurar_o_nome_do_contato, excluir_contato, executar_operacao


base_de_contatos = {}

print("====== Bem vindo à sua agenda de contatos! ======")
opcao_escolhida = solicita_opcao_do_usuario()

# TODO: utilizar a opção do match

while opcao_escolhida != 6:

    if opcao_escolhida == 1:

        contato = ler_contato()
        adicionar_contato_na_agenda(contato, base_de_contatos)
        print("====== Escolha outra opção ======")
        opcao_escolhida = solicita_opcao_do_usuario()

    elif opcao_escolhida == 2:

        nome_contato = recebe_nome_do_contato()
        contato_encontrado = procurar_o_nome_do_contato(nome_contato,base_de_contatos)

        if contato_encontrado == nome_contato:
            alteracao = input('Qual alteração você deseja fazer? (1-nome do contato, 2-telefone do contato): ')
    
        if alteracao == '1':
            novo_nome_contato = input('Qual o novo nome do contato? ')
            contato_alterado =[novo_nome_contato,base_de_contatos[nome_contato]]
            excluir_contato(nome_contato,base_de_contatos)
            adicionar_contato_na_agenda(contato_alterado,base_de_contatos)
            
        elif alteracao == '2':
            novo_numero_contato = int(input('Qual o novo número do contato? '))
            contato_alterado = [nome_contato, novo_numero_contato]
            excluir_contato(nome_contato, base_de_contatos)
            adicionar_contato_na_agenda(contato_alterado,base_de_contatos)
            
        
        opcao_escolhida = solicita_opcao_do_usuario()

    elif opcao_escolhida == 3:

        executar_operacao(excluir_contato, base_de_contatos=base_de_contatos)
        print("====== Escolha outra opção ======")
        opcao_escolhida = solicita_opcao_do_usuario()
            
    elif opcao_escolhida == 4:
        executar_operacao(procurar_o_nome_do_contato,base_de_contatos=base_de_contatos)
        print("====== Escolha outra opção ======")
        opcao_escolhida = solicita_opcao_do_usuario()        

    elif opcao_escolhida == 5:
       mostrar_todos_os_contatos(base_de_contatos)
       print("====== Escolha outra opção ======")
       opcao_escolhida = solicita_opcao_do_usuario() 


print('A agenda está sendo encerrada')