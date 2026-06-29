

def mostrar_menu():
    print("\n= MENÚ PRINCIPAL =")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")



def leer_opcion():
    #Lee y retorna la opción elegida por el usuario validando que sea numérica.
    try:
        opcion = int(input("Seleccione una opción (1-6): "))
        return opcion
    except ValueError:
        return -1  




def validar_titulo(titulo):
    #Retorna True si el título no está vacío ni contiene solo espacios.
    return len(titulo.strip()) > 0


def validar_copias(copias_str):
# """Retorna True si es un entero válido mayor o igual a cero."""
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




def agregar_libro(lista_libros):
    print("\n Registra Nuevo Libro ")
    titulo = input("Ingrese el título del libro: ")
    
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni contener solo espacios.")
        return

    copias_raw = input("Ingrese la cantidad de copias: ")
    if not validar_copias(copias_raw):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_raw = input("Ingrese el período de préstamo (en días): ")
    if not validar_prestamo(prestamo_raw):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    
    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_raw),
        "prestamo": int(prestamo_raw),
        "disponible": False  
    }
    
    lista_libros.append(nuevo_libro)
    print(f"¡Libro '{nuevo_libro['titulo']}' registrado con éxito!")


def buscar_libro(lista_libros, titulo_buscar):
    for i in range(len(lista_libros)):
        if lista_libros[i]["titulo"].lower() == titulo_buscar.strip().lower():
            return i
    return -1


def eliminar_libro(lista_libros):
    
    print("\n--- Eliminar Libro ---")
    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")
    
    posicion = buscar_libro(lista_libros, titulo_eliminar)
    
    if posicion != -1:
        libro_eliminado = lista_libros.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' ha sido eliminado exitosamente.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")


def actualizar_disponibilidad(lista_libros):
    #"""Recorre todos los libros y actualiza el estado según la cantidad de copias."""
    for libro in lista_libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False


def mostrar_libros(lista_libros):
    #"""Actualiza la disponibilidad de los libros y los muestra formateados."""
    actualizar_disponibilidad(lista_libros)
    
    print("\n LISTA DE LIBROS ")
    if not lista_libros:
        print("No hay libros registrados en el sistema")
        return
        
    for libro in lista_libros:
        estado_str = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado_str}")




def main():
    coleccion_libros = []
    
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if opcion == 1:
            agregar_libro(coleccion_libros)
            
        elif opcion == 2:
            print("\nBuscar Libro ")
            titulo_búsqueda = input("Ingresa título del libro a buscar: ")
            posicion = buscar_libro(coleccion_libros, titulo_búsqueda)
            
            if posicion != -1:
                actualizar_disponibilidad(coleccion_libros)
                
                libro = coleccion_libros[posicion]
                estado_str = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print(f"\n[Libro Encontrado en la posición {posicion}]")
                print(f"Título: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Préstamo: {libro['prestamo']}")
                print(f"Estado: {estado_str}")
            else:
                print("El libro no se encuentra registrado.")
                
        elif opcion == 3:
            eliminar_libro(coleccion_libros)
            
        elif opcion == 4:
            actualizar_disponibilidad(coleccion_libros)
            print("\nDisponibilidad de todos los libros actualizada correctamente.")
            
        elif opcion == 5:
            mostrar_libros(coleccion_libros)
            
        elif opcion == 6:
            print("\nGracias por usar el sistema.")
            break
            
        else:
            print("seleccione un número del 1 al 6.")



if __name__ == "__main__":
    main()