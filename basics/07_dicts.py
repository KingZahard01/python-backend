### Dictionaries ###

# Definition
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    'Nombre': 'Juan',
    'Apellido': 'Garcia',
    'Edad': 23,
    1: 'Python'
}

my_dict = {
    'Nombre': 'Juan',
    'Apellido': 'Garcia',
    'Edad': 23,
    'Lenguajes': {'Python', 'Java', 'Typescript'},
    1: 1.65
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print(my_dict[1])
print(my_dict['Nombre'])

print('Juan' in my_dict)
print('Apellido' in my_dict) # busca solo la clave

# Inserción
my_dict['Calle'] = 'Calle Falsa 123'
print(my_dict)

# Actualización
my_dict['Nombre'] = 'Jose'
print(my_dict['Nombre'])

# Eliminación
del my_dict['Calle']
print(my_dict)

# Otras operaciones
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre', 1, 'Piso']

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # crea un nuevo diccionario con las mismas claves que my_list y valores None
my_new_dict = dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict) # crea un nuevo diccionario con las mismas claves y valores None
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict) # crea un nuevo diccionario con las mismas claves que my_dict y valores None
my_new_dict = dict.fromkeys(my_dict, 'JuanitoDev')
print(my_new_dict) # adigna el valor 'JuanitoDev' a todas las claves del diccionario

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
