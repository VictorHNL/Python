#exercicio 1: escreva um programa em python que consiga receber do usuário no maximo vinte nomes de pessoas
quantidade_usuario = 0 

while quantidade_usuario < 20:
    x = input("Deseja cadastrar um nome? (s/n)").lower()
    
    if x == "s":
        nome_usuario = input("Digite o nome do usuário: ")
        quantidade_usuario += 1 

    elif x == "n":
        print("Cadastro encerrado.")
        break

print("Número máximo de usuários alcançados.")

#exercicio 2: escreva um programa em python que receba do usuário as idades dos 50 alunos de sistemas de informações

quantidade_cadastro = 0

while quantidade_cadastro < 50:
    inicio = input("Deseja cadastrar uma idade? (s/n): ").lower()

    if inicio == "s":
        input("Digite a idade do usuário: ")
        quantidade_cadastro += 1
    
    elif inicio == "n":
        print("Cadastro encerrado")
        break

print("Número máximo de idades de usuário alcançados.")

