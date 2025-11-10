"""
# 🐉 Dragonbound 2D XYZ

Proyecto desarrollado para el curso **Programación I (CS1111 - UTEC)**.  
Simula el clásico juego **Dragonbound** en consola, utilizando **Python** y la librería **Colorama** para renderizar un mapa con colores.  
El usuario puede inicializar el mundo, visualizar los jugadores y lanzar proyectiles siguiendo una trayectoria parabólica.

---

## 📁 Estructura del Proyecto

```
📦 dragonbound-2d-xyz
│
├── main.py               # Programa principal: flujo del juego
├── dragonbound.py        # Módulo con funciones de dibujo y física
├── README.md             # Documentación del proyecto
└── requirements.txt      # Librerías necesarias
```

---

## ⚙️ Ejecución

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:
   ```bash
   python main.py
   ```
3. Escribe `init` para cargar el mapa.
4. Elige una acción:
   ```
   Input Exit (E) or Launch (L):
   ```
5. Si eliges **L**, ingresa el ángulo de disparo.  
   Verás la animación del lanzamiento con la bala en color **cian (CYAN)**.

---

## 🧩 Arquitectura y Descripción de Funciones

### 🔹 `main.py`
Controla la lógica general del juego y la interacción con el usuario.

#### Funciones:
- **`init_game(entrada)`**
  - Verifica si el usuario escribe `"init"`.
  - Llama a `draw_world_empty()` y `draw_world()` del módulo `dragonbound`.
  - Imprime el mapa en consola con `print_world()`.

- **Flujo principal**
  - Si la entrada es válida, solicita una acción:
    - `L` → Lanza la bala.
    - `E` → Finaliza el juego.
  - Calcula el ángulo, velocidad y llama a `draw_missile_launch()`.

---

### 🔹 `dragonbound.py`
Módulo que define las funciones gráficas y físicas del juego.

#### 🖼️ Dibujo del mundo

- **`draw_world_empty(mundo=[])`**  
  Crea una matriz de **20 filas × 30 columnas**, llenas con el color azul (`Back.BLUE`), que representa el cielo.

- **`draw_world(mundo)`**  
  Agrega al mapa todos los elementos del escenario (sol, carritos, jugadores, estructuras).  
  Devuelve la matriz completa lista para imprimir.

- **`print_world(mundo)`**  
  Recorre la matriz e imprime los colores en consola.

#### ☀️ Elementos del mapa

| Función | Descripción | Color |
|----------|--------------|-------|
| `draw_sun(mundo)` | Dibuja el sol en la esquina superior derecha | `Back.YELLOW` |
| `draw_players(mundo)` | Coloca a los jugadores A y B | `Back.MAGENTA` |
| `draw_cars(mundo)` | Dibuja los carritos debajo de los jugadores | `Back.CYAN`, `Back.GREEN` |
| `draw_stones(mundo)` | Crea las plataformas rocosas del terreno | `Back.WHITE` |
| `draw_concretes(mundo)` | Añade zonas de concreto intermedias | `Back.BLACK` |
| `draw_bricks(mundo)` | Construye el suelo de ladrillos | `Back.RED` |

---

### 🎯 Simulación de disparo

- **`draw_missile_launch(v_inicial, angle, mapa, player)`**  
  Simula el movimiento parabólico del proyectil, usando la ecuación:

  \[
  y = x \tan(\theta) - \frac{g x^2}{2 v_0^2 \cos^2(\theta)}
  \]

  - La bala del jugador **A** se pinta en **cian** (`Back.CYAN`).
  - La bala del jugador **B** se pinta en **verde** (`Back.GREEN`).
  - Se imprime el mapa en cada iteración para simular la animación.
  - Llama a `finish_game(player)` cuando el disparo termina.

- **`finish_game(player)`**  
  Imprime el mensaje `"El jugador X es el ganador"`.

---

### ⚡ Física del juego

- **`calculate_velocity(angle, gravity=9.8, distance=15)`**
  - Calcula la velocidad inicial ideal para alcanzar una distancia de 15 m.
  - Ecuación:
    \[
    v_0 = \sqrt{\frac{g \cdot d}{2 \cos(\theta) \sin(\theta)}}
    \]
  - Retorna `vi_perfecta` como número decimal (float).

---

## 🧮 Fórmulas físicas aplicadas

| Concepto | Fórmula |
|-----------|----------|
| Tiempo de vuelo | \( t = \frac{2v_0\sin(\theta)}{g} \) |
| Posición horizontal | \( x = v_0\cos(\theta)t \) |
| Posición vertical | \( y = v_0\sin(\theta)t - \frac{1}{2}gt^2 \) |
| Trayectoria | \( y = x\tan(\theta) - \frac{gx^2}{2v_0^2\cos^2(\theta)} \) |

---

## 📚 Librerías utilizadas

| Librería | Descripción | Uso |
|-----------|-------------|-----|
| `colorama` | Permite usar colores en consola (`Back`, `Fore`) | Renderizado visual del mapa |
| `math` | Funciones matemáticas: `sin`, `cos`, `tan`, `sqrt`, `radians` | Cálculos físicos y trigonométricos |

---

## 🌍 Mapa del juego

- **Dimensiones:** 20 filas × 30 columnas  
- **Cada celda = 1 m²**  
- **Colores usados:**
  - Azul → cielo  
  - Blanco → piedra  
  - Negro → concreto  
  - Rojo → ladrillo  
  - Amarillo → sol  
  - Cian / Verde → carritos  
  - Magenta → jugadores

---

## 🧠 Autores

**Curso:** CS1111 - Programación I  
**Profesor:** Wilder Nina Choquehuayta  
**Universidad:** Universidad de Ingeniería y Tecnología (UTEC)  
**Integrantes:** *(agrega tus nombres y códigos)*

---

## 🚀 Posibles mejoras

- Detección de colisión entre proyectil y estructuras.  
- Implementar viento o variación de gravedad.  
- Sistema de rondas con puntuación.  
- Efectos visuales y temporización entre cuadros.  
"""
