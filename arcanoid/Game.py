import pygame
import settings as stgs
import time
from threading import Thread

import ClassConnectTCP as tcpcon

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
        self.list_event_handler = []
        self.player = 0
        self.opponent = 0
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
        # print(width, height)
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
                if event.key == pygame.K_UP:
                    self.create_ball()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                for event_handler in self.list_event_handler:
                    event_handler(event.type, event.key)
        
    def __processing_collision(self):
        for id_dyn, dynamic_obj in enumerate(self.objects):        #перебираем динамические объекты
            if not dynamic_obj.is_static:
                for id_stat, static_obj in  enumerate(self.objects):      #берем статический объект
                    if isinstance(static_obj, AbcObjectClass) and not static_obj is dynamic_obj and static_obj.is_comm_dyn:         #если этот объект может взаимодействовать с другими динамическими объектами
                        collis = self.__check_collision(static_obj, dynamic_obj)
                        if collis[0]:
                            normal_2 = self.__get_normal(dynamic_obj, static_obj, collis[1], collis[2])
                            dynamic_obj.dy = dynamic_obj.dy if normal_2[1] == 0 else normal_2[1]
                            dynamic_obj.dx = dynamic_obj.dx if normal_2[0] == 0 else normal_2[0]

                            if dynamic_obj.hit(static_obj):
                                del self.objects[id_dyn]
                                #self.objects.remove(dynamic_obj)

                            if static_obj.hit(dynamic_obj):
                                del self.objects[id_stat]

                                #self.objects.remove(static_obj)


    def create_player(self, key_right = False, key_left = False, speed = 20, x = 0, y = -1):
        player = Player(x, y, speed, self.dis)
        self.objects.append(player)
        if key_right:
            self.list_event_handler.append(player.handle_key_event(key_right, player.move_right))
        if key_left:
            self.list_event_handler.append(player.handle_key_event(key_left, player.move_left))
        return player

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
        self.player = self.create_player(pygame.K_RIGHT, pygame.K_LEFT)
        self.opponent = self.create_player(False, False,20,0,0)
        self.create_ball()
        # self.create_brick(100, 100, 50, 100)
        for i in range(10):
            for j in range(10):
                self.create_brick(i*100, j*50, 80, 30, stgs.Colors.get_random_c())


    def Trash(self):
        for id, obj in enumerate(self.objects):
            if obj.is_deleted:
                del self.objects[id]
                #self.objects.remove(obj)

    def recvGameData(self):
        while True:
            data = self.test.recvData()
            if(data):
                self.opponent.x = data[0]

    def sendGameData(self):
        while True:
            self.test.sendData([self.player.x])
            time.sleep(1/60)
    
    def sendGameStateFromServer(self):
        while True:
            data = [[obj.x, obj.y, obj.width, obj.height] for obj in self.objects]
            self.test.sendData(data)
            time.sleep(1/60)

    def recvGameStateFromServer(self):
            data = self.test.recvData()
            if(data):
                for obj in data:
                    pygame.draw.rect(self.dis, stgs.Colors.c_black, [obj[0], obj[1], obj[2], obj[3]])

    def start_game(self):
        self.create_objects()
        v_type = input('type')
        if v_type == '1':
            self.test = tcpcon.Server('192.168.1.104',8888)
            p1 = Thread(target = self.sendGameStateFromServer, daemon = True)
            p2 = Thread(target = self.recvGameData, daemon = True)
            p2.start()
            p1.start()
        else:
            self.test = tcpcon.Client('192.168.1.104',8888)
            # p1 = Thread(target = self.recvGameStateFromServer, daemon = True)
            # p2 = Thread(target = self.recvGameData, daemon = True)
        
        
        while not self.end_game:
            # print(int(self.clock.get_fps()))
            
            self.dis.fill(stgs.Colors.c_white)
            self.__check_event()
            if v_type == '1':
                self.Trash()
                
                for obj in self.objects:
                    obj.draw()

                self.__processing_collision()
                            #objects.remove(obj)
            else:
                self.recvGameStateFromServer()
            pygame.display.update()
            self.clock.tick(stgs.FPS)
        pygame.quit()


