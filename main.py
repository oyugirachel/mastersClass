# Definindo uma lista vazia para armazenar registros de contato
agenda = []

# Função para registrar uma nova pessoa na agenda
def registrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o telefone: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    status = input("Digite o status (P para Pessoal, C para Comercial): ")
    agenda.append((nome, telefone, cidade, estado, status))
    print("Registro adicionado com sucesso!")

# Função para alterar dados de uma pessoa na agenda
def buscar_pessoa():
    nome_busca = input("Digite o nome da pessoa que deseja alterar: ")
    encontrado = False
    for idx, pessoa in enumerate(agenda):
        if pessoa[0] == nome_busca:
            telefone = input("Digite novo telefone: ")
            cidade = input("Digite novo cidade: ")
            estado = input("Digite novo estado: ")
            status = input("Digite novo Status (P para pessoaal, C para Business): ").upper()
            agenda[idx] = (nome_busca, telefone, cidade, estado, status)
            encontrado = True
            print("dados atualizados com sucesso!")
            break
    if not encontrado:
        print(f"pessoa com o Nome {nome_busca} not encontrado.")

# Função para listar todas as pessoas na agenda
def listar_agenda():
    for pessoa  in agenda:
        print("Nome:", pessoa[0])
        print("telefone:", pessoa[1])
        print("cidade:", pessoa[2])
        print("estado:", pessoa[3])
        print("Status:", pessoa[4])
        print("-" * 20)

# Função para buscar dados de uma pessoa na agenda
def buscar_pessoa():
    nome_busca = input("Digite o nome da pessoa que deseja buscar: ")
    encontrado = False
    for pessoa in agenda:
        if pessoa[0] == nome_busca:
            print("Nome:", pessoa[0])
            print("telefone:", pessoa[1])
            print("cidade:", pessoa[2])
            print("estado:", pessoa[3])
            print("Status:", pessoa[4])
            encontrado = True
            break
    if not encontrado:
        print(f"Pessoa com o nome {nome_busca} nao encontrado.")

#  Função para excluir uma pessoa da agenda
def excluir_pessoa():
    nome_busca = input("Digite o nome da pessoa que deseja excluir:  ")
    encontrado = False
    for idx, pessoa in enumerate(agenda):
        if pessoa[0] == nome_busca:
            agenda.pop(idx)
            print("Registro excluído com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print(f"Pessoa com o nome {nome_busca} não encontrada!.")

# Função principal
while True:
    print("\nMenu:")
    print("1. Registrar Pessoa na Agenda")
    print("2. Alterar Dados da Pessoa")
    print("3. Listar Agenda")
    print("4. Buscar Pessoa na Agenda")
    print("5. Excluir Pessoa da Agenda")
    print("6. Sair do Sistema")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        registrar_pessoa()
    elif opcao == "2":
        buscar_pessoa()
    elif opcao == "3":
        listar_agenda()
    elif opcao == "4":
        buscar_pessoa()
    elif opcao == "5":
        excluir_pessoa()
    elif opcao == "6":
        print("Saindo do sistema....")
        break
    else:
        print("Erro: opção inválida!! Escolha uma opção válida no menu..")
