# import randint() function
from random import randint


class Die:
    """a class representing a single die"""

    # instance of die will always have 6 sides
    # attribute of class num_sides is generated with 6 sides
    # can be changed if an argument is made calling the class Die(8)
    def __init__(self, num_sides=6):
        """assume a six-sided die"""
        self.num_sides = num_sides

    # randint() returns random whole number between 1 & num_sides
    # includes 1 & 6
    def roll(self):
        """return a random value between 1 & number of sides"""
        return randint(1, self.num_sides)
