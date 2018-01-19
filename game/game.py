class Game:

    def __init__(self, dealer, player, deck):
        self.dealer = dealer
        self.player = player
        self.deck = deck
        self.is_over = False
        self.is_player_done = False

        self._setup_game()

    def _setup_game(self):
        """
        Initialise game state and begin playing
        """
        self._shuffle_deck()
        self._setup_dealer()
        self._setup_player()

    def _shuffle_deck(self):
        # Ensure the deck is suffled
        self.deck.shuffle()

    def _setup_dealer(self):
        # Dealer gets 1x cards
        self._take_card(self.dealer)

    def _setup_player(self):
        # Player gets 2x cards
        self._take_card(self.player)
        self._take_card(self.player)

    def _take_card(self, player):
        player.take_card(self.deck.deal())

    def is_game_over(self):
        return self.is_over

    def show_game_state(self):
        list_cards = lambda cards: ', '.join([str(card) for card in cards])
        player_cards = list_cards(self.player.cards)
        dealer_cards = list_cards(self.dealer.cards)
        return '\n'.join([
            f'Player: {player_cards} = {self.player.get_value()}',
            f'Dealer: {dealer_cards} = {self.dealer.get_value()}',
        ])

    def check(self):
        # Has the player gone bust?
        if self.player.is_bust():
            self.is_over = True
            return self.dealer
        # Does the player have blackjack?
        elif self.player.has_blackjack():
            self.is_over = True
            return self.player

        # Has the player decided to stick?
        if self.is_player_done:
            # Has the dealer gone bust?
            if self.dealer.is_bust():
                self.is_over = True
                return self.player
            # Has the dealer reached the mimimum value?
            elif self.dealer.has_reached_limit():
                self.is_over = True

                if self.player.get_value() > self.dealer.get_value():
                    return self.player
                else:
                    return self.dealer

    def stick(self):
        self.is_player_done = True

        while not self.dealer.is_bust():
            self._take_card(self.dealer)

        return self.check()

    def hit(self):
        self._take_card(self.player)

        return self.check()

    def surrender(self):
        raise NotImplementedError
