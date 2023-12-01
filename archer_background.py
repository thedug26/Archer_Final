import pygame
from archer_game_constants import *
#import random


def draw_background(land):
    #input my sprites into variables

    grass=pygame.image.load("../Archer_Final/assets/Archer_Sprites/tile_0002.png").convert()
    dirt=pygame.image.load("../Archer_Final/assets/Archer_Sprites/tile_0004.png").convert()
    sky=pygame.image.load("../Archer_Final/assets/Archer_Sprites/tile_0001.png").convert()
    custom_font = pygame.font.Font("../Archer_Final/assets/fonts/Kenney Future.ttf", 48)

    #dirt.set_colorkey((255,0,0))
    #sky.set_colorkey((255,255,255))

    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
            land.blit(sky,(x,y))

    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        land.blit(dirt,(x,SCREEN_HEIGHT-TILE_SIZE))

    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        land.blit(grass,(x,SCREEN_HEIGHT-TILE_SIZE*2))

    #for _ in range(5):
    #    x=random.randint(0,SCREEN_WIDTH)
    #    land.blit(seagrass,(x,SCREEN_HEIGHT-TILE_SIZE*2))

    text=custom_font.render("Archer",True,(255,0,0))
    land.blit(text, (SCREEN_WIDTH/2-text.get_width()/2, text.get_height()/100))
