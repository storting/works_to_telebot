import pygame as pg
import sys
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
YELLOW = (225, 225, 0)
pg.init()
sc = pg.display.set_mode((700, 400))
sc.fill(WHITE)
pg.display.update()

bomb = False
H = 410
y_b = 0
x_b = 0
y = H
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1 and bomb == False:
                
                bomb = True
                
                x_b = i.pos[0]
                y_b = i.pos[1]
                

 
    sc.fill(WHITE)
    
 

    if bomb == True and y > y_b:
        pg.draw.circle(sc, YELLOW, (x_b, y), 20)
        y -= 5     
        pg.display.update()
    elif bomb == True and y <= y_b:

        sc.fill(WHITE)
        bomb = False
        y = H
        pg.draw.circle(sc, BLUE, (x_b, y_b), 40)
        pg.display.update()
        pg.time.delay(200)
        
        
            
        print(bomb)

        
            
            
    
    pg.time.delay(20)