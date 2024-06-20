# ESTRUTURA DE REPETIÇÃO

frutas = ("pera","maça", "banana", "melancia", "laranja", "abacaxi", "limão",)

# estrutura de repetição por

print(frutas)

for i in range(3,6):
    print(i,"-", frutas[i])

for fruta in frutas:
    print(fruta)

valor = 0
resultado = 0
multiplo = 0
while valor <=10:
    print(f"{multiplo} x {valor} = {resultado}")
    valor += 1
    resultado += multiplo
