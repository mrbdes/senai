# Desenvolver um promgrama para uma loja de lanches (Mac)
# Requisitos:
# - O usuario vai receber uma mensagem de boas vindas
# - Sistema irá retornar o nome lanche e o valor dele
# - Usar pelo menos 4 opçoes de lanche
# - Para resolver usar listas

print (f"Ola, Seja Bem Vindo MC!!")
lanches = ["Big Mac{$4,00}", "Quarteirao{$5,00}", "Mc Cheddar{$6,00}", "Duplo Quarterão{$7,00}",]
bebida = ["Coca Cola{$4,00}", " Fanta{$5,00}", " Suco de Uva{$6,00}", "Guarana{$7,00}",]
sorvete = ["Creme{$4,00}", " Chocolate{$5,00}", "Caramelo{$6,00}", "Morango{$7,00}",]

opcao = int(input("Qual é sua opcao de lanche? "))
opcao = int(input("Qual é sua opcao de bebida? "))
opcao = int(input("Qual é sua opcao de sorvete? "))

print("Voce escolheu o ", lanches[opcao-1])
print("Voce escolheu a ", bebida [opcao-1])
print("Voce escolheu a ", sorvete [opcao-1])