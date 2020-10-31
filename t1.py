class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print(self.side * self.side)


class Cube(Square):
    def area(self):
        super().__init__(2)
        super().area()
        face_area = self.side * self.side
        return face_area * 6

def volume(self):
        face_area = self.side * self.side
        return face_area * self.side
cs = Cube(2)
print(cs.area())