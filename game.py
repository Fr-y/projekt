from asyncio import constants
from random import randint
import pygame as pg
import math

from Enemy import *
from Tower import *
from Sprites import *


# pygame init
pg.init()
WIDTH, HEIGHT = 1000, 1000
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Game")
# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)
RED = (255, 0, 0)
DARK_GREY = (80, 80, 80)
FONT = pg.font.SysFont("ariel", 40)

BackGround = Background('images/background.jpg', [0,0])


# funcs

#grid rajzolása
def drawGrid():  # sourcery skip: use-itertools-product
    blockSize = 50 #Set the size of the grid block
    for x in range(0, WIDTH, blockSize):
        for y in range(0, HEIGHT, blockSize):
            rect = pg.Rect(x, y, blockSize, blockSize)
            pg.draw.rect(WIN, WHITE, rect, 1)

def placeTower(pos):
    tower = Tower("asd", (pos), 3)
    tower.draw(WIN, pos)


def main():
    run = True
    clock = pg.time.Clock()
    WIN.fill(BLACK)
    WIN.blit(BackGround.image, BackGround.rect)
    drawGrid()

    while run:
        # clock
        clock.tick(30)

        # kilepes
        for event in pg.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                placeTower(pos)
            if event.type == pg.QUIT:
                run = False

        # hivasok minden framenél(30/sec)
        pg.display.update()

    pg.quit()

main()