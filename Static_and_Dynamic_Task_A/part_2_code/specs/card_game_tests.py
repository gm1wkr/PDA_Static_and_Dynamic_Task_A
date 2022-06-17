import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        card_value_2 = Card(1, 2)
        card_ace = Card(2, 1)
        game_with_ace = CardGame()

    def test_check_for_ace_has_ace(self):

        game_with_no_ace = CardGame(self.card_value_2)
        card_has_ace = game_with_no_ace.check_for_ace(self.card_value_2)

        self.AssertEqual(True, self.card_has_ace)
