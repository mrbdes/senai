# variavel do tipo lista
lista_de_frutas = ["maçã", "banana", "laranja", "uva"]

# variavel do tipo tupla
tupla_de_cores = ("vermelho", "azul", "verde", "amarelo")

# variavel do tipo dicionario
dicionario_de_pessoas = {
    "nome", "alice",
    "idade:", 25,
    "cidade:", "Mauá"}


# exibindo os valores das variaveis
print("minha lista de frutas :", lista_de_frutas)
print("tupla de cores ", tupla_de_cores)
print("dicionario de pessoas", dicionario_de_pessoas)

# acessando elementos especificos
print("A segunda fruta da minha lista eh:", lista_de_frutas[1])
print("A cor verde esta ma tupla", "verde" in tupla_de_cores)
print(" A cor azul esta na tupla ", "azul" in tupla_de_cores)
print("O segundo elemento da minha tupla eh", tupla_de_cores[1])


print("A idade de ",
      dicionario_de_pessoas["nome"], "eh", dicionario_de_pessoas["idade"])
