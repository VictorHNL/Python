'''
Programa validador de palindromos
verifica se uma palavra digitada é um palindromo ou não
Ultilizando funcoes e listas
'''

def eh_palindromo(palavra):
    #função que verifica se uma palavra digitada é um palindromo
    palavra = palavra.lower() #transforma toda a palavra em minuscula
    palavra_invertida = list(palavra) #converte a palavra para lista
    palavra_invertida.reverse() #inverte a lista de caracteres
    #retorna o valor invertido da palavra
    return palavra == "".join(palavra_invertida) #compara a palavra original com a palavra invertida


#verifica se a palavra é um palindromo

while True:
    #solicita a palavra para o usuário
    palavra = input("Digite uma palavra: ")

    
    if eh_palindromo(palavra):
        print(f"A palavra digitada, {palavra}, é um palindromo.")
    else: 
        print(f"A palavra digitada, {palavra}, não é um palíndromo.")

    opcao = input("Deseja cadastrar uma nova palavra) (s=sim)   ").lower()
    if opcao != "s":
        break