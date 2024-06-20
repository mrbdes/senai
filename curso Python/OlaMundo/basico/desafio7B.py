# Soma de uma faixa de numero: Peça ao usuário para inserir um número
# inicial e final e calcule a soma de todos os números
# UTILIZANDO WHILE

num_inicial = int(input("Digite um numero inicial para soma: "))
num_final = int(input("Digite o numeor final da soma: "))

num = num_inicial
soma = 0

while num <= num_final:
    soma = soma + num
    num = num + 1
