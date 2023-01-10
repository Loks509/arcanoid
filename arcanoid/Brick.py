import pygame
from ObjectClass import AbcObjectClass

class Brick(AbcObjectClass):
    """Класс кирпичика"""
    def __init__(self, x, y, width, height, display, color:tuple, count_lifes = 1, id = False):
        super().__init__((x, y), (width, height), id)
        self.display = display
        self.color = color
        self.count_lifes = count_lifes

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

    def get_bounds(self):
        return ((self.x, self.y),(self.x + self.width, self.y + self.height))

    def hit(self, obj):
        """Если количество попаданий по блоку закончилось, то возвращает True"""
        self.count_lifes -= 1
        return True if self.count_lifes == 0 else False