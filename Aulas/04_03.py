
'''
nome = input("digite seu nome: ")
#concatenção
print("Olá " + nome + ", boa noite")

#convertendo a entrada de dados para valores inteiros
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
soma = n1 + n2 
print(soma)

#convertendo a entrada de dados para valores reais
n3 = float(input("digite um numero: \n"))
n4 = float(input("digite um numero: \n "))
soma = n1 + n2 
print(soma)
'''

import time

nome = input("escreva seu nome: ")
adivinhe = ("Irei adivinhar seu nome....") 
print(adivinhe)
time.sleep(1.5)
print("3...")
time.sleep(1.5)
print("2...")
time.sleep(1.5)
print("1...")
print(f"seu nome é: {nome}")
