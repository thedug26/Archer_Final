import pygame


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.image = pygame.image.load('../Archer_Final/assets/Archer_Sprites/soldier_stand.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen
        self.time = pygame.time.get_ticks()
        self.scream = pygame.mixer.Sound("../Archer_Final/assets/Archer_Sounds/scream.wav")
        self.scream_length = self.scream.get_length() * 1000

    def update(self, arrow_group):
        collision = pygame.sprite.spritecollideany(self, arrow_group)
        print(arrow_group)
        if collision:
            self.image = pygame.image.load("../Archer_Final/assets/Archer_Sprites/soldier_hurt.png")
            pygame.mixer.Sound.play(self.scream)
            self.time = pygame.time.get_ticks()

        elif pygame.time.get_ticks() - self.time >= self.scream_length:
            self.image = pygame.image.load('../Archer_Final/assets/Archer_Sprites/soldier_stand.png')

    def draw(self):
        self.screen.blit(self.image, self.rect)
