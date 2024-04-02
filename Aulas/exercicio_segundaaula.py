# 1- Receba dois números do usuário e mostre o resultado da multiplicação
'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(n1 * n2)

#2- receba o nome do usuário e mostre uma mensagem de boas vindas

nome = input("Qual seu nome: ")
print(f"Bom dia {nome}")

""" 3- receba um número do usuário e mostre:
a) o valor do dobro
b) o valor da metade
c) o valor de seu quadrado """

numero = float(input("Digite um número: "))
dobro_numero = numero * 2
print(f"O dobro do seu número é: {dobro_numero}")
valor_metade = numero / 2
print(f"A metade do seu número é {valor_metade}")
valor_quadrado = numero * numero
print(f"Seu número ao quadrado: {valor_quadrado}")
'''
"""Uma escola precisa calcular a média final das notas de seus alunos.
As médias possuem as seguintes fórmulas para cálculo:
Média final = (nota 1 + nota 2 + nota 3)/3 

escreva um programa em python que calcule e mostra a media de um aluno juntamente com seu nome;

"""
aluno = input("Escreva seu nome: ")
nota1 = float(input("escreva sua nota 1: "))
nota2 = float(input("escreva sua nota 2: "))
nota3 = float(input("escreva sua nota 3: "))
media_final = ((nota1 + nota2 + nota3)/ 3)
aprovado = 7

if media_final >= aprovado:
    print(f"Aluno {aluno}, foi aprovado com a media da nota final de: {media_final}.")
else:
    print(f"Aluno {aluno}, foi reprovado com a media da nota final de: {media_final}.")
