import os
from tkinter.filedialog import askdirectory
def main():
# Local da pasta 
  caminho = askdirectory(title="Selecione uma pasta")
  print(caminho)
# listar os arquivos de pasta
lista_arquivos = os.listdir(caminho) 
print(lista_arquivos)
local ={
    "documentos": ["docx","doc"],
    ~"panilhas": [".xlsx", ".xls", "csv"],
    "texto": ["txt"],
    "pdf":[".pdf"],
    "imagens":[".jpg", ".png", ".jpeg",".bmp"]
    }
for arquivos in lista_arquivos:

nome, extensao = os.patch.splitxt(f"{caminho}/{arquivo}"}
for pasta in locais:
    if extensao in locais[pasta]:

        if not os.path.exists(f"{caminho}/{pasta}")
        os.mkdir(f"{caminho}/{pasta}")
        os.rename(
          f"{caminho}/{arquivo}",
          f"{caminho}/{pasta}/{arquivo}",
        )
