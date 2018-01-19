import random

from .cards import AceCard, Card, FaceCard


class Deck:
    ace_card_class = AceCard
    card_class = Card
    face_card_class = FaceCard

    def __init__(self):
        self.cards = self._create_deck()
        self.dealt = []

    def _create_deck(self):
        suits = ['heart', 'spade', 'diamond', 'club']
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        deck = []

        for suit in suits:
            deck.append(self._create_ace_card(suit))

            for card in cards:
                deck.append(self._create_card(card, suit))

            deck.append(self._create_face_card('Jack', suit))
            deck.append(self._create_face_card('Queen', suit))
            deck.append(self._create_face_card('King', suit))

        return deck

    def _create_ace_card(self, suit):
        return self.ace_card_class('Ace', suit)

    def _create_card(self, card, suit):
        return self.card_class(str(card), suit, card)

    def _create_face_card(self, card, suit):
        return self.ace_card_class(card, suit)

    def shuffle(self):
        """
        Shuffle the deck
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deal a card from the deck, add the card to the dealt pile
        """
        card_index = random.randint(0, len(self.cards) - 1)

        card = self.cards[card_index]

        self.cards = self.cards[0:card_index] + self.cards[card_index+1:]
        self.dealt.append(card)

        return card
