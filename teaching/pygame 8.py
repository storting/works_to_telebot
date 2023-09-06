import pygame
import sys
pygame.font.init()
 
sc = pygame.display.set_mode((300, 300))
sc.fill((255, 255, 255))
rect = pygame.Rect((230, 230, 70, 70)) 
font = pygame.font.SysFont(None, 36)
text = font.render('YESSS', True, (0, 0, 0))
surf = pygame.Surface((70, 70))
surf2 = pygame.Surface((30, 30))

place = surf2.get_rect(center=(40, 40))

sc.blit(surf, rect)
sc.blit(surf2, place)
pygame.display.update()

cl = False
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    place = surf2.get_rect(center=(x, y))
    surf.fill((200, 43, 100))
    sc.blit(surf, (230, 230))
    sc.blit(surf2, place)
    if rect.contains(place):
       
       print('234')
       sc.blit(text, (20, 20))

        
    
    pygame.display.update()
    sc.fill((255, 255, 255))