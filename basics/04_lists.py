### Lists ###

# Definición
my_list = list()
my_other_list = []
print(len(my_list))

my_list = [23, 12, 34, 45, 56]
print(my_list)
print(len(my_list))

my_other_list = [23, 1.65, "Juan", "Garcia"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y busqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # Cuantas veces aparece el número 30 en la lista
# print(my_other_list[4]) # IndexError
# print(my_other_list[-5]) # IndexError

print(my_other_list.index("Juan"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2]
print(age)

# Concatenación
print(my_list + my_other_list)
# print(my_list - my_other_list) # TypeError

# Creación, Inserción, Actualización y Eliminación (CRUD)
my_other_list.append("JuanitoDev") # Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Agrega un elemento en la posición 1
print(my_other_list)

my_other_list[1] = "Azul" # Actualiza el elemento en la posición 1
print(my_other_list)

my_other_list.remove("Azul") # Elimina el elemento con el valor "Azul" de la lista
print(my_other_list)

my_list.remove(12) # Elimina el elemento con el valor 12 de la lista
print(my_list)

print(my_list.pop()) # Elimina el último elemento de la lista
print(my_list)

# my_pop = my_list.pop(2) # Elimina el elemento en la posición 2
# print(my_pop)
print(my_list)

del my_list[1] # Elimina el elemento en la posición 1
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy() # Crea una copia de la lista
my_list.clear() # Elimina todos los elementos de la lista

print(my_list)
print(my_new_list)

my_new_list.reverse() # Invierte el orden de los elementos en la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos en la lista de forma ascendente
print(my_new_list)

my_new_list.sort(reverse=True) # Ordena los elementos en la lista de forma descendente
print(my_new_list)

# Sublistas
print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))
