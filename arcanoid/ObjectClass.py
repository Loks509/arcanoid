from abc import ABC, abstractmethod

class AbcObjectClass(ABC):
    """description of class"""
    id = 1
    def __init__(self, coord:tuple, size_obj:tuple, id:int):
        self.x = coord[0]
        self.y = coord[1]

        self.width = size_obj[0]
        self.height = size_obj[1]
        self.is_static = True       #по умолчанию все объекты статические
        self.is_comm_dyn = True    #Взаимодействие с другими динамическими объектами
        self.is_deleted = False
        if id:
            self.id = id
            if AbcObjectClass.id < id:
                AbcObjectClass.id = id      #у клиента сначала приходят все объекты, потом он может создавать свои
        else:
            self.id = AbcObjectClass.id
        AbcObjectClass.id+=1

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

    # @abstractmethod
    # def get_data_to_send():
    #     """возвращет данные для отправки в виде списка"""
    #     pass

    def hit(self, obj):
        """Вызывается при ударе по объекту, получает объект, который ударился"""
        return False
