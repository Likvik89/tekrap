import pygame
from pygame.math import *


buttons = []
mouse_pos = Vector2()

teknologipoints = 0
elevetos = 0

screen = pygame.display.set_mode((1500 , 1000), 0)



class button():
    def __init__(self, pos_x, pos_y, width, height, function, sprite):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.click = function
        self.sprite = sprite
        buttons.append(self)