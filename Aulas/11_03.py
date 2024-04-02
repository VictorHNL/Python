
#Estruturas condicionais:
numero = float(input("Digite um numero: "))

if numero >= 0 :
    print("Seu valor é positivo")
else:
    print("Seu valor é negativo")


#Escreva um programa em python que receba dois numeros inteiros do usuario e realise a somados dois numeros e o resultado apenas se o segundo numero for maior que o primeiro:

#condicional simples 
n1 = (float(input("Digite o primeiro número: ")))
n2 = (float(input("Digite o segundo número: ")))

if n2 > n1:
    print(n1 + n2)

#condicional complexo
numero = int(input("Digite um número: "))

if numero > 0:
    print("Seu número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("Seu número é zero")


#Escreva um programa em python que, receba dois numeros do usuario e se o primeiro numero for maior calcule e mostre o quadrado da soma dos dois numeros, se o segundo numero for o maior calcule e mostre a soma dos quadrados dos numeros, caso sejam iguais mostrar uma mensagem de erro.
    
#entradas de dados para os valores
n1 = float(input("Digite seu número: "))
n2 = float(input("Digite seu número: "))

#entradas condicionais
#caso 1 - mostrar o quadro da soma
if n1 > n2:
    soma = n1 + n2
    print(f"O quadrado da soma dos números é {soma * soma}")
#caso 2 - mostrar a soma dos quadrados
elif n1 < n2:
    resultado = n1**2 + n2**2
    print(f"As somas dos quadrados é {resultado}")
else:
    print("Erro, os números são iguais tente novamente...")