from basic_shapes import BasicShape

class Circle(BasicShape):
    def __init__(self, _name, _area, r:float, x:float, y:float, n: str = "Circle"):
        super().__init__(_name, _area)
        self._radius = r
        self._x_center = x
        self._y_center = y
        self._name = n
        self._area = self.calc_area()


    def calc_area(self):
        self._area = 3.14 * (self._radius ** 2)
        return self._area









