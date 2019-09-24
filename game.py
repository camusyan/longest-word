from random import randint
import string
import requests

class Game:
    LETTERS = string.ascii_uppercase[:27]
    def __init__(self):

        self.grid = []
        for _ in range(0, 9):
            self.grid.append(self.LETTERS[randint(0, 25)])

    def is_valid(self, grid):
        for i in grid:
            if i not in self.LETTERS:
                return False
        if len(grid) > 7:
            return False

        return self.__check_dictionary(grid)

    def __check_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']
