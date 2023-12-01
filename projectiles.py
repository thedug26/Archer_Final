import pygame
from math import sin, cos, atan2, pi

from archer_game_constants import *


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, theta, screen):
        super().__init__()
        self.image = pygame.image.load('../Archer_Final/assets/Archer_Sprites/arrow.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.theta = theta  # theta in deg
        self.zoom = 1
        self.speed = 8+1.75
        self.screen = screen

        # collision sound
        self.scream = pygame.mixer.Sound("../Archer_Final/assets/Archer_Sounds/scream.wav")

        # keep track of score
        self.score = 0
        # init values for trajectory
        self.x_vel = self.speed * cos(self.theta * pi / 180)
        self.y_vel = self.speed * sin(self.theta * pi / 180)

        self.x_acc = 0
        self.y_acc = 0

        self.drag = 5e-3
        self.gravity = 5e-2

    def update(self):
        # check if this bullet should stop (land on dirt)
        if self.y > self.screen.get_height() - TILE_SIZE * 2:
            self.y_vel = 0
            self.x_vel = 0
        else:
            self.x += self.x_vel
            self.y -= self.y_vel

        # handle the velocity
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc

        # handle the acceleration
        self.x_acc = -self.drag * self.x_vel
        self.y_acc = -self.drag * self.y_vel - self.gravity

        # Update the bullet's rect
        self.rect.center = (self.x, self.y)

        # update the theta IF positive y velocity
        if not self.y_vel == 0:
            rads = atan2(self.y_vel, self.x_vel)
            self.theta = rads * 180 / pi

    def draw(self, target, screen):
        rot_arrow = pygame.transform.rotozoom(self.image, self.theta, 1)
        # get rectangle of rotated bullet
        rot_arrow_rect = rot_arrow.get_rect()
        rot_arrow_rect.center = self.rect.center

        # get rectangle of target
        target_rect = target.rect
        # check if the arrow rectangle collides with target rectangle
        collide = rot_arrow_rect.colliderect(target_rect)
        if collide:
            self.score += 1
            # self.kill() # remove arrow if collision
            pygame.mixer.Sound.play(self.scream)

        screen.blit(rot_arrow, rot_arrow_rect)
