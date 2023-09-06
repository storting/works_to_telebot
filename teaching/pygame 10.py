from random import randint
import pygame as pg
import sys
 

 
W = 400
H = 400
WHITE = (255, 255, 255)
CARS = ('car1.png', 'car2.png', 'car3.png')
# для хранения готовых машин-поверхностей
CARS_SURF = []
 
# надо установить видео режим
# до вызова image.load()
sc = pg.display.set_mode((W, H))
 
for i in range(len(CARS)):
    CARS_SURF.append(
        pg.image.load(CARS[i]).convert_alpha())
 
 
class Car(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(1, 3)
 
    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()
 
 
cars = pg.sprite.Group()
 
# добавляем первую машину,
# которая появляется сразу
Car(randint(1, W),
    CARS_SURF[randint(0, 2)], cars)
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(1, W),
                CARS_SURF[randint(0, 2)], cars)
 
    sc.fill(WHITE)
 
    cars.draw(sc)
 
    pg.display.update()
    pg.time.delay(20)
 
    cars.update()