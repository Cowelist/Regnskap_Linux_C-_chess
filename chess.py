#!/bin/python
import pygame
import os

os.system ("clear")

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

screen.fill ((225, 255, 255))

clock.tick(60)


#print("\033[34m █\033[0m")