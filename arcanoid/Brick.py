import pygame
from ObjectClass import AbcObjectClass

class Brick(AbcObjectClass):
    """Класс кирпичика"""
    def __init__(self, x, y, width, height, display, color:tuple):
        super().__init__((x, y), (width, height))
        self.display = display
        self.color = color

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

    def get_bounds(self):
        return ((self.x, self.y),(self.x + self.width, self.y + self.height))


