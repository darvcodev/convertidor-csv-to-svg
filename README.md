# Conversor CSV TO SVG

Este proyecto en Python contiene un conversor de figuras a archivos SVG.

## Descripción

El conversor SVG convierte una lista de figuras en un archivo SVG. Las figuras se cargan desde un archivo CSV y se representan en el archivo SVG con formato adecuado.

El proyecto consta de los siguientes archivos:

- `conversor_svg.py`: Contiene las funciones principales del conversor SVG.
- `interfaz_conversor_svg.py`: Proporciona una interfaz de línea de comandos para interactuar con el conversor.

## Requisitos

- Python 3.x

## Funcionalidades

El proyecto ofrece las siguientes funcionalidades:

1. Cargar lista de figuras desde un archivo CSV.
2. Crear un archivo SVG a partir de la lista de figuras cargadas.
3. Salir del programa.

## Uso

Para utilizar el conversor SVG, sigue los siguientes pasos:

1. Ejecuta el archivo `interfaz_conversor_svg.py`.
2. Se mostrará un menú de opciones.
3. Selecciona la opción correspondiente a la función que deseas ejecutar.
4. Sigue las instrucciones adicionales que se muestran en pantalla.

## Ejemplo de código

A continuación se muestra un fragmento del código principal del proyecto:

```python
import conversor_svg as conv

def iniciar_aplicacion() -> None:
    continuar = True
    lista = None
    while continuar:
        mostrar_menu()
        opcion = int(input("Elija la función a ejecutar: "))
        if opcion == 1:
            lista = ejecutar_cargar_lista_figuras()
        elif opcion == 2:
            ejecutar_convertir_a_svg(lista)
        elif opcion == 3:
            continuar = False
        else:
            print("Selección inválida.")

iniciar_aplicacion()
```

## Licencia
Este proyecto está bajo la Licencia MIT.
