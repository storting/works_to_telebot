import pygame
import sys
H = 500
W = 500
FPS = 60


sc = pygame.display.set_mode((H, W))
sc.fill((255, 255, 255))
 
car = pygame.image.load('18.png').convert_alpha()

car_rect = car.get_rect(center=(H/2, W/2))
sc.blit(car, car_rect)

pygame.display.update()
move_x = pygame.Rect(2, 0, 0, 0)
place = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
 


    if keys[pygame.K_LEFT]:
        
        rot_left = pygame.transform.rotate(car, 90)   
        car_rect.move_ip(-4, 0)
        sc.blit(rot_left, car_rect)
        pygame.display.update()
        
        
        
    elif keys[pygame.K_RIGHT]:
        
        rot_right = pygame.transform.rotate(car, -90)
        car_rect.move_ip(4, 0)
        sc.blit(rot_right, car_rect)

        pygame.display.update()
    elif keys[pygame.K_UP]:
        rot_up = car
        car_rect.move_ip(0, -4)
        sc.blit(rot_up, car_rect)
        pygame.display.update()
    elif keys[pygame.K_DOWN]:
        rot_down = pygame.transform.rotate(car, 180)
        car_rect.move_ip(0, 4)
        sc.blit(rot_down, car_rect)
        pygame.display.update()




 
    sc.fill((255, 255, 255))
    pygame.time.delay(FPS)