import math
import random
import pygame as pg
from pygame.sprite import Group
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2


#nem allat, animál
def animal(obj, angle=None, scale=None, loop=True):
    n_kepek = len(obj.kepek.keys())
    obj.kep = obj.kepek[f'frame_{(obj.frame % n_kepek)}']
    obj.frame += 1
    if obj.frame > n_kepek and not loop:
        obj.kill()

    if scale:
        obj.kep = pg.transform.scale(obj.image, scale)
    if angle:
        obj.kep = pg.transform.rotate(obj.image, -angle)


class Torony(Sprite):

    def __init__(self, jatek, _tipus, pos):
        Sprite.__init__(self, jatek.all_sprites, jatek.towers)
      self.game = jatek
      self.type = _tipus
      self.set_up_attributes()
      self.utolso_loves = 0
      self.ertek = self.price
      self.lerakott = False
      self.kep = self.game.asset_manager.kepek['towers'][self.type]
      self.rect = self.kep.get_rect() #getrect haha
      self.rect.center = (pos)
      self.barrel = Barrel(self.game, self.type, pos)