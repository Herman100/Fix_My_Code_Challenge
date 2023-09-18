#!/usr/bin/python3
""" Calculating geometry of square """


class Square:
    """ square parameters calc """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return f"Square (Width: {self.width}, Height: {self.height})"


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
