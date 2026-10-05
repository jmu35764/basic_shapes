from basic_shapes import BasicShape

class Circle(BasicShape):
    def __init__(self, _name, _area, r:float, x:float, y:float):
        super().__init__(_name, _area)
        self._name = "Circle"
        self._radius = r
        self._x_center = x
        self._y_center = y








