class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return ((self.x)**2 + (self.y)**2)**0.5
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    '''A class to manufacture rectangle objects'''
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

if __name__ == "__main__":
    box = Rectangle(Point(0,0), 4, 1)
    bomb = Rectangle(Point(5,3), 2, 2)
    print("box:", box)
    print("bomb:", bomb)
    input()
