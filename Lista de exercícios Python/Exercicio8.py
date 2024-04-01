#8. Escreva um programa que converta um valor em dólares para reais. O usuário deve informar a taxa de câmbio e o valor em dólares.
dolar = float(input("Digite seu valor em dólares:"))
taxa_de_cambio = ("R$4.94 para cada 1.0US$")
print(taxa_de_cambio)
converter = (dolar * 4.94)
print(f"Dolar: {dolar}, Reias: {converter}")
