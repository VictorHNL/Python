'''
 - Variáveis acumuladoras
Realizam o somatório de uma coleção de valores

 - Exercício 1 
  Uma escola precisa de um programa que receba as 4 notas de um aluno, calcule a média aritmétrica das notas e mostre se o aluno esta aprovado ou não com sua média

   - Média de aprovação da escola: 6,0
'''


while True:
    opcao = input("Deseja cadastrar um aluno s/n?: ")
    opcao.lower
    
    if opcao == "s":
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
