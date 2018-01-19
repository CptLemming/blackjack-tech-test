class Player:

    def __init__(self, bet=0):
        self.cards = []
        self.bet = 0

    def __repr__(self):
        return f'<{self.__class__.__name__}:{self.get_winner_text()}>'

    def take_card(self, card):
        self.cards.append(card)

    def get_value(self):
        """
        Return sum of cards in hand
        """
        value = 0
        ace_cards = []

        for card in self.cards:
            if hasattr(card, 'is_ace_card') and card.is_ace_card:
                ace_cards.append(card)
            else:
                value += card.get_value()

        # Add ace cards after we've added up the 'others'
        # Prevents preemptive use as high card
        for ace_card in ace_cards:
            if value + ace_card.get_value(as_high=True) > 21:
                value += ace_card.get_value(as_high=False)
            else:
                value += ace_card.get_value(as_high=True)

        return value

    def is_bust(self):
        """
        Determine if the hand has gone bust
        """
        return self.get_value() > 21

    def has_blackjack(self):
        """
        Determine if the hand is Blackjack!
        """
        return self.get_value() == 21

    @staticmethod
    def get_winner_text():
        return 'You won the game!'


class Dealer(Player):

    def has_reached_limit(self):
        return self.get_value() > 16

    @staticmethod
    def get_winner_text():
        return 'You lost the game!'
