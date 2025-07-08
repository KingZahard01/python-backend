class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.name = nombre
        self.age = edad
        self.grade = grado

    def estudiar(self):
        return f"El estudiante {self.name} está estudiando"

get_name = input("Ingresa tu nombre: ")
get_age = input("Ingresa tu edad: ")
get_grade = input("Ingresa tu grado: ")

estudiante1 = Estudiante(get_name, get_age, get_grade)

estudiar = input("Escribe estudiar...: ")
if estudiar.lower() == "estudiar":
    print(estudiante1.estudiar())
