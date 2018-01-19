import copy
from random import Random
import unittest
from unittest.mock import patch

from game import Card, Deck


class TestDeck(unittest.TestCase):
    """
    Test the Deck class from the Game library
    """
    def setUp(self):
        # Mock the use of the random lib to add a seed
        # The will ensure deterministic tests on the Deck
        self.random = Random(666)

    @patch('game.deck.random')
    def test_deal_returns_card(self, random):
        random.randint._mock_side_effect = self.random.randint
        random.shuffle._mock_side_effect = self.random.shuffle

        deck = Deck()
        card = deck.deal()

        self.assertIsInstance(card, Card)

    @patch('game.deck.random')
    def test_deal_remove_card_from_cards(self, random):
        random.randint._mock_side_effect = self.random.randint
        random.shuffle._mock_side_effect = self.random.shuffle

        deck = Deck()
        card = deck.deal()

        self.assertNotIn(card, deck.cards)

    @patch('game.deck.random')
    def test_deal_adds_card_to_dealt(self, random):
        random.randint._mock_side_effect = self.random.randint
        random.shuffle._mock_side_effect = self.random.shuffle

        deck = Deck()
        card = deck.deal()

        self.assertIn(card, deck.dealt)

    @patch('game.deck.random')
    def test_shuffle_updates_order_of_cards(self, random):
        random.randint._mock_side_effect = self.random.randint
        random.shuffle._mock_side_effect = self.random.shuffle

        deck = Deck()

        cards = copy.deepcopy(deck.cards)
        deck.shuffle()
        new_cards = deck.cards

        self.assertNotEqual(cards, new_cards)
