import pygame

from Ball import Ball

from Player import Player

pygame.init()
 
FPS = 30

def check_collision(obj1, obj2):
    """подразумеваем только прямоугольные границы коллизий"""
    b1 = obj1.get_bounds()
    b2 = obj2.get_bounds()
    if b1[1][0] < b2[0][0] or b1[0][0]>b2[1][0] or b1[0][1]>b2[1][1] or b1[1][1]<b2[0][1]:
        return False
    else:
        return True
        
def get_normal(obj1, obj2):
    pass


dis=pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('Арканоид')
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

b1 = Ball(20,20,10,10,dis, black)

p1 = Player(dis)


objects = []
objects.append(b1)
objects.append(p1)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #перенести в игрока
                p1.move_r = True
            if event.key == pygame.K_LEFT:
                p1.move_l = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                p1.move_r = False
            if event.key == pygame.K_LEFT:
                p1.move_l = False
    dis.fill(white)
   
    for obj in objects:
        obj.draw()
    if check_collision(p1, b1):     #временное решение
        b1.dy = -b1.dy
    pygame.display.update()
    clock.tick(FPS)

 
pygame.quit()