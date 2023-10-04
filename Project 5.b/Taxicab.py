# Author: Leonel Garay
# Date: 10/30/2019
# Description: Taxicab class that holds X & Y coordinates as well as odometer. Project 5b.


class Taxicab:
    """Holds Current X & Y Coordinate as well as odometer."""

    def __init__(self, _x_coord, _y_coord, _odometer=0):
        """Takes two parameters to initialize the coordinates and initializes the odometer to zero """
        self._x_coord = _x_coord  # x_coord is a private attribute
        self._y_coord = _y_coord  # y_coord is a private attribute
        self._odometer = _odometer  # odometer is a private attribute

    def get_x_coord(self):
        """Returns X Coordinate"""
        return self._x_coord

    def get_y_coord(self):
        """Returns Y Coordinate"""
        return self._y_coord

    def get_odometer(self):
        """Returns the Odometer"""
        return self._odometer

    def move_x(self, move_x):
        """Tells how far the Taxicab should shift left or right"""
        self._odometer += abs(move_x)  # Update Odometer using the absolute value of move_x
        self._x_coord += move_x # Updates X Coordinates using move_x

    def move_y(self, move_y):
        """Tells how far the Taxicab should shift up or down"""
        self._odometer += abs(move_y)  # Update Odometer using the absolute value of move_y
        self._y_coord += move_y  # Updates Y Coordinates using move_y
