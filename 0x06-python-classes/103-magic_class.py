#!/usr/bin/python3

class MagicClass():
    """Initialize and define methods area and circumference"""

    def __init__(self, radius):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) != int or type(radius) != float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculate area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calcualte circumference"""
        return 2 * math.pi * self.__radius
