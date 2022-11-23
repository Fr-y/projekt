import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LEAF_GREEN = (33, 162, 31)
BLUE = (0, 0, 255)
DARK_BLUE = (100, 100, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 255, 100)
BROWN = (162, 93, 65)

WIDTH = 1280
HEIGHT = 720
FPS = 30
TITLE = "Tower Defense"
SELL_BTN_COLOR = (148,0,0)
INACTIVE_BTN_COLOR = DARKGREY
UPGRADE_BTN_COLOR = (9,111,0)
MENU_BTNS_COLOR = BROWN
MENU_BTNS_TXT_COLOR = WHITE
INFO_BOX_COLOR = (0,0,0,30)

TOWER_TYPES = {
  'green_tank': {
    'damage': 1,
    'price': 50,
    'range': 170,
    'rate': 2000,
  },
    'green_tank_upgraded': {
    'damage': 2,
    'price': 35,
    'range': 230,
    'rate': 1500,
  },
}

ENEMY_TYPES = [
  'green_bike', 'blue_bike', 'yellow_bike', 'red_bike', 'black_bike', 
  'green_car', 'blue_car', 'yellow_car', 'red_car', 'black_car']

ENEMY_PROPS = {
  'green_bike': {
    'health': 1,
    'value': 2,
    'speed': 3,
  },
}

LEVELS = {
  '1': {
    'weights': [100,0,0,0,0,0,0,0,0,0],
    'rate': 800,
    'n': 15
  },
  '2': {
    'weights': [50,50,0,0,0,0,0,0,0,0],
    'rate': 800,
    'n': 20
  },
  '3': {
    'weights': [40,30,30,0,0,0,0,0,0,0],
    'rate': 800,
    'n': 25
  },
  '4': {
    'weights': [30,20,20,30,0,0,0,0,0,0],
    'rate': 500,
    'n': 30
  },
  '5': {
    'weights': [20,20,20,20,20,0,0,0,0,0],
    'rate': 500,
    'n': 35
  },
  '6': {
    'weights': [10,10,20,20,20,20,0,0,0,0],
    'rate': 500,
    'n': 40
  },
  '7': {
    'weights': [10,10,10,10,20,20,20,0,0,0],
    'rate': 500,
    'n': 40
  },
  '8': {
    'weights': [10,10,10,10,10,10,40,0,0,0],
    'rate': 500,
    'n': 40
  },
  '9': {
    'weights': [0,0,10,10,10,10,30,30,0,0],
    'rate': 500,
    'n': 40
  },
  '10': {
    'weights': [0,0,10,10,10,10,10,50,0,0],
    'rate': 500,
    'n': 40
  },
  '11': {
    'weights': [0,0,0,10,10,10,10,40,20,0],
    'rate': 500,
    'n': 40
  },
  '12': {
    'weights': [0,0,0,10,10,10,10,20,40,0],
    'rate': 500,
    'n': 40
  },
  '13': {
    'weights': [0,0,0,0,10,10,10,10,40,20],
    'rate': 500,
    'n': 40
  },
  '14': {
    'weights': [0,0,0,0,10,10,10,10,20,40],
    'rate': 500,
    'n': 40
  },
  '15': {
    'weights': [0,0,0,0,0,10,10,10,20,50],
    'rate': 500,
    'n': 40
  },
  '16': {
    'weights': [0,0,0,0,30,0,0,0,10,60],
    'rate': 500,
    'n': 40
  },
}