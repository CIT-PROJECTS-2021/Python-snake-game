import pygame
from pygame.locals import *
import time
import random
#this method is defined in the snake class
#to increase the length of the snake by 1
#the append function means you are adding something at the end of the list
# for this case we are adding a block which adds to the length of our snake.
def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

#the increase length method is called in the play function which is defined in the
#game class.
#on collision,(when the snake eats the apple) the apple moves to a diferent location
#and the snake's length inreases
def play(self):
        self.snake.walk()
        self.apple.draw()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()
