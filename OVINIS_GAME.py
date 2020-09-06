import pygame

pygame.init()
x: int = 25
y: int = 225
a: int = 1000
b: int = 275

background = pygame.image.load('background')
ovini1 = pygame.image.load('ovini1')
ovini2 = pygame.image.load('ovini2')

vel = 25

wind = pygame.display.set_mode((1140,640))
pygame.display.set_caption("OVINIS WAR")

c = True
while c:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c = False

    commands = pygame.key.get_pressed()

    wind.fill((0, 0, 0))
    wind.blit(background, (0, 0))

    if commands[pygame.K_w]:
        y -= vel
    if commands[pygame.K_s]:
        y += vel

    if (y < 0):
        y = 700
    elif (y > 700):
        y = 0
    wind.blit(ovini1, (x,y))

    if commands[pygame.K_UP]:
        b -= vel
    if commands[pygame.K_DOWN]:
        b += vel

    if (b < 0):
        b = 700
    elif (b > 700):
        b = 0

    wind.blit(ovini2, (a,b))
    pygame.display.update()
