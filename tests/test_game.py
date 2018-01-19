import unittest
from unittest.mock import patch

from game import Deck, Game, Player, Dealer


class TestDeck(unittest.TestCase):
    """
    Test the Game class from the Game library
    """
    def test_check_returns_dealer_when_player_is_bust(self):
        dealer = Dealer()
        deck = Deck()

        with patch.object(Player, 'is_bust', return_value=True):
            player = Player()

            game = Game(dealer=dealer, player=player, deck=deck)

            winner = game.check()

            self.assertEqual(dealer, winner)

    def test_check_returns_player_when_player_has_blackjack(self):
        dealer = Dealer()
        deck = Deck()

        with patch.object(Player, 'has_blackjack', return_value=True):
            player = Player()

            game = Game(dealer=dealer, player=player, deck=deck)

            winner = game.check()

            self.assertEqual(player, winner)

    def test_check_returns_player_when_player_is_done_and_dealer_is_bust(self):
        deck = Deck()

        with patch.object(Game, '_setup_game'):
            with patch.object(Dealer, 'is_bust', return_value=True):
                dealer = Dealer()
                player = Player()

                game = Game(dealer=dealer, player=player, deck=deck)
                game.is_player_done = True

                winner = game.check()

                self.assertEqual(player, winner)

    def test_check_returns_player_when_player_is_done_and_player_has_higher_value(self):
        deck = Deck()

        with patch.object(Game, '_setup_game'):
            with patch.object(Player, 'get_value', return_value=20):
                with patch.object(Dealer, 'get_value', return_value=10):
                    with patch.object(Dealer, 'has_reached_limit', return_value=True):
                        dealer = Dealer()
                        player = Player()

                        game = Game(dealer=dealer, player=player, deck=deck)
                        game.is_player_done = True

                        winner = game.check()

                        self.assertEqual(player, winner)

    def test_check_returns_dealer_when_player_is_done_and_player_has_lower_value(self):
        deck = Deck()

        with patch.object(Game, '_setup_game'):
            with patch.object(Player, 'get_value', return_value=20):
                with patch.object(Dealer, 'get_value', return_value=21):
                    with patch.object(Dealer, 'has_reached_limit', return_value=True):
                        dealer = Dealer()
                        player = Player()

                        game = Game(dealer=dealer, player=player, deck=deck)
                        game.is_player_done = True

                        winner = game.check()

                        self.assertEqual(dealer, winner)

    def test_check_returns_none_when_game_is_not_over(self):
        dealer = Dealer()
        deck = Deck()

        with patch.object(Player, 'is_bust', return_value=False):
            with patch.object(Player, 'has_blackjack', return_value=False):
                player = Player()

                game = Game(dealer=dealer, player=player, deck=deck)

                winner = game.check()

                self.assertIsNone(winner)

    def test_hit_calls_take_card(self):
        dealer = Dealer()
        player = Player()
        deck = Deck()

        with patch.object(Game, '_setup_game'):
            with patch.object(Game, '_take_card') as mock_method:
                game = Game(dealer=dealer, player=player, deck=deck)

                game.hit()

                mock_method.assert_called_once_with(player)

    def test_hit_calls_check(self):
        dealer = Dealer()
        player = Player()
        deck = Deck()

        with patch.object(Game, '_setup_game'):
            with patch.object(Game, 'check') as mock_method:
                game = Game(dealer=dealer, player=player, deck=deck)

                game.hit()

                mock_method.assert_called_once_with()

    def test_stick_calls_take_card_until_dealer_is_bust(self):
        player = Player()

        dealer_is_bust = [
            False,  # Take card = 9
            False,  # Take card = 18
            False,  # Take card = 27
            True,   # Dealer is bust

            # Extra iteration required here to prevent StopIteration Exception?
            True,
        ]

        with patch.object(Game, '_setup_game'):
            with patch.object(Dealer, 'is_bust', side_effect=dealer_is_bust):
                with patch.object(Game, '_take_card') as mock_method:
                    dealer = Dealer()
                    deck = Deck()
                    game = Game(dealer=dealer, player=player, deck=deck)

                    game.stick()

                    self.assertEqual(mock_method.call_count, 3)
