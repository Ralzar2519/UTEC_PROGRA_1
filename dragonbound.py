#IMPORTACION DE MODULOS y METODOS
from colorama import Back, init
from math import tan, cos, sqrt, sin
import os
from time import sleep


init(autoreset =  True)

def draw_world_empty(mundo = [] ):
    """
    Crea una matriz vacia dpnde se coloca Back.BLUE entre cada interseccion fila-columna

    Args:
        mundo (list): Lista vacia

    Returns:
        Matriz 20 x 30 contenida en la variable mundo
    """

    for f in range(20):
        unafila = [Back.BLUE]* 30
        mundo.append(unafila)

    return mundo

def draw_world(mundo : list[list]) -> list[list]:
    """
    Invoca a las funciones draw_sun, draw_players, draw_cars, draw_stones, draw_concrete y draw bricks para que
    modifiquen la variable mundo. De manera que cuando se use la funcion print_world() se pueda mostrar el mundo con
    todos sus elementos

    Args:
        mundo (list): Lista retornada previamente por la funcion draw_world_empty()

    Returns:
        mundo (list): Mapa del mundo con todos los elementos incorporados
    """
    draw_sun(mundo)
    draw_players(mundo)
    draw_cars(mundo)
    draw_stones(mundo)
    draw_concretes(mundo)
    draw_bricks(mundo)

    return mundo

def draw_sun(mundo : list[list]) -> list[list]:
    """
    Cambia los valores de la matriz mundo con los color YELLOW en las posiciones donde debe estar ubicado el sol

    Args:
        mundo (list): mundo retornado con por la funcion draw_world_empty()

    Returns:
        La matriz mundo con los colores del sol incorporados en su posicion.
    """
    for f in range(4):
        for c in range(26, 30):
            if f == 0 and c == 2:
                continue
            if f == 2 and c == 26:
                continue
            if f == 3 and c == 27:
                continue
            if f == 3 and c == 29 :
                continue
            mundo[f][c] = Back.YELLOW

def draw_players(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con los color MAGENTA en las posiciones donde debe estar ubicado los jugadores

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores de los jugadores incorporados en su posicion.
    """
    mundo[10][7] = Back.MAGENTA
    mundo[10][22] = Back.MAGENTA

def draw_cars(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con los colores respectivos de los carritos del jugador A y B en las posiciones
        donde debe estar ubicado.

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores de los carrtitos de A y B incorporados en su posicion.
    """
    for col in range(6,9):
         mundo[11][col] = Back.CYAN #carrito uno
    for col in range(21,24):
         mundo[11][col] = Back.GREEN #carrito dos

def draw_stones(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con el color de la piedra (WHITE) en las posiciones
        donde debe estar ubicado.

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores de las piedras  incorporados en su posicion.
    """
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

def draw_concretes(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con el color del comcreto (BLACK) en las posiciones
        donde debe estar ubicado.

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores del concreto incorporados en su posicion.
    """
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

def draw_bricks(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con el color de los ladrillos (ROJO) en las posiciones
        donde debe estar ubicado.

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores de los ladrillos  incorporados en su posicion.
    """
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

def print_world(mundo : list[list]) -> list[list]:
    """
        Cambia los valores de la matriz mundo con el color de la piedra (WHITE) en las posiciones
        donde debe estar ubicado.

        Args:
            mundo (list): mundo retornado con por la funcion draw_world_empty()

        Returns:
            La matriz mundo con los colores de las piedras  incorporados en su posicion.
        """
    for fila in range(20):
        for col in range(30):
            print(mundo[fila][col] + '   ', end='')
        print()

def calculate_velocity(angle : float , gravity = 9.8 , distance = 15) -> float:
    """
    Calcula la velocidad inicial que debe ser lanzado la bala por el jugador para que realice un tiro perfecto.

    Args:
    angle: Angulo introducido por el jugador y convertido en radianes
    Gravity: Argumento por defecto con valor igual a 9.8
    Distance: Argumento por defecto con valor igual a 15 que representa la distancia horizontal entre los jugadores

    Returns:
    Vi_perfecta: Velocidad inicial con la que debe ser lanzada la bala para un tiro perfecto
    """
    #El sqrt representa que se esta aplicando raiz cuadrada
    vi_perfecta = sqrt( (gravity * distance)/(2*cos(angle)*sin(angle)) )
    return vi_perfecta

def limpiar_pantalla():
    """
    Limpia la consola mediante un comando del sistema operativo
    """
    os.system('cls')

def draw_missile_launch(v_inicial, angle, mapa, player):
    """
    Dibuja la trayectoria de la bala lanzada por un jagador, pintando el espacio que ocupa la bala segun el color del
    jugador sea A o B.

    Args:
    v_inicial : Velocidad inicial en la que debe lanzar la bala para que elimine al otro jugador
    angle : Angulo introducido por el jugador y convertido en radianes
    mapa : Matriz que contiene los colores del mundo
    player: Representa si el jugador es A o B

    Returns:
    Muestra la trayectoria de la bala dependiendo de quien es player, mediante el calculo de la posicion y cuando la bala
    esta en una ppsicion x_inicial + x, siendo x un valor que va desde  1 a 15. Cada posicion de la bala se imprime 15 veces
    y entre cada impresion hay un salto de linea. El numero 15 indica la distancia horizantal entre los jugadores. Cuando x es 15,
    se llama a la funcion finish_game() debido a que la bala llego a la posicion que se ublica el jugador rival.
    """

    if player == 'A':
        for x in range(1, 16):
            y = x * tan(angle) - (9.8 * x ** 2) / (2 * v_inicial ** 2 * cos(angle) ** 2)

            #Posiciones dentro del mundo:
            #pos_x indica el numero de columna que ocupa la bala en la matriz mundo
            #pos_y indica el numero de fila que ocupa la bala en la matriz mundo
            pos_x = 7 + x
            pos_y = 10 - round(y)

            color_guardado = mapa[pos_y][pos_x]
            mapa[pos_y][pos_x] = Back.CYAN

            limpiar_pantalla()
            print_world(mapa)
            sleep(0.5)

            mapa[pos_y][pos_x] = color_guardado

    else:
        for x in range(1,16):
            y = x * tan(angle) - (9.8 * x ** 2) / (2 * v_inicial ** 2 * cos(angle) ** 2)

            pos_x = 22 - x
            pos_y = 10 - round(y)

            #Guardado del valor original del espacio que ocupara la bala
            color_guardado = mapa[pos_y][pos_x ]
            mapa[pos_y][pos_x ] = Back.GREEN

            limpiar_pantalla()
            print_world(mapa)
            sleep(0.5)

            mapa[10 - round(y)][pos_x ] = color_guardado


def finish_game(player):
    """
    Imprime una frase que indica que durante el turno de player, el gano.
    Args:
        player: Representa si el jugador es A o B.

    Retorns:
        str: Frase donde indica que player gano a su rival
    """
    print("El jugador "+ player + " es el ganador")




