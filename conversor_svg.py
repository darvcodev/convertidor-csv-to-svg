def cargar_lista_figuras(ruta_archivo: str) -> list:
    figuras = []
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()

        cantidad_figuras = int(lineas[0].strip())

        i = 1
        for _ in range(cantidad_figuras):
            posicion = tuple(map(int, lineas[i].strip().split(',')))
            tamanho = tuple(map(int, lineas[i+1].strip().split(',')))
            esquina = tuple(map(int, lineas[i+2].strip().split(',')))
            grosor = int(lineas[i+3].strip())
            color_interno = tuple(map(int, lineas[i+4].strip().split(',')))
            color_linea = tuple(map(int, lineas[i+5].strip().split(',')))
            rotacion = tuple(map(int, lineas[i+6].strip().split(',')))

            figura = {
                'posicion': posicion,
                'tamanho': tamanho,
                'esquina': esquina,
                'grosor': grosor,
                'color_interno': color_interno,
                'color_linea': color_linea,
                'rotacion': rotacion
            }
            figuras.append(figura)

            i += 7

    return figuras


def rgb_to_hex(color: tuple) -> str:
    """
    Convierte una tupla con un color en RGB a una cadena que representa el color en hexadecimal
    Parámetros:
        color - Tupla que representa un color en el formato (R,G,B)
    Retorno:
        Una cadena con el color en formato hexadecimal
    """
    return "#%02x%02x%02x" % color


def convertir_a_svg(figuras: list) -> None:
    archivo_svg = open('output.svg', 'w')

    archivo_svg.write(
        '<svg height="500px" version="1.1" width="500px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')

    for figura in figuras:
        x, y = figura['posicion']
        ancho, alto = figura['tamanho']
        rx, ry = figura['esquina']
        grosor = figura['grosor']
        color_interno = rgb_to_hex(figura['color_interno'])
        color_linea = rgb_to_hex(figura['color_linea'])
        rotacion = figura['rotacion']

        etiqueta_rect = f'<rect fill="{color_interno}" height="{alto}" rx="{rx}" ry="{ry}" stroke="{color_linea}" stroke-width="{grosor}px" transform="rotate({rotacion[0]}, {x}, {y})" width="{ancho}" x="{x}" y="{y}" />\n'
        archivo_svg.write(etiqueta_rect)

    archivo_svg.write("</svg>\n")
    archivo_svg.close()
