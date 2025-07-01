### Variables ###

my_str = "My String"
print(my_str)

my_int = 5
print(my_int)

my_int_to_str = str(my_int)
print(my_int_to_str)
print(type(my_int_to_str))

my_bool = False
print(my_bool)

# Concatenación de variables
print(my_str, my_int_to_str, my_bool)
print("Este es el valor de: ", my_bool)

# Algunas funciones del sistema
print(len(my_str))

# Variables en una sola linea. Cuidado de abusar de esta sintaxis!
name, surname, alias, age = "Juan", "Garcia", "Juanito", 23
print("Me llamo:", name, surname,
    ". Mi edad es:", age,
    ". Y mi alias es:", alias)

# Inputs
name = input("Cual es tu nombre? ")
age = input("Cuantos años tienes? ")
print(name)
print(age)

# Cambiamos el tipo
name = 23
age = "Juan"
print(name)
print(age)

# forzamos el tipo
address: str = "Mi direccion"
address = True
address = 5
address = 1.2
print(type(address))
