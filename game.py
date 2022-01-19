# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, userword):
        if userword =='':
            return False
        tmpgrid=self.grid.copy()
        for letter in userword :
            if letter not in tmpgrid:
                return False
            tmpgrid.remove(letter)
        return True
