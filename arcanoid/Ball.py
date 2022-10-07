from cmath import sqrt
import pygame
from ObjectClass import AbcObjectClass

class Ball(AbcObjectClass):
    """Класс игрового шара"""
    def __init__(self, x, y, width, height, display, color:tuple):
        super().__init__((x, y), (width, height))
        self.display = display
        self.color = color

        self.dx = 1
        self.dy = 1
        norma = (self.dx * self.dx + self.dy * self.dy)**(0.5)
        #print (norma)
        #self.dx = self.dx / norma
        #self.dy = self.dy / norma

        self.speed_x = 5
        self.speed_y = 10

    def update(self):
        new_x = self.x + self.speed_x * self.dx
        new_y = self.y + self.speed_y * self.dy

        if new_x + self.width > self.display.get_width() or new_x < 0:  #обработка столкновения со стенами
            self.dx = 1 if new_x < 0 else -1
            new_x = self.x + self.speed_x * self.dx

        if new_y + self.height > self.display.get_height() or new_y < 0:
            self.dy = 1 if new_y < 0 else -1
            new_y = self.y + self.speed_y * self.dy

        self.x = new_x
        self.y = new_y

    def draw(self):
        self.update()
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

    def get_bounds(self):
        return ((self.x, self.y),(self.x + self.width, self.y + self.height))

    def set_v_by_n(self, n: tuple):
        """Устанавливает вектор скорости сонаправленным с нормальню"""
        scalar_m = n[0] * self.dx + n[1] * self.dy
        if scalar_m < 0:      #угол больше 90 градусов
            #proekz_perpend = (n[0] * scalar_m, n[1] * scalar_m)
            self.dx = self.dx - 2 * scalar_m * n[0]
            self.dy = self.dy - 2 * scalar_m * n[1]