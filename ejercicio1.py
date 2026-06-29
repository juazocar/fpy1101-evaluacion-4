def validar_titulo(titulo):
    return titulo.strip() != ""


def validar_copias(copias_str):
    try:
        valor = int(copias_str)
        return valor >= 0
    except ValueError:
        return False


def validar_prestamo(prestamo_str):
    try:
        valor = int(prestamo_str)
        return valor > 0
    except ValueError:
        return False


def mostrar_menu():
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar un número entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número entero.")


def agregar_libro(libros):
    titulo = input("Ingrese el título del libro: ")
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío.")
        return

    copias_input = input("Ingrese cantidad de copias: ")
    if not validar_copias(copias_input):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_input = input("Ingrese período de préstamo (días): ")
    if not validar_prestamo(prestamo_input):
        print("Error: El préstamo debe ser un número entero mayor que cero.")
        return

    libro = {
        "titulo": titulo,
        "copias": int(copias_input),
        "prestamo": int(prestamo_input),
        "disponible": False
    }

    libros.append(libro)
    print("Libro agregado correctamente.")


def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1


def eliminar_libro(libros):
    titulo = input("Ingrese el título del libro a eliminar: ")
    posicion = buscar_libro(libros, titulo)

    if posicion != -1:
        libros.pop(posicion)
        print("Libro eliminado correctamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")


def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False
    print("Disponibilidad actualizada.")


def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    if len(libros) == 0:
        print("No existen libros registrados.")
        return

    print("Lista de libros")
    for libro in libros:
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")

        if libro["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")
        print("*********************************************")


libros = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("Ingrese el título a buscar: ")
        posicion = buscar_libro(libros, titulo)

        if posicion != -1:
            print("\nLibro encontrado")
            print(f"Posición: {posicion}")
            print(f"Título: {libros[posicion]['titulo']}")
            print(f"Copias: {libros[posicion]['copias']}")
            print(f"Préstamo: {libros[posicion]['prestamo']}")

            if libros[posicion]["disponible"]:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN COPIAS")
        else:
            print("Libro no encontrado.")

    elif opcion == 3:
        eliminar_libro(libros)

    elif opcion == 4:
        actualizar_disponibilidad(libros)

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break