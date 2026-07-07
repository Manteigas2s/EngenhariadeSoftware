class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)

    def fechar_porta(self):
        print("As portas do carro foram fechadas.")

    def abrir_porta(self):
        print("As portas do carro foram abertas.")



carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Ford", "Mustang")


carro1.descrever()
carro1.abrir_porta()
carro1.fechar_porta()

print()

carro2.descrever()
carro2.abrir_porta()
carro2.fechar_porta()