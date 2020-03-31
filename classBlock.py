import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('flappytube.png')
        self.image = self.image.subsurface(580, 0, 240, 1500)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = 2000
        self.rect.y = 500
        self.speed = 5


    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()
    def mirror(self):
        self.image = pygame.transform.flip(self.image, 0, 1)