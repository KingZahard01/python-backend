### Conditionals ###

# if
my_condition = False
if my_condition: # es lo mismo que if my_condition == True
    print("Se ejecuta la condición")

my_condition = 5 * 5 # 25
if my_condition == 10:
    print('Se ejecuta el segundo if')

# if, elif, else
if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')
elif my_condition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20 o distinto de 25')

print('La ejecución continúa')

# Condicional con inspección
my_str = ''
if not my_str:
    print('Mi cadena de texto es vacía')

if my_str == 'Mi cadena de texto':
    print('Estas cadenas de texto coinciden')
