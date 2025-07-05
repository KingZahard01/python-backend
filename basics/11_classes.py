### Classes ###

# Definición
class MyEmptyPerson:
    pass # Para poder dejar la clase vacía

print(MyEmptyPerson)

# Clase con constructor, funciones y propiedades privadas y públicas
class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # propiedad pública
        self.__name = name # propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Juan", "Garcia")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Juan", "Garcia", "JuanitoDev")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
