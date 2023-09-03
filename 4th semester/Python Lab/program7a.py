import math


class shape:
    def __init__(self):
        self.area = 0
        self.name = " "

    def showarea(self):
        print("Area of", self.name, "is", self.area)


class circle(shape):
    def __init__(self, radius):
        self.area = 0
        self.name = "circle"
        self.radius = radius

    def calcarea(self):
        self.area = math.pi * self.radius ** 2


class rectangle(shape):
    def __init__(self, l, b):
        self.area = 0
        self.name = "rectangle"
        self.l = l
        self.b = b

    def calcarea(self):
        self.area = self.l * self.b


class triangle(shape):
    def __init__(self, h, b):
        self.area = 0
        self.name = "triangle"
        self.h = h
        self.b = b

    def calcarea(self):
        self.area = 1 / 2 * self.h * self.b


c = circle(5)
c.calcarea()
c.showarea()
r = rectangle(5, 6)
r.calcarea()
r.showarea()
t = triangle(6, 7)
t.calcarea()
t.showarea()
