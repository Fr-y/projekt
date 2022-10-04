import itertools
import pygame
from pygame.locals import *
from math import floor, dist
GRID = [(x*50, y*50) for y, x in itertools.product(range(20), range(20))]
USED_GRID = []

def calc_grid(pos):
	npos = (floor(pos[0] / 50) * 50, floor(pos[1] / 50)  * 50)
	return min(GRID, key=lambda x: dist(x, npos))

class Tower:
	def __init__(self, tower, pos, lvl):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load('images/tower.jpg')
		self.tower = tower #tipus  
		self.pos = pos  #(x,y)
		self.level = lvl
	
	def draw(self, WIN, pos):
		grid_clicked = calc_grid(pos)	
		if grid_clicked not in USED_GRID:
			WIN.blit(self.image, calc_grid(pos))
			USED_GRID.append(grid_clicked)
		else:
			print("You already placed a tower there")


