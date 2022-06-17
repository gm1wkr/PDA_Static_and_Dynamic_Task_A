import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_value_2 = Card(1, 2)
        self.card_value_8 = Card(1, 8)
        self.card_ace = Card(2, 1)
        self.game = CardGame()

    def test_check_for_ace_has__true(self):
        card_has_ace = self.game.check_for_ace(self.card_ace)
        self.assertEqual(True, card_has_ace)

    def test_check_for_ace__false(self):
        card_has_ace = self.game.check_for_ace(self.card_value_2)
        self.assertEqual(False, card_has_ace)

    def test_highest_card__false(self):
        returned_card = self.game.highest_card(self.card_value_2, self.card_value_8)
        self.assertEqual(8, returned_card.value)

    def test_highest_card__True(self):
        returned_card = self.game.highest_card(self.card_value_8, self.card_value_2)
        self.assertEqual(8, returned_card.value)

    def test_cards_total__fails(self):
        card_list = [self.card_value_2, self.card_value_8]
        total_value = self.game.cards_total(card_list)
        self.assertNotEqual("You have a total of 8", total_value)

    def test_cards_total__pass(self):
        card_list = [self.card_value_2, self.card_value_8]
        total_value = self.game.cards_total(card_list)
        self.assertEqual("You have a total of 10", total_value)
