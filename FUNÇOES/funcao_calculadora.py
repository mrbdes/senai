# Exercício Funções
# Criar as funções main() e as demais funções para criar uma
# calculadora com as operações +, -, /, * .
# As funções deverão realizar somente o calculo
# O usuário devera digitar 2 números e a operação que deseja realizar
# OBS.: seu código deverá bloquear a divisão por zero

# Criar as funções para calculo
def somarNumeros(n1, n2):
    res = n1 + n2
    return res
    
def subtrairNumeros(n1, n2): 
    res = n1 - n2
    return res

def multiplicarNumeros(n1, n2):
    res = n1 * n2
    return res

def dividirNumeros(n1, n2):   
    res = n1 / n2
    return res

def main():

    print("Olá, bem vindo a Calculadora SENAI")
    num1 = int(input("Digite o primeiro numero para calculo"))
    num2 = int(input("Digite o segundo numero para calculo"))
    operacao = input("Digite a operacao a ser calculada")

if __name__ == "__main__":
    main()

def soma(num1, num2):
    res = num1 + num2
    return res


def subtracao(num1, num2):
    res = num1 - num2
    return res


def multiplicao(num1, num2):
    res = num1 * num2
    return res


def divisao(num1, num2):
    try:
        res = num1 / num2
        return res
    except ZeroDivisionError
    print("Erro: Nao eh possivel fazer divisao por zero!!!")
    else:
        print("operacao invalida!")
    return res