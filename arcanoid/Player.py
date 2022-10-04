from ObjectClass import AbcObjectClass

class Player(AbcObjectClass):
    def __init__(self):
        self.x = 0
        self.speed = 1
        self.size_x = 15
        self.size_y = 5


    def move(self, dx):
        self.x += dx * self.speed
        return self.x

    def get_x(self):
        return self.x

    def draw(self):
        pass
