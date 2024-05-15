#programa que realiza e controla um cadastro de nomes atraves das ações de CRUD - Creat, Read, Update, Delete.
#Definir a lista do cadastro
#variavel global - pode ser acessada dentro de todo o programa
nomes = [] #foi criada uma lista vazia

#funções CRUD


#Create (criar)
def cadastrar_nome():
    nome = input("Digite o nome a ser cadastrado: ")
    nomes.append(nome) #inserindo um novo item na lista
    print(f"O nome {nome} foi cadastrado com sucesso!")

#Read (ler) - listagem geral dos nomes cadastrados
def listar_nomes():
    if nomes: #verdadeiro - listar os nomes cadastrados
        print("Nomes Cadastrados:")
        for i, nome in enumerate(nomes):
            print(f"{i+1}. {nome}")
    else: #falso - mostrar mensagem de lista vazia
        print("Nenhum nome cadastrado.")

#Read - consultado de um nome especifico
def consultar_nome():
    nome = input("Digite o nome a ser encontrado: ")
    if nome in nomes:  #se o nome digitado existir na lista mostra mensagem de sucesso
        print(f"O nome {nome} foi encontrado.")
    else: #falso - mostrar mensagem de erro (nome não encontrado)
        print(f"O nome {nome} não foi encontrado.")

#funcao Menu
def menu():
    while True:
        print("\nMenu: ")
        print("1. Cadastar nome")
        print("2. Listar nomes")
        print("3. Consultar nome")
        print("4. Excluir nome")
        print("5. Ordenar por ordem crescente")
        print("6. Ordenar por prdem decrescente")
        print("7. Sair")

        opcao = input("Digite a opção desejada:")

        if opcao == '1':
            cadastrar_nome()
        elif opcao == '2':
            listar_nomes()
        elif opcao == '3':
            consultar_nome()
        elif opcao == '7':
            #encerrar o programa
            print("Programa encerrado")
            break
        else:
            print("Opção inválida.")

menu()



