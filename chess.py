#!/bin/python
import pygame
import os

os.system ("clear")

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

x = 100
y = 100

white = (255, 255, 255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
object = (0, 0)



class Pice:
    def __init__(self, position, side):
        self.position = position
        self.__side = None
        #if side = true | side = white

   
    def movment(self, movment):
        if self.__side == True:
            pass #+1 cord
        elif self.__side == False:
            pass #-1 cord


class Pawn(Pice):
    def set_side (self, side):
        self.__side = None





       
screen.fill (white)

screen.blit(x,y)

pygame.display.flip()

clock.tick(60)


#print("\033[34m █\033[0m")