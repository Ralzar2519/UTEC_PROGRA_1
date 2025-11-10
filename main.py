import dragonbound
from math import radians
mundo = []


while True:
    entrada = input('Escribe init para cargar el mapa: ')

    if entrada  == 'init':
        print('Welcome to the world of dragonbound 2d xyz')
        mundo_vacio = dragonbound.draw_world_empty(mundo)
        mapa = dragonbound.draw_world(mundo_vacio)
        dragonbound.print_world(mapa)

        accion = input('Input Exit (E) or Launch (L): ')

        if accion == 'L':
            print('Turno jugador A')
            player = 'A'
            angulo = int(input('Ingresa el angulo de tiro [1-70]: '))
            angulo_rad = radians(angulo)

            mundo_vacio = dragonbound.draw_world_empty(mundo)
            mapa = dragonbound.draw_world(mundo_vacio)

            velocidad_inicial = dragonbound.calculate_velocity(angulo_rad)
            dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa, player)
            break

        else:
            print('Turno jugador B')
            player = 'B'
            angulo = int(input('Ingresa el angulo de tiro: '))
            angulo_rad = radians(angulo)

            mundo_vacio = dragonbound.draw_world_empty(mundo)
            mapa = dragonbound.draw_world(mundo_vacio)

            velocidad_inicial = dragonbound.calculate_velocity(angulo_rad)
            dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa, player)
            break

    else:
        print('Ingrese la palabra correcta para cargar el mapa.')



