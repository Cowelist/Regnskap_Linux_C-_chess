#!/bin/python
import pygame
import os

os.system ("clear")

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.dispaly.set_caption("Chess")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill ((225, 255, 255))




#print("\033[34m █\033[0m")