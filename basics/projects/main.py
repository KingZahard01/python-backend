"""
Gestor de tareas CLI:
Agregar, editar, eliminar y listar tareas con prioridad y estado.

1. Agregar una tarea nueva.
2. Editar una tarea existente.
3. Eliminar una tarea existente.
4. Listar todas las tareas.
5. Asignar prioridad a una tarea.
6. Asignar estado a una tarea.
"""

# Almacena las tareas
tareas = []

def menu():
    """Muestra el menú de inicio"""
    print("\nGestor de tareas CLI")
    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Eliminar tarea")
    print("4. Ver todas las tareas")
    print("5. Salir")

def agregar_tarea():
    """Añade una nueva tarea a la lista"""
    titulo = input("titulo de la tarea: ")
    new_tarea = {
        'titulo': titulo,
        'prioridad': 'media', # valor por defecto
        'estado': 'pendiente' # valor por defecto
    }
    tareas.append(new_tarea)
    print(f"Tarea '{titulo}' agregada con éxito!")

def listar_tareas():
    """Muestra todas las tareas"""
    if not tareas:
        print('No hay tareas.')
    else:
        print('Lista de tareas:')
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea['titulo']} - {tarea['prioridad']} - {tarea['estado']}")

def editar_tarea():
    """Modifica una tarea"""
    listar_tareas()
    if not tareas:
        return
    else:
        try:
            num = int(input('Numero de tarea a editar: ')) -1
            if 0 <= num < len(tareas):
                print(f"Editando: {tareas[num]['titulo']}")
                tareas[num]['titulo'] = input("Nuevo titulo: ") or tareas[num]['titulo']
                tareas[num]['prioridad'] = input("Nueva prioridad (alta/media/baja): ") or tareas[num]['prioridad']
                tareas[num]['estado'] = input("Nuevo estado (pendiente/en progreso/completada): ") or tareas[num]['estado']

                print("Tarea actualizada!")
            else:
                print("Numero invalido")
        except ValueError:
            print("Debes ingresar un numero valido")

def eliminar_tarea():
    """Eliminar una tarea"""
    listar_tareas()
    if not tareas:
        return
    else:
        try:
            num = int(input('Numero de tarea a eliminar: ')) -1
            if 0 <= num < len(tareas):
                tarea_eliminada = tareas.pop(num)
                print(f"Tarea {tarea_eliminada['titulo']} eliminada con exito!")
            else:
                print("Número inválido")
        except ValueError:
            print("Debes ingresar un numero valido")

# Programa
while True:
    menu()
    opcion = int(input("\nElige una opcion (1-5): "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        editar_tarea()
    elif opcion == 3:
        eliminar_tarea()
    elif opcion == 4:
        listar_tareas()
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
