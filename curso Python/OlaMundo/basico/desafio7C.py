# Soma de uma faixa de numero: Peça ao usuário para inserir um número
# inicial e final e calcule a soma de todos os números
# UTILIZANDO FOR

num_inicial = int(input("Digite um numero inicial para soma: "))
num_final = int(input("Digite o numeor final da soma: "))

soma = 0

for num in range(num_inicial, num_final+1):
    soma = soma + num

print("A soma dos numeros eh ", soma)
