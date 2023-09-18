#!/usr/bin/python3
"""A class module to represent a square."""


class Square():
    """A class to represent a square."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize square with given width."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate and return the area of the square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate and return the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a string representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
