import pygame
from projectiles import Arrow
from archer_game_constants import *


class Adventurer(pygame.sprite.Sprite):
    def __init__(self, x, y, arrows, screen):
        super().__init__()
        self.image = pygame.image.load('../Archer_Final/assets/Archer_Sprites/adventurer_stand.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.theta = 45
        self.arrow = pygame.transform.rotate(pygame.image.load('../Archer_Final/assets/Archer_Sprites/arrow.png'),-45)
        self.arrows = arrows
        self.last_fire = 0
        self.screen = screen
        self.score=0

    def update(self):

        # check for key presses
        self.check_keys()

    def check_keys(self):
        # check for key presses
        keys = pygame.key.get_pressed()
        # if the left arrow key is pressed
        if keys[pygame.K_LEFT]:
            # rotate the arrow left
            self.theta += 1+1
        # if the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            # rotate the arrow right
            self.theta -= 1+1
        # if space bar is pressed (limit fire interval to 0.5 seconds)
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_fire > 500:
            # set the last fire time
            self.last_fire = pygame.time.get_ticks()

            # create an arrow
            arrow = Arrow(self.rect.centerx, self.rect.centery, self.theta, self.screen)
            # add the arrow to the arrows group
            self.arrows.add(arrow)

            #use arrow instance to set score
            #self.score += arrow.score

    def draw(self):
        self.screen.blit(self.image, self.rect)
        # Rotate the arrow and scale it
        rot_arrow = pygame.transform.rotozoom(
            self.arrow, self.theta, 1)
        # Get the rectangle of the rotated arrow
        rot_arrow_rect = rot_arrow.get_rect()
        # Set the center of the rotated arrow to the center of the tank
        rot_arrow_rect.center = self.rect.center
        # Draw the rotated arrow
        self.screen.blit(rot_arrow, rot_arrow_rect)