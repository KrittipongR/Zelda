import math

WIDTH = 1152 #1280
HEIGHT = 648 #720

TILE_SIZE = 48

PLAYER_WALK_SPEED = 180

POT_SPEED = 360

NUMBER_OF_MONSTER=10 #For testing rn
NUMBER_OF_POTS=5

MAP_WIDTH = WIDTH // TILE_SIZE - 2
MAP_HEIGHT = int(math.floor(HEIGHT/TILE_SIZE)) - 2

MAP_RENDER_OFFSET_X = (WIDTH - (MAP_WIDTH * TILE_SIZE)) / 2
MAP_RENDER_OFFSET_Y = (HEIGHT - (MAP_HEIGHT *TILE_SIZE)) / 2

TILE_TOP_LEFT_CORNER = 4
TILE_TOP_RIGHT_CORNER = 5
TILE_BOTTOM_LEFT_CORNER = 23
TILE_BOTTOM_RIGHT_CORNER = 24

TILE_FLOORS = [
    7, 8, 9, 10, 11, 12, 13,
    26, 27, 28, 29, 30, 31, 32,
    45, 46, 47, 48, 49, 50, 51,
    64, 65, 66, 67, 68, 69, 70,
    88, 89, 107, 108
]

TILE_EMPTY = 19

TILE_TOP_WALLS = [58, 59, 60]
TILE_BOTTOM_WALLS = [79, 80, 81]
TILE_LEFT_WALLS = [77, 96, 115]
TILE_RIGHT_WALLS = [78, 97, 116]