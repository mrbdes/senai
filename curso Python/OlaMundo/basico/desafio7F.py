# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
    num = int(input("Numero: "))
    numeros.append(num)

print(numeros)
maior = 0

for num in numeros:
    if maior < num:
        maior = num

print(maior)
