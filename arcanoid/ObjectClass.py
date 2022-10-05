from abc import ABC, abstractmethod

class AbcObjectClass(ABC):
    """description of class"""

    def __init__(self, coord:tuple, size_obj:tuple):
        self.x = coord[0]
        self.y = coord[1]

        self.width = size_obj[0]
        self.height = size_obj[1]

    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def update():
        pass
    @abstractmethod
    def get_bounds():
        """возвращет верхнюю левую и нижнюю правую точку"""
        pass