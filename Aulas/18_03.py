#importa o modulo pi da biblioteca math
from math import pi
'''
raio = float(input("informe o raio do círculo: "))
if raio > 0:
    area = pi * ( raio**2)
    #imprime o resultado da area
    print(f"A área do circulo é: {area:.2}")
else: 
    print("A medido do raio deve ser maior que zero.")
'''
'''
 - Estruturas de repetição
 Blocos de programa que repetem suas intruções

 - Enquanto (while)
 Enquanto (condição) faça
 intruções

 Fim_enquanto

 Ex:
 x = 0;
 Enquanto (x < 100 ) faça
 Escreva (x);
 x:= x + 1;
 Fim_Enquanto.
'''
#loop - laço de repetição 
'''
x = 0
while x <= 100:
    print(x)
    x += 1 # x = x + 1

#Escreva um programa em python que mostre todos os numeros pares entre 0 e 2250
x = 0
while x <= 2250:
    print(x)
    x += 2

# 2 forma de fazer
numero = 0
quantidade = 0 # variavel contadora
somatorio = 0 # variavel acumuladora
while numero <=2250:  # Você pode alterar o limite superior conforme necessário
    if numero % 2 == 0:
        print(numero)
        quantidade += 1
        somatorio += numero
    numero += 1
print(f"Foram econtrados{quantidade} números pares.")
print(f"A soma total dos números pares é {somatorio}")



#programa de cadastro de salarios
quantidadeFuncionarios = 0 # total de funcionarios
totalSalarios =  0 #somatorio os salarios
quantidade = int(input("Quantos funcionários deseja cadastrar? "))
cont = 0 #conta os funcionarios ate a quantidade desejada

while cont < quantidade:
    salario = float(input("Informe o salário do funcionario: "))
    totalSalarios += salario
    cont += 1 #mais um funcionario cadastrado
print(f"A soma total dos salários é {totalSalarios:.2f}")

'''
'''
#programa de cadastro de salarios
quantFuncionarios = 0 
totalSalarios = 0

opcao = "s"
while True:
    if opcao == "s":
        salario = float(input("Informe o salário do funcionario: "))
        totalSalarios += salario
        quantFuncionarios += 1
        opcao = input("Deseja cadasrar mais um funcionário(s/n): ")
    else:
        break

print(f"A soma total dos salários é R${totalSalarios}")
print(f"A empresa pagou para {quantFuncionarios} funcionários.")
'''

#menu 
while True:
    print("""
            Programa de cálculo de áreas
          Menu - Digite a opção desejada:
          1. Quadrado
          2. Retângulo
          3. Triângulo
          4. Trapézio
          5. Pentágono
          6. Círculo
          0. Sair
            """)
    opcao = int(input("Qual área desejada calcular? "))
    if opcao == 1:
        ladoQ1 = float(input("Digite o tamanho do lado 1: "))
        ladoQ2 = float(input("Digite o tamanho do lado 2: "))
        areaQuadrado = ladoQ1 * ladoQ2
        print(f"A área do quadrado é: {areaQuadrado}")
    elif opcao == 2:
        ladoR1 = float(input("Digite o tamanho do lado do seu retângulo: "))
        alturaR2 = float(input("Digite a altura do seu retângulo: "))
        areaRetangulo = ladoR1 * alturaR2
        print(f"A área do seu retângulo é : {areaRetangulo}")
    elif opcao == 3:
        ladoT = float(input("Digite a base do triângulo: "))
        baseT = float(input("Digite a altura do seu triângulo: "))
        areaTriangulo = (ladoT * baseT) / 2
        print(f"A área do seu Triângulo: {areaTriangulo}")
    elif opcao == 4:
        BaseMaior = float(input("Digite base maior do seu trapezio: "))
        BaseMenor = float(input("Digite a base menor do seu trapezio: "))
        alturaTrapezio = float(input("Digite a altura do seu trapezio: "))
        areaTrapezio = ((BaseMaior + BaseMenor) * alturaTrapezio) / 2
        print(f"A área do seu Trapezio é: {areaTrapezio}")
    elif opcao == 5:
        ladoP = float(input("Digite o lado do seu pentágono: "))
        alturaP = float(input("Digite a altura do seu pentagono: "))
        areaPentagono = ladoP * alturaP
        print(f"A área do seu Pentágono: {areaPentagono}")
    elif opcao == 6:
        raioCirculo = float(input("Informe o raio do Círculo: "))
        areaCirculo = pi * raioCirculo
        print(f"A área do seu círculo é: {areaCirculo:.2}")
    elif opcao == 0:
        print("Obrigado por usar nosso menu de calculo das áreas :) ")
        break
    else:
        print("Opção inválida!")
        