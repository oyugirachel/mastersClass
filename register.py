# Inicializar a lista de contatos
agenda = []

# Função para cadastrar uma pessoa na agenda
def cadastrar_pessoa():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    status = input("Status (P para Pessoal, C para Comercial): ")
    agenda.append((nome, telefone, cidade, estado, status))
    print("Cadastro realizado com sucesso!")

# Função para alterar dados de uma pessoa na agenda
def alterar_dados():
    nome_alterar = input("Digite o nome da pessoa que deseja alterar: ")
    for i, contato in enumerate(agenda):
        if contato[0] == nome_alterar:
            print(f"Nome: {contato[0]}")
            print(f"Telefone: {contato[1]}")
            print(f"Cidade: {contato[2]}")
            print(f"Estado: {contato[3]}")
            print(f"Status: {contato[4]}")
            novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
            novo_telefone = input("Novo telefone (deixe em branco para manter o mesmo): ")
            nova_cidade = input("Nova cidade (deixe em branco para manter o mesmo): ")
            novo_estado = input("Novo estado (deixe em branco para manter o mesmo): ")
            novo_status = input("Novo status (deixe em branco para manter o mesmo): ")
            if novo_nome:
                contato = (novo_nome, novo_telefone, nova_cidade, novo_estado, novo_status)
                agenda[i] = contato
                print("Dados alterados com sucesso!")
            return
    print(f"Pessoa com o nome '{nome_alterar}' não encontrada.")

# Função para listar todos os contatos na agenda
def listar_agenda():
    for contato in agenda:
        print(f"Nome: {contato[0]}")
        print(f"Telefone: {contato[1]}")
        print(f"Cidade: {contato[2]}")
        print(f"Estado: {contato[3]}")
        print(f"Status: {contato[4]}")
        print()

# Função para procurar uma pessoa na agenda
def procurar_pessoa():
    nome_procurar = input("Digite o nome da pessoa que deseja procurar: ")
    for contato in agenda:
        if contato[0] == nome_procurar:
            print(f"Nome: {contato[0]}")
            print(f"Telefone: {contato[1]}")
            print(f"Cidade: {contato[2]}")
            print(f"Estado: {contato[3]}")
            print(f"Status: {contato[4]}")
            return
    print(f"Pessoa com o nome '{nome_procurar}' não encontrada.")

# Função para excluir uma pessoa da agenda
def excluir_pessoa():
    nome_excluir = input("Digite o nome da pessoa que deseja excluir: ")
    for contato in agenda:
        if contato[0] == nome_excluir:
            agenda.pop(contato)
            print("Cadastro excluído.")
            return
    print(f"Pessoa com o nome '{nome_excluir}' não encontrada.")

# Loop principal
while True:
    print("\nMenu de Opções:")
    print("1. Cadastrar Pessoa na Agenda")
    print("2. Alterar dados da Pessoa")
    print("3. Listar Agenda")
    print("4. Procurar pessoa na Agenda")
    print("5. Excluir Pessoa da Agenda")
    print("6. Sair do sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        alterar_dados()
    elif opcao == "3":
        listar_agenda()
    elif opcao == "4":
        procurar_pessoa()
    elif opcao == "5":
        excluir_pessoa()
    elif opcao == "6":
        print("Saindo do sistema.")
        break
    else:
        print("Erro: opção inválida!")
