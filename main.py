
#IMPORTACION DE LOS MODULOS DRAGONBOUND, MATH, TIME
from dragonbound import limpiar_pantalla, draw_world, draw_world_empty, print_world, calculate_velocity, draw_missile_launch, finish_game
from math import radians
from time import sleep

#Variable general
mundo = []

while True:
    entrada = input('Escribe init para cargar el mapa: ')
    limpiar_pantalla()
    sleep(0.5)

    if entrada  == 'init':
        print('Welcome to the world of dragonbound 2d xyz',)
        print()
        mundo_vacio = draw_world_empty(mundo)
        mapa = draw_world(mundo_vacio)
        print_world(mapa)

        accion = input('Input Exit (E) or Launch (L): ')

        if accion == 'L':
            player = input('Imput player: ')

            if player == 'A':
                angulo = int(input('Ingresa el angulo de tiro [1-70]: '))
                angulo_rad = radians(angulo)
                limpiar_pantalla()
                sleep(0.5)

                mundo_vacio = draw_world_empty(mundo)
                mapa = draw_world(mundo_vacio)

                velocidad_inicial = calculate_velocity(angulo_rad)
                draw_missile_launch(velocidad_inicial, angulo_rad, mapa, player)
                finish_game(player)

                accion = input('Input Exit (E) or Launch (L): ')

                if accion == 'E':
                    break


            else:
                angulo = int(input('Ingresa el angulo de tiro [1-70]: '))
                angulo_rad = radians(angulo)
                limpiar_pantalla()
                sleep(0.5)

                #Modificacion del mapa
                mundo_vacio = draw_world_empty(mundo)
                mapa = draw_world(mundo_vacio)

                velocidad_inicial = calculate_velocity(angulo_rad)
                draw_missile_launch(velocidad_inicial, angulo_rad, mapa, player)
                finish_game(player)

                accion = input('Input Exit (E) or Launch (L): ')

                if accion == 'E':
                    break

        if accion == 'E':
            break
    else:
        print('Ingrese la palabra correcta para cargar el mapa.')



