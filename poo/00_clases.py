### Clases y Objetos ###

class Celular: # se usa PascalCase
    def __init__(self, marca, modelo, color): # constructor
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # acciones del celular
    def llamar(self): # metodo es una funcion dentro de la clase
        return f"Llamando... desde {self.marca} {self.modelo}"

    def colgar(self):
        return f"Colgando la llamada... desde {self.marca} {self.modelo}"

# instancia del objeto Celular
celular1 = Celular("Samsung", "Galaxy S21", "Negro")
print(celular1.color)
print(celular1.llamar())
print(celular1.colgar())

celular2 = Celular("Apple", "iPhone 13", "Blanco")
print(celular2.color)
print(celular2.llamar())
print(celular2.colgar())
