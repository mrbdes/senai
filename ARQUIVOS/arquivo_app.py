# escrita de arquivos
def main():
    pessoas = ["Ana", "Joao", "Bia", "jose"]
    salarios = [5000, 2300, 6200, 9000]

    arquivo = open("texto.txt", "w+")
# arquivo texto
    for i in range(4):

        arquivo.write(pessoas[i])
        arquivo.write("\tSalario: ")
        arquivo.write(str(salarios[i]))
        arquivo.write("\n")

    # Fechar o arquivo quando finalizar as alteraçoes
    arquivo.close()


if __name__ == "__main__":
    main()
