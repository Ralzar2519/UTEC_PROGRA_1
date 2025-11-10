import dragonbound
from math import radians

angulo = int(input('Ingresa el angulo de tiro: '))
angulo_rad = dragonbound.radians(angulo)

mundo_vacio = dragonbound.draw_world_empty()
mapa = dragonbound.draw_world(mundo_vacio)

velocidad_inicial = dragonbound.calculate_velocity(angulo_rad)

dragonbound.draw_missile_launch(velocidad_inicial, angulo_rad, mapa)
