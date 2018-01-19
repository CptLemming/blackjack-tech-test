from game.game import Game
from game.players import Player, Dealer
from game.deck import Deck


if __name__ == "__main__":
    # Initialize game state
    player = Player()
    dealer = Dealer()
    deck = Deck()

    game = Game(dealer=dealer, player=player, deck=deck)

    # Perfom an initial check for a winner
    winner = game.check()

    # Define our allowed options
    options = ['hit', 'stick', 'surrender']

    options_text = '\n'.join([
        'Options:',
        '- hit',
        '- stick',
        '- surrender',
    ])

    print('|', '='*32, '|')
    print('| Welcome to Blackjack', ' '*11, '|')
    print('|', '='*32, '|')

    try:
        # Continue the game until either the player or dealer has won
        while not game.is_game_over():
            print(game.show_game_state())
            print('')
            print(options_text)

            # Request user input
            response = input('Please enter an option: ')

            if response in options:
                winner = getattr(game, response)()
            else:
                print('*'*32)
                print('Sorry, that wasn\'t a valid option')
                print('*'*32)
    except KeyboardInterrupt:
        print('')
        print('Come back soon!')
    else:
        print('')
        print('Thanks for playing!', winner)
        print(game.show_game_state())
