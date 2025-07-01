### Strings ###
my_str = "Mi String"
my_other_str = 'Mi otro string'

print(len(my_str))
print(len(my_other_str))
print(my_str + " " + my_other_str)

my_new_line_str = "Este es un String\ncon salto de linea"
print(my_new_line_str)

my_tab_str = "\tEste es un String con tabulación"
print(my_tab_str)

my_scape_str = "\\tEste es un String \\n escapado"
print(my_scape_str)

# Formateo
name, surname, age = "Juan", 'Garcia', 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language
print(a, b, c, d, e, f)
print(a, b, c, d, e, f, sep='-')

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
language_slice = language[::-1]
print(language_slice)

# Funciones del lenguaje
print(language.capitalize()) # Primera letra en mayúscula
print(language.upper()) # Todo en mayúsculas
print(language.count('t')) # Cuantas veces se repite
print(language.isnumeric())
print("1".isnumeric())
print(language.lower()) # Todo en minúsculas
print(language.lower().isupper()) # Todo en minúsculas y verifica si es mayúsculas
print(language.startswith("Py"))
print("Py" == "py") # No es lo mismo
