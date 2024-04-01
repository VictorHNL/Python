#Jogo da adivinhação
while True:
    print("Um número secreto foi escolhido aleatoriamente entre 1 a 100. O desafio é adivnhar o número secreto")

    numero = int(input("Digite um numéro de 1 a 100: "))
    secreto = 58

    if numero > secreto:
        print("O número secreto é menor")
    elif numero < secreto :
        print("O número secreto é maior")
    else:
        print("Párabens! você advinhou o número secreto!")
        break
