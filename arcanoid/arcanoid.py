import pygame

from Ball import Ball

from Player import Player

from Brick import Brick

pygame.init()
 
FPS = 30

def check_collision(obj1, obj2):
    """подразумеваем только прямоугольные границы коллизий"""
    b1 = obj1.get_bounds()
    b2 = obj2.get_bounds()
    if b1[1][0] < b2[0][0] or b1[0][0]>b2[1][0] or b1[0][1]>b2[1][1] or b1[1][1]<b2[0][1]:
        return (False, )

    bound_intesect = {}
    bound_intesect['1_side'] = max(b1[0][0], b2[0][0])
    bound_intesect['2_side'] = min(b1[1][0], b2[1][0])
    bound_intesect['3_side'] = min(b1[1][1], b2[1][1])
    bound_intesect['4_side'] = max(b1[0][1], b2[0][1])

    width = abs(bound_intesect['1_side'] - bound_intesect['2_side'])
    height = abs(bound_intesect['3_side'] - bound_intesect['4_side'])
    #print(bound_intesect)
    print(width, height)
    if(width * height == 0):
        width = height =0

    return (True, width, height)
        
def get_normal(ball, obj, width, height):
    old_x = ball.x - ball.dx * width
    old_y = ball.y - ball.dy * height
    
    ball.x = old_x
    ball.y = old_y
    b = ball.get_bounds()
    ob = obj.get_bounds()
    if ob[0][1] == ball.y + ball.height: return (0, -1)
    if ob[1][1] == ball.y: return (0, 1)
    if ob[0][0] == ball.x + ball.width: return (-1, 0)
    if ob[1][0] == ball.x: return (1, 0)

    return (0, 0)


dis=pygame.display.set_mode((800, 1000))
pygame.display.update()
pygame.display.set_caption('Арканоид')
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

b1 = Ball(20,20,10,10,dis, black)
b2 = Ball(50,20,10,10,dis, black)

p1 = Player(dis)


objects = []
objects.append(p1)
objects.append(b1)
objects.append(b2)

objects.append(Brick(200, 300, 100, 30, dis, black))

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

    for ball in objects:
        if isinstance(ball, Ball):
            for obj in objects:
                if isinstance(obj, Player) or isinstance(obj, Brick):
                    collis = check_collision(obj, ball)
                    if collis[0]:     #временное решение
                        normal_2 = get_normal(ball, obj, collis[1], collis[2])
                        #ball.set_v_by_n(normal_2)
                        #print(normal_2)
                        ball.dy = ball.dy if normal_2[1] == 0 else normal_2[1] 
                        ball.dx = ball.dx if normal_2[0] == 0 else normal_2[0] 
                        #objects.remove(obj)
    pygame.display.update()
    clock.tick(FPS)

 
pygame.quit()