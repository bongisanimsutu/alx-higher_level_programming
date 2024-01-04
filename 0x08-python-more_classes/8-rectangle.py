#!/usr/bin/python3
"""
This script, 8-rectangle, is created for Holberton Python project 0x08 task 8.
"""

class Rectangle:
    """
    Class for printing or computation of dimensions of a rectangle.

    Takes in args for width and height of a rectangle, and contains methods for calculation of the area or perimeter. __str__, __repr__, and __del__ functionality defined below.

    Attributes:
        number_of_instances (int): counter incrementing for every instantiation, and decrementing for every instance deletion.
        print_symbol (str): single character to be used in assembling string representation of rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Increments `number_of_instances` and calls setters for `__width` and `__height`.

        Args:
            width (int): horizontal dimension of rectangle, defaults to 0
            height (int): vertical dimension of rectangle, defaults to 0
        """
        type(self).number_of_instances += 1
        # attribute assignment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for __width."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for __height."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangle represented by the current instance."""
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instances."""
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval()."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrements `number_of_instances`, then prints message upon deletion of instance."""
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

