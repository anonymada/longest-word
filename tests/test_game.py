from distutils.fancy_getopt import FancyGetopt
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def empty_world_is_valid(self):
        new_game = Game()
        self.assertEqual(new_game.is_valid(''),False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('AZERTYUIO')
        self.assertIs(new_game.is_valid("ROUTE"),True)
        self.assertEqual(new_game.grid,list('AZERTYUIO'))

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('AZERTYUIO')
        self.assertIs(new_game.is_valid("MOTARD"),False)
        self.assertEqual(new_game.grid,list('AZERTYUIO'))
    
    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Forcer la grille à un scénario de test :
      self.assertIs(new_game.is_valid('FEUN'), False)
