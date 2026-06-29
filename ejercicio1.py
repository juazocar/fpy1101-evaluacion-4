
lista_libros = []


def validar_titulo(titulo):
    """Valida que el título no esté vacío ni sea solo espacios."""
    return len(titulo.strip()) > 0


def validar_copias(copias_str):
    """Valida que las copias sean un entero mayor o igual que cero."""
    if not copias_str.isdigit():
        return False
    return int(copias_str) >= 0


def validar_prestamo(prestamo_str):
    """Valida que el período de préstamo sea un entero mayor que cero."""
    if not prestamo_str.isdigit():
        return False
    return int(prestamo_str) > 0


def mostrar_menu():
    """Muestra las opciones del menú en pantalla. No recibe ni retorna nada."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """Lee y valida la opción del menú. Retorna un entero entre 1 y 6."""
    opcion = input("Seleccione una opción (1-6): ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
        print("Opción inválida. Ingrese un número entre 1 y 6.")
        opcion = input("Seleccione una opción (1-6): ")
    return int(opcion)


def agregar_libro(lista):
    """
    Solicita los datos del libro al usuario, valida cada campo
    e incorpora el registro a la lista solo si todos son válidos.
    Recibe la lista como parámetro (IE 22).
    """
    print("\n--- Agregar Libro ---")

    titulo = input("Ingrese el título del libro: ")
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni contener solo espacios.")
        return

    copias_str = input("Ingrese la cantidad de copias (número entero >= 0): ")
    if not validar_copias(copias_str):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_str = input("Ingrese el período de préstamo en días (número entero > 0): ")
    if not validar_prestamo(prestamo_str):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_str),
        "prestamo": int(prestamo_str),
        "disponible": False
    }

    lista.append(libro)
    print(f"Libro '{libro['titulo']}' registrado exitosamente.")


def buscar_libro(lista, titulo):
    """
    Recorre la lista buscando un libro por título exacto.
    Retorna la posición (índice) si lo encuentra, o -1 si no existe.
    Recibe la lista y el título como parámetros (IE 22).
    """
    for indice in range(len(lista)):
        if lista[indice]["titulo"] == titulo:
            return indice
    return -1


def eliminar_libro(lista):
    """
    Solicita el título del libro a eliminar.
    Invoca la función de búsqueda para localizarlo (no duplica lógica).
    Recibe la lista como parámetro (IE 22).
    """
    print("\n--- Eliminar Libro ---")
    titulo = input("Ingrese el título del libro a eliminar: ")

    posicion = buscar_libro(lista, titulo)

    if posicion != -1:
        lista.pop(posicion)
        print(f"El libro '{titulo}' fue eliminado correctamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")



def actualizar_disponibilidad(lista):
    """
    Recorre todos los registros y actualiza el campo 'disponible'
    según la cantidad de copias de cada libro.
    Recibe la lista como parámetro (IE 22).
    """
    for libro in lista:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False


def mostrar_libros(lista):
    """
    Primero actualiza la disponibilidad de todos los libros,
    luego muestra cada registro con el formato indicado.
    Recibe la lista como parámetro (IE 22).
    """
    print("\n=== LISTA DE LIBROS ===")

    if len(lista) == 0:
        print("No hay libros registrados.")
        return

    actualizar_disponibilidad(lista)

    for libro in lista:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("*" * 45)



def opcion_buscar_libro(lista):
    """
    Solicita el título, invoca buscar_libro y muestra el resultado.
    El programa principal decide qué hacer con el valor retornado (IE 8).
    Recibe la lista como parámetro (IE 22).
    """
    print("\n--- Buscar Libro ---")
    titulo = input("Ingrese el título del libro a buscar: ")

    posicion = buscar_libro(lista, titulo)

    if posicion != -1:
        libro = lista[posicion]
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"\nLibro encontrado en la posición {posicion}:")
        print(f"  Título   : {libro['titulo']}")
        print(f"  Copias   : {libro['copias']}")
        print(f"  Préstamo : {libro['prestamo']} días")
        print(f"  Estado   : {estado}")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")


def main():
   
    while True:
        # IE 20: Se invocan mostrar_menu y leer_opcion en cada iteración
        mostrar_menu()
        opcion = leer_opcion()

        # IE 21: Lógica del programa principal que dirige a cada función
        if opcion == 1:
            agregar_libro(lista_libros)
        elif opcion == 2:
            opcion_buscar_libro(lista_libros)
        elif opcion == 3:
            eliminar_libro(lista_libros)
        elif opcion == 4:
            actualizar_disponibilidad(lista_libros)
            print("Disponibilidad actualizada correctamente.")
        elif opcion == 5:
            mostrar_libros(lista_libros)
        elif opcion == 6:
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break


main()