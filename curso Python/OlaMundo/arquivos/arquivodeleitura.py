# Leitura e Escrita de Arquivos

def main():

    # Leitura de arquivo
    # Read
    arquivo = open("texto.txt", "r")

    if arquivo.mode == 'r':  # Arquivo foi realmente aberto
        # conteudo = arquivo.read()
        # print(conteudo)
        # readlines ler linhas individualmete dentro de uma lista
        linhas = arquivo.readlines()
        # for l in linhas:
        #     print(l)
        print(linhas)

    # Fechar o arquivo quando finalizar as alteraçoes
    arquivo.close()


if __name__ == "__main__":
    main()
