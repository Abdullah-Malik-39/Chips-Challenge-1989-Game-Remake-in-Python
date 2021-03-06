import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)
ORANGE = (255,165,0)
DARK_BLUE = (0,0,255)
PURPLE = (128,0,128)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 700  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Chip's Challenge"
BGCOLOR = BROWN


TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tileGreen_39.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 5
AVOID_RADIUS = 50

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 50

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
TOTAL_CHIP = 16
ITEM_IMAGES = {'key_red': 'key_red.jpg','key_blue': 'key_blue.jpg','key_green': 'key_green.jpg','key_yello': 'key_yello.jpg',
               'gate_red': 'gate_red.jpg','gate_blue': 'gate_blue.jpg','gate_green': 'gate_green.jpg','gate_yello': 'gate_yello.jpg',
               'exit':'exit.jpg','exit_check':'exit_check.jpg','chip':'chip.jpg','fire':'fire.jpg',
               'water':'water.jpg','fire_im':'fire_im.jpg','water_im':'water_im.jpg','weee':'weee.jpg','thief':'thief.jpg'}
KEY = {'exit_status':False,'key_red':0,'key_blue':0,'key_green':0,'key_yello':0,'chip':0,'level':1,'fire': False, 'water': False}

