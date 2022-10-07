import pygame
import settings as stgs

from ObjectClass import AbcObjectClass

from Ball import Ball

from Player import Player

from Brick import Brick

class Game():
    """Класс игры"""
    def __init__(self):
        self.dis = pygame.display.set_mode((800, 700))
        pygame.display.update()
        pygame.display.set_caption(stgs.name_game)

        self.clock = pygame.time.Clock()
        self.objects = []
        self.player = 0
        self.end_game = False

    def __check_collision(self, obj1, obj2):
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
        
    def __get_normal(self, ball, obj, width, height):
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

    def __check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.end_game=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #перенести в игрока
                    self.player.move_r = True
                if event.key == pygame.K_LEFT:
                    self.player.move_l = True

                if event.key == pygame.K_UP:
                    self.create_ball()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.move_r = False
                if event.key == pygame.K_LEFT:
                    self.player.move_l = False
        
    def __processing_collision(self):
        for dynamic_obj in self.objects:        #перебираем динамические объекты
            if not dynamic_obj.is_static:
                for static_obj in self.objects:      #берем статический объект
                    if isinstance(static_obj, AbcObjectClass) and not static_obj is dynamic_obj and static_obj.is_comm_dyn:         #если этот объект может взаимодействовать с другими динамическими объектами
                        collis = self.__check_collision(static_obj, dynamic_obj)
                        if collis[0]:
                            normal_2 = self.__get_normal(dynamic_obj, static_obj, collis[1], collis[2])
                            dynamic_obj.dy = dynamic_obj.dy if normal_2[1] == 0 else normal_2[1]
                            dynamic_obj.dx = dynamic_obj.dx if normal_2[0] == 0 else normal_2[0]

                            if dynamic_obj.hit(static_obj):
                                self.objects.remove(dynamic_obj)

                            if static_obj.hit(dynamic_obj):
                                self.objects.remove(static_obj)


    def create_player(self):
        self.player = Player(0, 20, self.dis)
        self.objects.append(self.player)

    def create_ball(self, old_ball = False):
        if old_ball:
            pass
        else:
            ball = Ball(self.player.x + self.player.width/2, self.player.y - 20, 20, 20, self.dis, stgs.Colors.c_black)
            self.objects.append(ball)

    def create_brick(self, x, y, w, h, color:tuple = (0,0,0)):
        brick = Brick(x, y, w, h, self.dis, color)
        self.objects.append(brick)

    def create_objects(self):
        self.create_player()
        self.create_ball()
        # self.create_brick(100, 100, 50, 100)
        for i in range(10):
            for j in range(10):
                self.create_brick(i*100, j*50, 80, 30, stgs.Colors.get_random_c())



    def start_game(self):
        self.create_objects()
        while not self.end_game:
            self.dis.fill(stgs.Colors.c_white)
            self.__check_event()
            for obj in self.objects:
                obj.draw()

            self.__processing_collision()
                            #objects.remove(obj)
            pygame.display.update()
            self.clock.tick(stgs.FPS)
        pygame.quit()


