from funciones import (mostrar_menu,
                    leer_opcion, 
                    agregar_libro,
                    eliminar_libro,
                    buscar_libro,
                    actualizar_disponibilidad,
                    mostrar_libros)


libros = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("Ingrese título a buscar: ")
        pos = buscar_libro(libros, titulo)

        if pos != -1:
            libro = libros[pos]
            print("\nLibro encontrado:")
            print(libro)
        else:
            print("No encontrado")

    elif opcion == 3:
        eliminar_libro(libros)

    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break

