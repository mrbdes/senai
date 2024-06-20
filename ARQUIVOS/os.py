# os - operating system ou sistema operacional
# pastas (diretorios)
#  locais ( caminhos / path)

import os

from datetime import date

def main():

    diretorio = "C:\Temp"
    arquivo = os.listdir(diretorio)

    for arq in arquivo:
        print(arq)
# nova_pasta ="E: /Temp/Python313"
# cria uma nova pasta/diretorio
data_hoje = str(date.today())
nova_pasta = "E:/Temp/" + data_hoje
nova_pasta = "E:/Temp/2024-05-17"
os.makedirs(nova_pasta)

