
# módulo de calculo do imc

def calcularIMC(altura, peso):

    imc = peso /(altura ** 2)
    return imc

# Módelo de mensagen ao usuario do IMC
def imprimirIMC(imc):
    print(f"Ola usuario, seu Imc é {imc}!!!")

# Módulo Mensagen de boas vindas
def imprimirBoasVindas():
    print("************** SISTEMA DE CÁLCULO DO IMC *************")
    print("Olá, seja bem vindo ao sisterma de calculo do IMC")


# módulo principal
def main():

    resultado = calcularIMC(1,80,88)
    resultado = round (resultado,2)

    imprimirIMC (resultado)

if __name__ == "__main__":
   main()
