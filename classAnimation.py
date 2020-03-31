import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('crosshair.png')
        self.w = self.image.get_width() // 2
        self.h = self.image.get_height() // 2
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()



    def click(self, birdrect):
        #self.rect.center = [birdrect.right - 20, birdrect.centery - 10]
        self.rect = birdrect