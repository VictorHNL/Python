'''
 - Variáveis acumuladoras
Realizam o somatório de uma coleção de valores

 - Exercício 1 
  Uma escola precisa de um programa que receba as 4 notas de um aluno, calcule a média aritmétrica das notas e mostre se o aluno esta aprovado ou não com sua média

   - Média de aprovação da escola: 6,0
'''


while True:
    opcao = input("Deseja cadastrar um aluno s/n?: ")

    if opcao.lower() == "s":
        aluno = input("Digite seu nome: ")
        n1 = float(input(f"Seja bem-vindo {aluno}, digite a primeira nota: "))
        n2 = float(input(f" Aluno (a) {aluno}, digite a segunda nota: "))
        n3 = float(input(f" Aluno (a) {aluno}, digite a terceira nota: "))
        n4 = float(input(f" Aluno (a) {aluno}, digite a quarta nota: "))

        nota_final = ((n1 + n2 + n3 + n4)/4)

        if nota_final >= 6:
            print(f"Aluno (a) {aluno} foi aprovado com média final de {nota_final:.1f}")
        else:
            print(f"Aluno (a) {aluno} está reprovado com a média final de {nota_final:.1f}")
    else:
        break

'''
 - Escreva um programa em python que mostre todos os números ímpares entre 10 - 325
'''

x = 11
somatorio = 0
while x <= 325:
    if x % 2 != 0:
        print(x)
        x +=2
    somatorio += x
print(f"A soma de todos os ímpares entre o número 11 a 325 é de {somatorio}")

'''
 - Uma empresa precisa cadastrar os salários de seus funcionários, final do cadastro devem ser apresentados as seguintes afirmações:
    - Somatorio total dos salários
    - Média sálarial 
    - O maior sálario cadastrado
    - Menos sálario cadastrado

    Escreva um programa em python que atenda os seguintes requisitos
'''
somatorio_salarial = 0
total_funcionario = 0
maior_salario = float('-inf')  # Inicializa com um valor negativo infinito
menor_salario = float('inf')   # Inicializa com um valor positivo infinito

while True:
    opcao = input("Deseja cadastrar um funcionário? (s/n): ")
    if opcao.lower() == "s":
        funcionario = input("Escreva o nome do funcionário: ")
        salario = float(input(f"Digite o salário do funcionário {funcionario}: "))
        total_funcionario += 1
        somatorio_salarial += salario
        
        # Atualiza o maior e o menor salário, se necessário
        if salario > maior_salario:
            maior_salario = salario
        if salario < menor_salario:
            menor_salario = salario
    else:
        break
    
print(f"A somatória do salário dos funcionários é de {somatorio_salarial}")
print(f"O maior salário cadastrado é {maior_salario}")
print(f"O menor salário cadastrado é {menor_salario}")
media_salarial = somatorio_salarial / total_funcionario
print(f"A média salarial foi de {media_salarial:.2f}")
