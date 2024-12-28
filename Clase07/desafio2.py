# Lista para almacenar las tareas pendientes
lista_tarea = [] # [1,2,3]

# Bucle principal
while True:
    # Menu de opciones
    print()
    print("-"*30)
    print("Menú principal")
    print("-"*30)
    print("1. Agregar una tarea.")
    print("2. Eliminar una tarea.")
    print("3. Mostrar todas las tareas.")
    print("4. Eliminar todas las tareas.")
    print("5. Salir.")
    print()

    opcion = input("Elija una opcion [1..5]: ").strip()

    # Procesamos la opcion 1:
    if opcion == "1":
        tarea = input("Ingrese la tarea: ").strip()
        lista_tarea.append(tarea)
        print("Tarea agregada:",tarea )
    else:
        # procesamos la opcion 2
        if opcion == "2":
            num_tarea = int(input("Ingrese el número de la tarea a ELIMINAR: ").strip())
            # Aseguramos que la tarea exista
            if num_tarea <= len(lista_tarea):
                aux = lista_tarea.pop(num_tarea - 1)
                print("Tarea eliminada:", aux)
            else:
                print("No existe esa tarea.")
        else:
            # procesamos la opcion 3
            if opcion == "3":
                if lista_tarea: # Ver si hay tareas
                    indice = 1
                    for tarea in lista_tarea:
                        print(indice,"-",tarea)
                        indice += 1
                else:
                    print("No tienes tareas pendientes.")
            else:
                # procesamos la opcion 4
                if opcion == "4":        
                    lista_tarea.clear()
                    print("Lista limpiada.")
                else:
                    # procesamos la opcion 5
                    if opcion == "5":
                        print("Programa finalizado.")  
                        break
                    else:
                        print("Opción no válida!")