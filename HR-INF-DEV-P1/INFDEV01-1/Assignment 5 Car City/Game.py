import time
from threading import Thread

import time
import random
from random import randint
from Tile import *
from Node import *

pygame.init()

offset = 30
board_size = 10
car_texture = pygame.image.load("Content\car.png")
entry_tile = build_square_matrix(board_size, offset)
rand = randint(0,5)
x = randint(0,5)
y = randint(0,5)

NotTraverseable = 0
Park = 1

def Update(cars):
        def move(self, x, y):
            self.X = x
            self.Y = y

        def add(self, speed, cars):
            self.SPEED  = speed
            self.CARS   = cars


        def remove(self,cars, remove, park):
            self.CARS   = cars
            self.REMOVE = remove
            self.PARK   = park


    #TODO: add the logic of your cars here
    #HINT For filtering reasons we return a list (of cars?)


def Draw(self):
    class insert ():
        width = int(offset / 3)
        screen.blit(pygame.transform.scale(car_texture, (width, width)),
        (width + 0 * offset, width + 0 * offset))



#TODO: add the draw of your cars below
#
# Use the following code to draw your car.
# HINT: POSITION_X and POSITION_Y represent the position of the car to draw on the screen


def Main():
  start = time.time()
  cars = Empty
  while True:
    pygame.event.wait()
    screen.fill(green)
    entry_tile.Reset()
    entry_tile.Draw(screen)

    cars = Update(cars)
    Draw(cars)

    pygame.display.update()
    pygame.display.flip()
    time.sleep(1)
    
Main()