from colorama import Back, init
from math import pi, sin, cos,sqrt, radians

init(autoreset =  True)

def draw_world_empty(mundo = [] ):

    #Completa el mundo con pixeles de color azul para facilitar el dibujo,
    #despues en draw_world nos enfocamos en dibujar el ladrillo, concreto, los carritos y los jugadores
    for f in range(20):
        unafila = [Back.BLUE]* 30
        mundo.append(unafila)

    return mundo

def draw_world(mundo):
    draw_sun(mundo)
    draw_players(mundo)
    draw_cars(mundo)
    draw_stones(mundo)
    draw_concretes(mundo)
    draw_bricks(mundo)

    return mundo

def draw_sun(mundo):
    for f in range(4):
        for c in range(26, 30):
            if(f == 0 and c == 26):
                continue
            if(f == 2 and c == 26):
                continue
            if(f == 3 and c == 27):
                continue
            if(f == 3 and c == 29):
                continue
            mundo[f][c] = Back.YELLOW

def draw_players(mundo):
     mundo[10][7] = Back.MAGENTA
     mundo[10][22] = Back.MAGENTA

def draw_cars(mundo):
     for col in range(6,9):
         mundo[11][col] = Back.CYAN #carrito uno
     for col in range(21,24):
         mundo[11][col] = Back.GREEN #carrito dos

def draw_stones(mundo):
    mundo[11][14] = mundo[11][15] = Back.WHITE
    for fila in range(12,17):
        if fila == 12:
            for c in [0,1,6,7,8,13,14,15,16,21,22,23,28,29]:
                mundo[fila][c] = Back.WHITE
        elif fila == 13:
            lista = list(range(10)) + list(range(20,30))
            for c in lista:
                mundo[fila][c] = Back.WHITE
        elif fila == 14:
            lista = list(range(1,6)) + list(range(9, 11)) + list(range(19,21)) + list(range(24,29))
            for c in lista:
                mundo[fila][c] = Back.WHITE
        elif fila == 15:
            lista = list(range(2,5)) + list(range(10, 20)) + list(range(25,28))
            for c in lista:
                mundo[fila][c] = Back.WHITE
        elif fila == 16:
            lista = list(range(11,19))
            for c in lista:
                mundo[fila][c] = Back.WHITE

def draw_concretes(mundo):
    for fila in range(13,16):
        if fila == 13:
            for c in list(range(10,20)):
                mundo[fila][c] = Back.BLACK
        elif fila == 14:
            lista = list(range(6,9)) + list(range(11, 19)) + list(range(21, 24))
            for c in lista:
                mundo[fila][c] = Back.BLACK
        elif fila == 15:
            lista = list(range(5, 10)) + list(range(20, 25))
            for c in lista:
                mundo[fila][c] = Back.BLACK

def draw_bricks(mundo):
    for fila in range(16,20):
        if fila == 16:
            lista = list(range(7, 11)) + list(range(19, 23))
            for c in lista:
                mundo[fila][c] = Back.RED
        elif fila == 17:
            for c in list(range(7,23)):
                mundo[fila][c] = Back.RED
        elif fila == 18:
            for c in list(range(8,22)):
                mundo[fila][c] = Back.RED
        elif fila == 19:
            for c in list(range(8,22)):
                mundo[fila][c] = Back.RED

        # Añade la cantidad de pixeles pintadas de
def print_world(mundo):
  for fila in range(20):
        for col in range(30):
            print(mundo[fila][col] + '   ', end='')
        print()

def calculate_velocity(angle, gravity = 9.8 , distance = 15):

    angle_rad = radians(angle)

    vi_perfecta = sqrt( (gravity * distance)/(2*cos(angle_rad)*sin(angle_rad)) )
    return vi_perfecta



def draw_missile_launch(v_inicial, angle, mapa, x0=8, y0=11, steps=15, g=9.8):
    v_x = v_inicial * cos(angle)
    v_y = v_inicial * sin(angle)
    tiempo_vuelo = (v_y / 9.8) * 2
    y_max = 11 + (v_inicial * pow(sin(angle), 2)) // (2 * 9.8)
    for m in range(15): time_act = tiempo_vuelo / (15 - m)
    d_x = 8 + v_x * time_act
    d_x = round(d_x)
    d_y = 11 - abs(v_y * time_act - 0.5 * 9.8 * pow(time_act, 2))
    d_y = round(d_y)
    if d_y <= y_max: mapa[d_y][d_x] = Back.CYAN
    print_world(mapa)
    print() else: d_y =


        # pintar temporalmente la bala en cian y renderizar
        saved = mapa[iy][ix]
        mapa[iy][ix] = Back.CYAN
        print_world(mapa)
        print()
        # restaurar el valor anterior (para que el mapa base no sea sobrescrito)
        mapa[iy][ix] = saved




