import pygame
from ObjectClass import AbcObjectClass




class Player(AbcObjectClass):
    def __init__(self, spawn_x, spawn_y, speed, display, width = 100, height = 20, color:tuple = (100,100,100), is_playable = True, id = False):
        y = spawn_y if spawn_y != -1 else display.get_height() - height
        super().__init__((spawn_x, y), (width, height), id)
        self.__base_speed = self.speed = speed
        #self.__baffs = []
        self.display = display
        self.color = color
        self.move_r = False
        self.move_l = False
        self.is_playable = is_playable

    def move_right(self, e_type):
        if e_type == pygame.KEYDOWN: self.move_r = True
        if e_type == pygame.KEYUP: self.move_r = False

    def move_left(self, e_type):
        if e_type == pygame.KEYDOWN: self.move_l = True
        if e_type == pygame.KEYUP: self.move_l = False

    def handle_key_event(self, e_key_in, action):
        def handler(e_type, e_key):
            if e_key_in == e_key:
                action(e_type)
        return handler

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
