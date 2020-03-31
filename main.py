import pygame
import random
import classBird
import classBlock
import classAnimation

pygame.init()
font = pygame.font.SysFont('DOCKER THREE', 40)

# Display
back = pygame.image.load('flappyfon.jpg')
gamedisplay = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Clock
clock = pygame.time.Clock()
FPS = 120
pygame.time.set_timer(pygame.USEREVENT, 8000)

bird = classBird.Bird()

anime = classAnimation.Animation()

flappy = pygame.sprite.Group()
flappy.add(bird)



def startgame():
    global rad
    text = font.render('Click to start (Najmi)', 1, (153, 0, 0))
    textrect = text.get_rect()
    textrect.center = [960, 540]

    start = False
    while not start:
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                start = True

        if rad > 1:
            rad -= 20
        gamedisplay.blit(back, (0, 0))
        pygame.draw.circle(gamedisplay, (0, 0, 0), (960, 540), rad)
        gamedisplay.blit(text, textrect)
        pygame.display.update()


def gameover():
    global rad
    if rad < 2000:
        rad += 20

    pygame.draw.circle(gamedisplay, (0, 0, 0), (960, 540), rad)

    text = font.render('Game Over (Vi Zdohli)', 1, (153, 0, 0))
    textrect = text.get_rect()
    textrect.center = [960, 540]

    gamedisplay.blit(text, textrect)

    # pygame.display.update()


def lvl1():
    flappy.update()
    flappy.draw(gamedisplay)


gameovertimer = 0

game = True
lvl = True
rad = 2000
startgame()
rad = 1


while game == True:
    clock.tick(FPS)
    gamedisplay.blit(back, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()
        if e.type == pygame.USEREVENT:
            pos1 = random.randint(100, 600)
            tube = classBlock.Block()
            tube.mirror()
            tube.rect.bottom = pos1
            flappy.add(tube)

            pos2 = pos1 + 300
            tube2 = classBlock.Block()
            tube2.rect.top = pos2
            flappy.add(tube2)

    for i in flappy.sprites()[1::]:
        if i.rect.right <= 0:
            i.kill()

        if i.rect.colliderect(bird.rect):
            flappy.draw(gamedisplay)
            anime.click(bird.rect)
            gamedisplay.blit(anime.image, anime.rect)
            lvl = False


    if lvl == True:
        lvl1()
    else:

        gameovertimer += 1
        if gameovertimer > 3000:
            gameover()

    if bird.rect.y < -600 or bird.rect.y > 1680:

        lvl = False

    pygame.display.update()
pygame.quit()
