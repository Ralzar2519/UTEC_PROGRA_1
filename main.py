import dragonbound
from dragonbound import draw_missile_launch

mundo = []

palabra_clave = input('Escribe init para cargar el mapa: ')

def init_game(entrada):
    if entrada == 'init':
        print('Welcome to the world of dragobound 2d xyz')
        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)
        dragonbound.print_world(mapa)
        return True

    else:
        print('Ingrese la palabra correcta para cargar el mapa')
        init_game(palabra_clave)
        return False

if init_game(palabra_clave) == True:
    accion = input ( 'Input Exit (E) or Launch (L): ')

    if accion == 'L':
        print(input('Turno jugador A'))
        angulo = int(input('Ingresa el angulo de tiro: '))
        angulo_rad = dragonbound.radianes(angulo)

        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)

        velocidad_inicial = dragonbound.calculate_velocity(angulo)
        dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa)
