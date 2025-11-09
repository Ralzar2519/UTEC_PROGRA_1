from statistics import variance

import dragonbound
mundo = []
variance = "jbhjghcgghd"

entrada = input('Escribe init para cargar el mapa: ')

def init_game(entrada):
    if entrada == 'init':
        print('Welcome to the world of dragobound 2d xyz')
        mundo_vacio = dragonbound.draw_world_empty(mundo)
        dragonbound.draw_world(mundo_vacio)
        return True

    else:
        print('Ingrese la palabra correcta para cargar el mapa')
        init_game(input('Escribe init para cargar el mapa: '))
        return False

init_game(entrada)

if init_game(entrada) == True:
    accion = input ( 'Input Exit (E) or Launch (L): ')

    if accion == 'E':
        print('Salio del juego')

    else:
        print( '(LAUNCH) Input player : A)' )
