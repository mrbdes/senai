# Faça um programa, utilizando while e listas, que permita o usuário
# escrever o nome de cinco pessoas e os mostre na tela.

nomes = []

for i in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome)

print("Minha lista de nomes eh ", nomes)
