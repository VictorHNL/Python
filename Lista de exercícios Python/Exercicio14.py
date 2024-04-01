#14. Escreva um programa que calcule o desconto de um produto com base em um percentual informado pelo usuário.

valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = valor_produto * (percentual_desconto / 100)
valor_com_desconto = valor_produto - desconto
print("O valor do produto com desconto é:", valor_com_desconto)