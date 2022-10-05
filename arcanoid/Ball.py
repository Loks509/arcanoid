import pygame
from ObjectClass import AbcObjectClass

class Ball(AbcObjectClass):
    """Класс игрового шара"""
    def __init__(self, x, y, width, height, display, color:tuple):
        super().__init__((x, y), (width, height))
        self.display = display
        self.color = color
        self.dx = 1
        self.dy = 2
        self.speed = 5

    def update(self):
        new_x = self.x + self.speed * self.dx
        new_y = self.y + self.speed * self.dy

        if new_x + self.width > self.display.get_width() or new_x < 0:
            self.dx = -self.dx
            new_x = self.x + self.speed * self.dx

        if new_y + self.height > self.display.get_height() or new_y < 0:
            self.dy = -self.dy
            new_y = self.y + self.speed * self.dy

        self.x = new_x
        self.y = new_y

    def draw(self):
        self.update()
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

    def get_bounds(self):
        return ((self.x, self.y),(self.x + self.width, self.y + self.height))



