#FUNCIONES DE MENÚ
def mostrar_menu():
    print("\n========= MENÚ PRINCIPAL =========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("===================================")

def leer_opcion():
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if 1 <= op <= 6:
                return op
            else:
                print("Opción inválida")
        except:
            print("Debe ingresar un número")

#VALIDACIONES
def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias):
    return copias >= 0

def validar_prestamo(prestamo):
    return prestamo > 0

#OPCIÓN 1
def agregar_libro(libros):
    print("\n--- Agregar libro ---")
    
    titulo = input("Ingrese título: ")
    if not validar_titulo(titulo):
        print("Error: título inválido")
        return

    try:
        copias = int(input("Ingrese copias: "))
        if not validar_copias(copias):
            print("Error: copias inválidas")
            return
    except:
        print("Error: debe ser número")
        return

    try:
        prestamo = int(input("Ingrese días de préstamo: "))
        if not validar_prestamo(prestamo):
            print("Error: préstamo inválido")
            return
    except:
        print("Error: debe ser número")
        return

    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False
    }

    libros.append(libro)
    print("Libro agregado correctamente")

#OPCIÓN 2
def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1

#OPCIÓN 3
def eliminar_libro(libros):
    titulo = input("Ingrese título a eliminar: ")
    pos = buscar_libro(libros, titulo)

    if pos != -1:
        libros.pop(pos)
        print("Libro eliminado")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

#OPCIÓN 4
def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False

#OPCIÓN 5
def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    print("\n=== LISTA DE LIBROS ===")

    if len(libros) == 0:
        print("No hay libros registrados")
        return

    for libro in libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"

        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("=== oooo ===")