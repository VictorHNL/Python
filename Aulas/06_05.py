# encontrara soma dos numeros de 1 a 20 de 3 em 3
'''
soma = 0 
print("Somatório dos números: ")
for x in range(1,20,3):
    print(x)
    soma = soma + x 
print(f"A soma é: {soma}")
'''

#progra que lista todos os numeros de 1 ate 29
'''
for n in range (0,30):
    print(n)
'''
'''
#Primeiro exemplo de listas em python
lista =["Python","Java","C++","C#","PHP","Delphi","Cobol","VB"]
#imprimir o valor da quarta posicao
print(lista[3])
#imprimir a lista
print(lista)
#altrar um valor da lista
lista[4] = "Clipper"
print(lista)
#mostrar o tamanho da lista
print("Sua lista possui", len(lista),"itens.")
#adicionara um elemento (valor) na lista (no final)
lista.append("SmallTalk")
#remover um item da lista (com indice)
del lista [2]
print(lista)
#unir listas 
lista.extend(["MySQL","PostgreSQL","Oracle"])
print(lista)
'''
'''
Dada a lista L = [5, 7, 2, 9, 4, 1, 3 escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente
f) lista em ordem decrescente.
'''

l = [5, 7, 2, 9, 4, 1, 3]

tamanho = len(l)
print("Tamanho da lista:", tamanho)

# b) Maior valor da lista
maior = max(l)
print("Maior valor da lista:", maior)

# c) Menor valor da lista
menor = min(l)
print("Menor valor da lista:", menor)

# d) Soma de todos os elementos da lista
soma = sum(l)
print("Soma de todos os elementos da lista:", soma)

# e) Lista em ordem crescente
crescente = sorted(l)
print("Lista em ordem crescente:", crescente)

# f) Lista em ordem decrescente
decrescente = sorted(l, reverse=True)
print("Lista em ordem decrescente:", decrescente)