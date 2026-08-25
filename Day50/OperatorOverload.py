


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def display(self):
        print(self.x, self.y)


class Vector(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)



o = Vector(11, 12)
o.add(o).display()
print(o.x, o.y)