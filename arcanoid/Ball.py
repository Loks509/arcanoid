import pygame
from ObjectClass import AbcObjectClass

class Ball(AbcObjectClass):
    """description of class"""
    def __init__(self, x, y, width, height, display, color:tuple):
        super().__init__((x, y), (width, height))
        self.display = display
        self.color = color
        self.dx = 1
        self.dy = 1
        self.speed = 1

    def update(self):
        new_x = self.coord_x + self.speed * self.dx
        new_y = self.coord_y + self.speed * self.dy

        if new_x + self.obj_width > self.display.get_width() or new_x < 0:
            self.dx = -self.dx
            new_x = self.coord_x + self.speed * self.dx

        if new_y + self.obj_height > self.display.get_height() or new_y < 0:
            self.dy = -self.dy
            new_y = self.coord_y + self.speed * self.dy

        self.coord_x = new_x
        self.coord_y = new_y

    def draw(self):
        self.update()
        pygame.draw.rect(self.display, self.color, [self.coord_x, self.coord_y, self.obj_width, self.obj_height])

    def get_bounds(self):
        pass



