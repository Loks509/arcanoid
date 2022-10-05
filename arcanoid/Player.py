import pygame
from ObjectClass import AbcObjectClass

class Player(AbcObjectClass):
    def __init__(self, display):
        self.x = 0
        self.speed = 5
        self.width = 100
        self.height = 20
        self.display = display
        self.color = (100,100,100)
        self.move_r = False
        self.move_l = False
        self.y = self.display.get_height() - self.height

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
