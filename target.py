import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = pygame.image.load('../Archer_Final/assets/Archer_Sprites/soldier_stand.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)
