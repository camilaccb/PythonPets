# Projeto agenda telefônica

    # Armazena o nome e o telefone
    # Funcionalidades da agenda:
        # Adicionar contato
        # Procurar um contato
        # Listar todos os contatos da agenda
        # Editar contato
        # Excluir contato


agenda = {'Camila Caldas': 85996662597, 'Joana Rita': 85987879530}

funcionalidades_agenda = ['1- Adicionar novo contato', '2- Procurar um contato', '3- Listar todos os contatos da agenda' '4- Editar contato', '5- Excluir contato', '6- Nenhuma das opções anteriores']
# Opção de saida de uma agenda 

print('Agenda telefônica iniciada')

for funcionalidade in funcionalidades_agenda:
    print(funcionalidade)

funcionalidade_desejada = int(input('Digite o número da funcionalidade desejada: ')) 
# validação da seleção da funcionalidade

if funcionalidade_desejada == 1:

    nome_contato_procurado = input('Digite o nome do contato procurado')
    telefone_contato_procurado = agenda.get(nome_contato_procurado, 'Contato não encontrado')
    print(telefone_contato_procurado)
    int(input('Você desejar procurar novamente ou retornar ao menu inicial'))
    
    


    

    
else:
    print('Agenda Encerrada')



