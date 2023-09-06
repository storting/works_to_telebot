import pygame
import sys

class pop:
    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (125, 125, 125)
    LIGHT_BLUE = (64, 128, 255)
    GREEN = (0, 200, 64)
    YELLOW = (225, 225, 0)
    PINK = (230, 50, 230)   
    def __init__(self):
        
        pygame.init()
        self.sc = pygame.display.set_mode((600, 400))
        self.clock = pygame.time.Clock()

        self.x1 = 20
        self.y1 = 20
        self.x2 = 30
        self.y2 = 30
 

        pygame.display.update()


        while True:
            
 

            self.clock.tick(self.FPS)
            self.sc.fill(self.BLACK)

            pygame.draw.rect(self.sc, self.YELLOW, 
                        (self.x1, self.y1, self.x2, self.y2))
            

            for i in pygame.event.get():
               if i.type == pygame.QUIT:
                   sys.exit()
            pygame.display.update()
            if self.x1 <= 600:
                self.x1 += 5
                
                
                
            else:
                self.x1 = 30
                self.y1 = 20
                self.x2 = 30
                self.y2 = 30
            print(self.x1)
            print(self.x2)

            
   

f = pop()