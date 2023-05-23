import conversor_svg as conv


def ejecutar_cargar_lista_figuras() -> list:
    ruta = input("Ingrese la ruta del archivo CSV de figuras: ")
    return conv.cargar_lista_figuras(ruta)


def ejecutar_convertir_a_svg(figuras: list) -> None:
    conv.convertir_a_svg(figuras)
    print("Se ha generado el archivo SVG")


def mostrar_menu() -> None:
    print("Menú de opciones:")
    print("1. Cargar lista de figuras")
    print("2. Crear archivo SVG")
    print("3. Salir")


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
