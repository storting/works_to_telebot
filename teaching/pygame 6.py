import pygame
import sys
 
FPS = 60
WIN_WIDTH = 800
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
x = 0
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))

hero = pygame.Surface((200, 200))
sc.blit(hero, (x, 12))
hero.fill(ORANGE)

sword = pygame.draw.circle(hero, (0, 250, 0), (20, 40), 20)
sword2 = pygame.draw.circle(hero, (0, 250, 0), (200, 100), 20)

pygame.display.update()
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    if x < 800:
        x += 1
        sc.blit(hero, (x, 12))
        hero.fill(ORANGE)
        sword = pygame.draw.circle(hero, (0, 250, 0), (20, 40), 20)
        sword2 = pygame.draw.circle(hero, (0, 250, 0), (200, 100), 20)
        pygame.display.update()
        sc.fill((0, 0, 0))
    else:
        x = -200
        sc.fill((0, 0, 0))
        pygame.display.update()


    

    clock.tick(FPS)