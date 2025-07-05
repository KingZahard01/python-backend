### Loops ###

# While
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual a 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 25:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("La ejecución continúa")

# For
my_list = [35, 23, 34, 45, 56, 7, 23]
for element in my_list:
    print(element)

my_tuple = (23, 1.66, "Juan", "Garcia", "Juan")
for element in my_tuple:
    print(element)

my_set = {"Juan", "Garcia", 23}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Juan",
    "Apellido": "Garcia",
    "Edad": 23,
    1: "Python"
}
for element in my_dict:
    print(element)
    if element == 'Edad':
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print("Se ejecuta")
else:
    print("El bucle for para el diccionario ha finalizado")
