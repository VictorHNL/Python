#19. Crie um programa que peça o raio e a altura de um cilindro e calcule seu volume.

import math
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
volume = math.pi * (raio ** 2) * altura
print("O volume do cilindro é:", volume)