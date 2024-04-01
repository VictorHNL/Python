#18. Desenvolva um programa que calcule o salário líquido de um funcionário,considerando descontos de impostos (10%).

salario = float(input("Digite o salário do funcionário: "))
salario_liquido = salario * 0.9  # desconto de 10%
print("O salário líquido do funcionário é:", salario_liquido)