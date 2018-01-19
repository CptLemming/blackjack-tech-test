class Card:

    def __init__(self, name, suit, value=None):
        self.name = name
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'<{self.__class__.__name__}:{self.name} of {self.suit}s>'

    def get_value(self):
        return self.value


class FaceCard(Card):
    is_face_card = True

    def get_value(self):
        return 10


class AceCard(Card):
    is_ace_card = True

    def get_value(self, as_high=False):
        """
        Return 1 or 11
        """
        if as_high:
            return 11
        return 1
