from abc import ABC, abstractmethod

class AbcObjectClass(ABC):
    """description of class"""

    def __init__(self, coord:tuple, size_obj:tuple):
        self.x = coord[0]
        self.y = coord[1]

        self.width = size_obj[0]
        self.height = size_obj[1]
        self.is_static = True       #по умолчанию все объекты статические
        self.is_comm_dyn = True    #Взаимодействие с другими динамическими объектами

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

    def hit(self, obj):
        """Вызывается при ударе по объекту, получает объект, который ударился"""
        return False
