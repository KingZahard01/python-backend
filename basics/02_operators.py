### Operadores Aritmeticos ###

# Operaciones con enteros
print(3 + 4)  # Suma
print(3 - 4)  # Resta
print(3 * 4)  # Multiplicación
print(3 / 4)  # División
print(3 % 4)  # Módulo
print(3 // 4)  # División entera
print(3 ** 4)  # Exponente
print(3 ** 2 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Que tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5) # 5 veces
print("Hola " * (2 ** 3)) # 8 veces

my_float = 2.5 * 2 # el resultadi es 5.0
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos (lógica booleana) ###
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
