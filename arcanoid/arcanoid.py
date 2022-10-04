import pygame

from Ball import Ball
pygame.init()
 
FPS = 30

dis=pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('Арканоид')
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

b1 = Ball(20,20,100,100,dis)

game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('fdfd')
            if event.key == pygame.K_LEFT:
                print('fdfd')
    dis.fill(white)
   
    b1.draw()
    pygame.draw.rect(dis, black, [20, 20, 10, 10])
    pygame.display.update()
    clock.tick(FPS)

 
pygame.quit()