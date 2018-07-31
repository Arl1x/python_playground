#!/usr/vin/env python3
# We want to import the pygame module and some constants and functions
# that already exist in the pygame module.
import pygame
from pygame.locals import *

# This is required to initialize pygame
pygame.init()

# Initialize our variables
display_width = 800
display_height = 600

# Not sure why we need the variable, but the rest of this sets the
# display to a pixel height/width as defined in the variables. We also
# set the title bar of the game window.
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('First Game Test')

# Here we define the event handler function that, for this test, drives
# the rest of the logic within the "game"


def event_handler():
    for event in pygame.event.get():
        # print(event)
        if event.type == QUIT or (
            event.type == KEYDOWN and (
                event.key == K_ESCAPE or
                event.key == K_q
            )
        ):
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()
