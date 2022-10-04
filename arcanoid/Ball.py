import pygame
from ObjectClass import AbcObjectClass

class Ball(AbcObjectClass):
    """description of class"""
    def __init__(self, x, y, width, height, display):
        super().__init__((x, y), (width, height))
        self.display = display

    def draw(self):
        pygame.draw.rect(self.display, (0,0,0), [self.coord_x, self.coord_y, self.obj_width, self.obj_height])

    def get_bounds(self):
        pass



