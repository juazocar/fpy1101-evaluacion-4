# fpy1101-evaluacion-4

Este repositorio contiene la solución del ejercicio 4 del curso `FPY1101`.

## Descripción general

`ejercicio1.py` es un programa de consola para administrar una colección de libros. El usuario puede agregar nuevos libros, buscar un libro por título, eliminar registros existentes, actualizar la disponibilidad y listar todos los libros registrados.

La información de cada libro se almacena en una lista de diccionarios en memoria con estos campos:

- `titulo`: nombre del libro.
- `copias`: cantidad de copias disponibles.
- `prestamo`: duración del préstamo en días.
- `disponible`: valor booleano que indica si el libro tiene al menos una copia disponible.

## Cómo funciona

1. El programa muestra un menú con seis opciones.
2. El usuario elige una opción ingresando un número.
3. El programa ejecuta la acción correspondiente sobre la colección interna de libros.
4. El menú se repite hasta que el usuario selecciona `6. Salir`.

## Funcionalidad principal

- `mostrar_menu()`: imprime las opciones disponibles.
- `leer_opcion()`: lee y valida la entrada del usuario como entero.
- `validar_titulo(titulo)`: verifica que el título no esté vacío ni sea solo espacios.
- `validar_copias(copias_str)`: valida que la cantidad de copias sea un entero mayor o igual a cero.
- `validar_prestamo(prestamo_str)`: valida que el período de préstamo sea un entero mayor que cero.
- `agregar_libro(lista_libros)`: solicita datos del libro, valida los campos y lo agrega a la lista.
- `buscar_libro(lista_libros, titulo_buscar)`: busca un libro por título y devuelve su índice o `-1` si no existe.
- `eliminar_libro(lista_libros)`: solicita un título y elimina el libro encontrado.
- `actualizar_disponibilidad(lista_libros)`: recorre todos los libros y marca `disponible` como `True` si tiene al menos una copia.
- `mostrar_libros(lista_libros)`: actualiza la disponibilidad y muestra cada libro con su estado.

## Uso

Ejecuta el programa desde la terminal:

```bash
python ejercicio1.py
```

A continuación, elige una opción del menú:

1. Agregar libro
2. Buscar libro
3. Eliminar libro
4. Actualizar disponibilidad
5. Mostrar libros
6. Salir

## Ejemplo de flujo

- Si se agrega un libro con 3 copias y préstamo de 7 días, ese libro se registra con `disponible = False` inicialmente y luego se actualiza a `True` cuando se muestra la lista o se actualiza la disponibilidad.
- Si se busca un libro, el sistema compara los títulos sin distinguir mayúsculas/minúsculas.
- Si se ingresa un título vacío o datos no numéricos válidos, se muestra un mensaje de error y no se agrega el libro.

## Requisitos

- Python 3.x

## Observaciones

- Los datos se almacenan solo en memoria durante la ejecución; al cerrar el programa se pierde la colección.
- `disponible` depende únicamente de la cantidad de copias.
- El menú permite interactuar de forma sencilla y mantiene el flujo hasta que el usuario elige salir.
