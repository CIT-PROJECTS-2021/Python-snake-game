import pygame
from pygame.locals import *
import time
#size of the block of the snake
SIZE = 40

def walk(self):
        #update the position of the body of the snake
        for i in range(self.length-1, 0, -1):
            self.x[i]==self.x[i-1]
            self.y[i]==self.y[i-1]
         #update the direction of the head of the snake   
        if self.direction =="right":
            self.x[0] +=SIZE
        if self.direction =="left":
            self.x[0] -=SIZE
        if self.direction =="up":
            self.y[0] -=SIZE
        if self.direction =="down":
            self.y[0] +=SIZE
        self.draw()
            

