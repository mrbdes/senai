class Carro:
    # Caracteristicas
    ano = 0
    marca = ""
    modelo = ""
    
    # Metodo construtor: executado automaticamente quando projeto é criado
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Funcionalidades ( funções = > metodos)
    def imprimirDados(self):
        print(f"A marca do meu carro ef {self.marca} e o modelo eh {self.modelo}")