from basic_shapes import BasicShape

class Circle(BasicShape):
    def __init__(self, _name, _area, r, x, y):
        super().__init__(_name, _area)
        self._radius = r
        self._x_center = x
        self._y_center = y

    def name(self):
        _name = "Circle"
        return self._name

    def area(self):





