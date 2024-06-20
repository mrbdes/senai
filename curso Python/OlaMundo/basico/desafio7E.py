# Faixa de numeros: Peça ao usuário para inserir um número inicial e
# final e mostre o intervalo de números
# caso o usuario digite invertido, seu programa deve corrigir

num_inicial = int(input("Digite um numero inicial: "))
num_final = int(input("Digite o numeor final: "))

# SOLUCAO 1
# if num_inicial < num_final:
#     for num in range(num_inicial, num_final+1):
#         print(num)
# else:
#     for num in range(num_final, num_inicial+1):
#         print(num)

# SOLUCAO 2
# if num_inicial > num_final:
#     aux = num_inicial
#     num_inicial = num_final
#     num_final = aux

# for num in range(num_inicial, num_final+1):
#     print(num)


# SOLUCAO 3 - SOMENTE EM PYTHON
if num_inicial > num_final:
    num_inicial, num_final = num_final, num_inicial

for num in range(num_inicial, num_final+1):
    print(num)
