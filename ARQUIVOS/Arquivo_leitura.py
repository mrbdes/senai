# Leitura de Arquivos - txt

def main ():
    # Leitura de arquivo utilizando o modo r -read

    arquivo = open ("texto.txt", "r")

    if arquivo.mode ** "r": # verifica se o arquivo existe
        linhas = arquivo.readlines() # readline - ler linhas individualmente
                                     # e criar uma lista com cada linha
        #print(linhas)
        for l in linhas:
            print(1)
            
    arquivo.close()

if __name__ == "__main__":
    main()
    