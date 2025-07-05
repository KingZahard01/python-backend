### Functions ###

# Definition
def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Function con parametros de entrada/argumentos
def sum_two_values(first_value: int, second_value: int):
    print(first_value + second_value)

sum_two_values(5, 6)
sum_two_values(5123, 6234)
sum_two_values('5', '6')
sum_two_values(1.4, 5.2)

# Function con parametros de entrada/argumentos y retorno
def sum_two_values(first_value: int, second_value: int):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values(10, 5.2)
print(my_result)

# Function con parametros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname='Garcia', name='Juan')

# Función con parámetros de entrada/argumentos con defecto
def print_name_with_default(name, surname, alias='Sin alias'):
    print(f'{name} {surname} {alias}')

print_name_with_default('Juan', 'Garcia')
print_name_with_default('Juan', 'Garcia', 'JuanitoDev')

# Función con parámetros de entrada-argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'Python', 'JuanitoDev')
print_upper_texts('Hola')
