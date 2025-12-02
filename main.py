import math
import pygame 
from pygame.math import *
import config
from config import *
pygame.init()

font = pygame.font.Font(None, 86) 
text_surface = font.render("TEKNOLOGI CLICKER", True, (0,0,0))



def check_buttons():
    for button in config.buttons:
        pygame.draw.rect(config.screen, (255,255,255), button.rect)
       
       # if button.rect.collidepoint():
        #    button.click

knap = config.button(2, 2, 50, 50, "pass", False)


running = True
while running:

    config.mouse_pos = Vector2(pygame.mouse.get_pos())
    config.screen.fill((100, 100, 255))
    config.screen.blit(text_surface, (450, 100))
    
    check_buttons()
    

    config.teknologipoints += 1
    
    pygame.display.flip()
    pygame.display.update()

    
    





