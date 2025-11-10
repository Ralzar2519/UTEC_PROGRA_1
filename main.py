import dragonbound
from math import radians
mundo = []

palabra_clave = input('Escribe init para cargar el mapa: ')

def init_game(entrada):
    """
    Genera resultados en funcion de la frase que ingresa el usuario.

    Args:
        entrada: dato string que representa lo que usuario ha escrito en consola

    Returns:
        Si el usuario ingresa la palabra init, se imprime la bienvenida al mundo junto con el mapa
        Si el usario ingresa una palabra diferente a 'init' entonces se le pide que ingrese la palabra correcta mediante la
        recursividad del funcion
    """
    if entrada == 'init':
        print('Welcome to the world of dragobound 2d xyz')
        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)
        dragonbound.print_world(mapa)
        return True

    else:
        print('Ingrese la palabra correcta para cargar el mapa')
        init_game(palabra_clave)

#Evita crear una estructura de control (if-else) muy extenso
if init_game(palabra_clave) == True:
    accion = input ( 'Input Exit (E) or Launch (L): ')

    if accion == 'L':
        print('Turno jugador A')
        player = 'A'
        angulo = int(input('Ingresa el angulo de tiro[0-70]: '))
        angulo_rad = radians(angulo)

        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)

        velocidad_inicial = dragonbound.calculate_velocity(angulo_rad)
        dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa,player)

    else:
        print('Turno jugador B')
        player = 'B'
        angulo = int(input('Ingresa el angulo de tiro: '))
        angulo_rad = radians(angulo)

        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)

        velocidad_inicial = dragonbound.calculate_velocity(angulo_rad)
        dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa,player)


