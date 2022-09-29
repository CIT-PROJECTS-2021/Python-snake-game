import pygame
from pygame.locals import *
import time
import random

SIZE = 50
BACKGROUND_COLOR = (120, 120, 5)

#Creating the apple Class
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 130
        self.y = 130
#Draw Method
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*SIZE
        self.y = random.randint(1,20)*SIZE
