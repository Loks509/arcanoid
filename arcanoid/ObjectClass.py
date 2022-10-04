from abc import ABC, abstractmethod

class AbcObjectClass(ABC):
    """description of class"""

    def __init__(self, coord:tuple, size_obj:tuple):
        self.coord_x = coord[0]
        self.coord_y = coord[1]

        self.obj_width = size_obj[0]
        self.obj_height = size_obj[1]

    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def get_bounds():
        pass