from random import randint

class Die():
    """ A class representing a sinle die"""

    def __init__(self, num_sides = 6):
        """Initialize die attribues"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random integer between 1 and num_sides """
        number = randint(1,self.num_sides)
        return number

        