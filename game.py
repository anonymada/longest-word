# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests

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
        return self.__check_dictionary(userword)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
