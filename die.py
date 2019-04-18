from random import randint


class Die():
    """ a class represetning a single dice"""

    def __init__(self, num_sides=6):
        """assume a 6 sided dice"""
        self.num_sides = num_sides

    def roll(self):
        """ retrun a random number between 1 and the number of sides"""
        return randint(1, self.num_sides)
