import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadimage = pygame.image.load('flappybird.png')
        self.w = self.loadimage.get_width() // 4
        self.h = self.loadimage.get_height() // 4
        self.loadimage = pygame.transform.scale(self.loadimage, (self.w, self.h))
        self.rect = self.loadimage.get_rect()
        self.rect.x = 100
        self.rect.y = 540
        self.speed = 1
        self.gravity = 1
        self.up = 15
        self.apex = 0
        self.image = pygame.transform.rotate(self.loadimage, self.apex)



    def update(self):
        if self.speed <= 100:
            self.rect.y += self.speed
            self.speed += self.gravity
        self.rotate()

    def jump(self):
        self.speed -= self.up

    def rotate(self):

        #if self.speed > 0:
            #self.apex -= 1

        #elif self.speed < 0:
            #self.apex += 1
        if self.speed < 0:
            self.apex =  -self.speed * 2
            if self.apex > 46:
                self.apex = 45
        elif self.speed > 0 :
            self.apex = -self.speed * 2
            if self.apex < -46:
                self.apex = -45
        self.image = pygame.transform.rotate(self.loadimage, self.apex)


