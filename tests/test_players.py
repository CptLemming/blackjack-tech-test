import copy
import unittest

from game import Card, FaceCard, AceCard, Player


class TestPlayer(unittest.TestCase):
    """
    Test the Player class from the Game library
    """
    def test_take_card_adds_card_to_cards(self):
        player = Player()
        card = Card('2', 'heart', 2)
        player.take_card(card)

        self.assertListEqual(player.cards, [card])

    def test_get_value_returns_value_of_player_cards(self):
        player = Player()
        player.take_card(Card('2', 'heart', 2))
        player.take_card(Card('3', 'heart', 3))

        value = player.get_value()

        self.assertEqual(value, 5)

    def test_get_value_uses_ace_as_11_below_or_equal_21(self):
        player = Player()
        player.take_card(Card('2', 'heart', 2))
        player.take_card(AceCard('Ace', 'heart'))

        value = player.get_value()

        self.assertEqual(value, 13)

    def test_get_value_uses_ace_as_1_if_value_exceeds_21(self):
        player = Player()
        player.take_card(Card('9', 'heart', 9))
        player.take_card(Card('9', 'spade', 9))
        player.take_card(AceCard('Ace', 'heart'))

        value = player.get_value()

        self.assertEqual(value, 19)

    def test_is_bust_returns_false_when_below_21(self):
        player = Player()
        player.take_card(Card('2', 'heart', 2))
        player.take_card(Card('3', 'heart', 3))

        outcome = player.is_bust()

        self.assertFalse(outcome)

    def test_is_bust_returns_false_when_equal_21(self):
        player = Player()
        player.take_card(Card('9', 'heart', 9))
        player.take_card(Card('9', 'spade', 9))
        player.take_card(Card('3', 'diamond', 3))

        outcome = player.is_bust()

        self.assertFalse(outcome)

    def test_is_bust_returns_true_when_over_21(self):
        player = Player()
        player.take_card(Card('9', 'heart', 9))
        player.take_card(Card('9', 'spade', 9))
        player.take_card(Card('9', 'diamond', 9))

        outcome = player.is_bust()

        self.assertTrue(outcome)

    def test_has_blackjack_returns_false_when_not_21(self):
        player = Player()
        player.take_card(Card('2', 'heart', 2))
        player.take_card(Card('3', 'heart', 3))

        outcome = player.has_blackjack()

        self.assertFalse(outcome)

    def test_has_blackjack_returns_true_when_21(self):
        player = Player()
        player.take_card(Card('9', 'heart', 9))
        player.take_card(Card('9', 'spade', 9))
        player.take_card(Card('3', 'diamond', 3))

        outcome = player.has_blackjack()

        self.assertTrue(outcome)
