class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x)**2 + (self.y)**2)**0.5

    def halfway(self, target):
        midx = (self.x + target.x)/2
        midy = (self.y + target.y)/2
        return Point(midx, midy)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
        '''A class to manufacture rectangle objects'''

        def __init__(self, posn, w, h):
            '''Initialize rectangle at posn, with width w and height h'''
            self.corner = posn
            self.width = w
            self.height = h

        def __str__(self):
            return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

        def grow(self, delta_width, delta_height):
            '''Grows (or shrinks) the object by the given deltas'''
            self.width += delta_width
            self.height += delta_height

        def move(self, dx, dy):
            '''Moves this object by the deltas'''
            self.corner.x += dx
            self.corner.y += dy

        def did_collide(self, tgt):
            def get_corners(tgt):
                '''Returns a tuple of Points defining three of the rectangles
                    corners,top-left, top-right,bottom-left, and bottom-right
                    in order.'''
                return (tgt.corner, Point(tgt.corner.x + tgt.width, tgt.corner.y),
                        Point(tgt.corner.x, tgt.corner.y - tgt.height),
                        Point(tgt.corner.x + tgt.width, tgt.corner.y + tgt.height))

            def is_corner_inside(self, tgt):
                '''Checks if any corner points of self are inside span of tgt.'''
                self_corners = get_corners(self)
                tgt_corners = get_corners(tgt)
                for corner_points in self_corners:
                    if (corner_points.x < tgt_corners[1].x and
                            corner_points.x > tgt_corners[0].x and
                            corner_points.y < tgt_corners[0].y and
                            corner_points.y > tgt_corners[2].y):
                        return True
                return False

            if is_corner_inside(self, tgt) or is_corner_inside(tgt, self):
                return True
            return False


if __name__ == "__main__":
    box = Rectangle(Point(2, 5), 5, 4)
    t1 = Rectangle(Point(6, 4), 3, 2)
    t2 = Rectangle(Point(3, 3), 2, 5)
    t3 = Rectangle(Point(1, 3), 4, 1)
    t4 = Rectangle(Point(4, 6), 2, 4)
    t5 = Rectangle(Point(6, 6), 3, 2)
    t6 = Rectangle(Point(6, 2), 3, 2)
    t7 = Rectangle(Point(1, 2), 3, 2)
    t8 = Rectangle(Point(1, 6), 3, 3)
    t9 = Rectangle(Point(4, 3), 2, 1)
    t10 = Rectangle(Point(1, 7), 8, 8)
    t11 = Rectangle(Point(9, 7), 3, 3)
    assert box.did_collide(t1) is True
    assert box.did_collide(t2) is True
    assert box.did_collide(t3) is True
    assert box.did_collide(t4) is True
    assert box.did_collide(t5) is True
    assert box.did_collide(t6) is True
    assert box.did_collide(t7) is True
    assert box.did_collide(t8) is True
    assert box.did_collide(t9) is True
    assert box.did_collide(t10) is True
    assert box.did_collide(t11) is False
    # tp = Point(2,3)
    # tp2 = Point(4, 5)
    # box = Rectangle(tp, 5, 3)
    # bomb = Rectangle(Point(5, 9), 2, 2)
    # assert tp.halfway(tp2).x == Point(3, 4).x
    # assert tp.halfway(tp2).y == Point(3, 4).y
    # assert str(box) == "((2, 3), 5, 3)"
    # assert str(box.grow(-2, 3)) == "((2.0, 3.0), 3.0, 6.0)"
    # assert str(box.move(1, 1)) == "((3.0, 4.0), 5.0, 3.0)"
    # input()
