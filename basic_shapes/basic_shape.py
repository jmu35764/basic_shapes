from ABC import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, _name: str, _area: float = 0)
        self._name = _name
        self._area = _area

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstratmethod
    def area(self):
        pass

    @area.setter
    @abstractmethod
    def area(self, value):
        pass

    @abstractmethod
    def calc_area(self):
        pass




