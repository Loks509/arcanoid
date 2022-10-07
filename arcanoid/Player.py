import pygame
from ObjectClass import AbcObjectClass

class Player(AbcObjectClass):
    def __init__(self, spawn_x, speed, display, width = 100, height = 20, color:tuple = (100,100,100)):
        super().__init__((spawn_x, display.get_height() - height), (width, height))
        self.__base_speed = self.speed = speed
        self.__baffs = []
        self.display = display
        self.color = color
        self.move_r = False
        self.move_l = False

    def handle_key_event(self):
        pass

    def update(self):
        if self.move_r == self.move_l:
            return

        if (self.move_r and not self.move_l):       dx = 1
        elif (not self.move_r and self.move_l):     dx = -1
        else:                                       dx = 0
        #dx = 1 if (self.move_r and not self.move_l) else -1 if (not self.move_r and self.move_l) else 0  # if в одну строку

        self.x = self.x + dx * self.speed
        if self.x + self.width > self.display.get_width():
            self.x = self.display.get_width() - self.width

        if self.x < 0:
            self.x = 0

    def get_x(self):
        return self.x

    def draw(self):
        self.update()
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

    def get_bounds(self):
        return ((self.x, self.y),(self.x + self.width, self.y + self.height))
