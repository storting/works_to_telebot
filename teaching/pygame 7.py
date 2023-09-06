import pygame
import sys
 
sc = pygame.display.set_mode((400, 400))
sc.fill((0, 0, 0))

cir = pygame.draw.circle(sc, (0, 0, 0), (200, 200), 200)

rect1 = pygame.Rect(0, 0, 200, 200)
rect2 = pygame.Rect(200, 0, 200, 200)
rect3 = pygame.Rect(0, 200, 200, 200)
rect4 = pygame.Rect(200, 200, 200, 200)


d1 = False
d2 = False
all = True

pygame.display.update()

while 1:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        d1 = True
        d2 = False
        all = False
    
    elif keys[pygame.K_RIGHT]:
        d2 = True
        d1 = False
        all = False

    elif keys[pygame.K_UP]:
        all = True
        d1 = False
        d2 = False

    if d1:

        cir = pygame.draw.circle(sc, (100, 100, 100), (200, 200), 200)
        pygame.display.update((rect1, rect4))
        pygame.time.delay(200)
        sc.fill((0, 0, 0))
        cir = pygame.draw.circle(sc, (255, 255, 255), (200, 200), 200)       
        pygame.display.update((rect1, rect4))
        pygame.time.delay(200)
    
    elif d2:

        cir = pygame.draw.circle(sc, (100, 100, 100), (200, 200), 200)
        pygame.display.update((rect2, rect3))
        pygame.time.delay(200)
        sc.fill((0, 0, 0))
        cir = pygame.draw.circle(sc, (255, 255, 255), (200, 200), 200)
        pygame.display.update((rect2, rect3))
        pygame.time.delay(200)

    elif all:

        cir = pygame.draw.circle(sc, (100, 100, 100), (200, 200), 200)
        pygame.display.update((rect1, rect2, rect3, rect4))
        pygame.time.delay(200)
        sc.fill((0, 0, 0))
        cir = pygame.draw.circle(sc, (255, 255, 255), (200, 200), 200)
        pygame.display.update((rect1, rect2, rect3, rect4))
        pygame.time.delay(200)
    

 

    
    pygame.display.update()
    pygame.time.delay(20)