# 1 - Escreva um programa em python que receba o nome do usuário e mostre uma mensagem de boas vindas
nome = input("Digite seu nome: ")
print(f"Boas vindas {nome}")

# 2 - Escreva um programa em python e verifique se as dimensões de um quadrilátero forma um quadrado ou um retângulo

base = float(input("Base : "))
altura = float(input("Altura: "))

if base == altura:
    print("As dimensões do seu Quadrilátero forma um Quadrado")
else:
    print("As dimensões do seu Quadrilátero forma um retângulo")

'''
# 3 - Escreva um programa que receba a idade de uma pessoa e de acordo com sua idade apresente as seguintes frases:
    a) não pode votar
    b) voto opcional
    c) voto obrigatório
'''

old = int(input("Digite sua idade: "))

if old < 16:
    print("Você não pode votar")
elif old >= 18 and 70:
    print("O seu Voto é obrigatório")
else:
    print("O seu voto é opcional")

'''
Portas Lógicas
 E --> and
 OU --> or 
'''

# escreva um programa em python que receba o nome de uma pessoa, sua idade e seu gênero e mostre se esta pessoa está apto ao SMO(serviço militar obrigatório)

nome = input("Digite seu nome: ")
idade = int(input(f"Bem-vindo {nome} qual é a sua idade? "))
genero = input(f"{nome} digite se você é Homem ou Mulher? ")
genero.lower
x = str("homem")
if genero == x and idade >= 18 and 45:
    print(f"{nome} está apto para o SMO(Serviço Militar obrigatório)")
else:
    print(f"{nome} não é apito para o serviço militar")

