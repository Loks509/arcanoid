import random
FPS = 60

width = 800
height = 600

name_game = "Арканоид"
#Цвета
class Colors:
    c_white = (255, 255, 255)
    c_black = (0, 0, 0)
    c_red = (255, 0, 0)
    c_green = (0, 255, 0)
    c_blue = (0, 0, 255)
    c_lawnGreen = (124, 252, 0)
    c_pink = (255, 20, 147)
    c_aquamarine = (102, 205, 170)
    c_gray = (100, 100, 100)
    
    list_color = ['c_black', 'c_red', 'c_green', 'c_blue', 'c_lawnGreen', 'c_pink', 'c_aquamarine']
    @classmethod
    def get_random_c(cls):
        #list_attr = vars(cls)#.__dict__.keys()
        #print(list_attr)
        random_key = random.choice(cls.list_color)
        return getattr(cls, random_key)

color_player = Colors.c_gray
color_opponent = Colors.c_red
