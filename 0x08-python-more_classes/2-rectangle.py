#!/usr/bin/python3
"""
This script, 2-rectangle, is created for Holberton Python project 0x08 task 2.
"""

class Rectangle:
    """
    Takes arguments for the width and height of a rectangle and includes methods for calculating the area or perimeter.

    Args:
        width (int): Horizontal dimension of the rectangle, defaults to 0.
        height (int): Vertical dimension of the rectangle, defaults to 0.

    Attributes:
        __width (int): Horizontal dimension of the rectangle.
        __height (int): Vertical dimension of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes the instance with the specified width and height.
        area(self): Calculates and returns the area of the rectangle (__width * __height).
        perimeter(self): Calculates and returns the perimeter of the rectangle (0 if either attribute is 0, or (__width * 2) + (__height * 2)).

    Properties:
        width: Getter and setter for the private __width attribute.
        height: Getter and setter for the private __height attribute.

    Raises:
        TypeError: If the provided value for width or height is not an integer.
        ValueError: If the provided value for width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        # Attribute assignment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for __width."""
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
        """Getter method for __height."""
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

