def ola():
    print("Olá Mundo!")

#Nomes de funções não possuem caracteres especiais

ola()


def saudacao():
    print("Olá Seja be,-vindo(a)")

saudacao()

def saudacao_personalizada(usuario):
    print(f"Olá, {usuario}! Seja bem-vindo(a)")


#chamado da função
nome = input("Digite seu nome: ")
saudacao_personalizada(nome)
