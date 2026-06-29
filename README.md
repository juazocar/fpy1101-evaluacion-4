# fpy1101-evaluacion-4

Este repositorio contiene la solución del ejercicio 4 para el curso `FPY1101`.

## Descripción

El programa implementa un sistema de gestión de libros en consola. Permite:

- Agregar libros con título, cantidad de copias y período de préstamo.
- Buscar libros por título.
- Eliminar libros registrados.
- Actualizar la disponibilidad según la cantidad de copias.
- Mostrar la lista de libros con su estado.

## Archivo principal

- `ejercicio1.py` — contiene la interfaz de menú y las funciones para gestionar la colección de libros.

## Uso

1. Ejecuta el archivo con Python:

```bash
python ejercicio1.py
```

2. Selecciona una opción del menú ingresando un número entre `1` y `6`.

## Requisitos

- Python 3.x

## Notas

- El estado de disponibilidad se calcula automáticamente cada vez que se muestra la lista o se busca un libro.
- El título no puede estar vacío y el número de copias debe ser un entero mayor o igual a `0`.
- El período de préstamo debe ser un entero mayor que `0`.
