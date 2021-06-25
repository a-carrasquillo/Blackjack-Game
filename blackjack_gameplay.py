'''
The main script that contains the game play/game logic of the blackjack
'''
# imports
#needed to clear the screen
from os import system, name

from games.board.cards.deck import Deck
from games.board.cards.blackjack.dealer import Dealer
from games.board.cards.blackjack.player import Player

def clear_screen():
    '''Function to clear the screen'''
    #for windows OS
    if name == 'nt':
        _ = system('cls')
    #for mac and Linux
    else:
        _ = system('clear')

def player_initial_setup():
    '''
    Function that help us collect the player information and creates a player object
    Returns:
        Player object
    '''
    # ask for the name
    playername = input('Enter your name: ')
    # ask for the initial money amount
    while True:
        try:
            initial_money = int(input('Enter your initial money amount: $'))
            break
        except TypeError:
            print('Please enter a valid integer value.\n')
    # returns the new player object
    return Player(playername,initial_money)

def setup():
    '''
    Function that helps us set up the initial conditions to start the game.
    Here we initialize the players, create and shuffle the deck and create an
    instance of the dealer.

    Returns:
        A tuple containing the players as a dictionary,
        the deck of cards and the dealer instance.
        (players,deck,dealer)
    '''
    # NOTE: more players can be added, but game logic
    # needs adjustment mainly in the driver
    players = {}
    # player initial setup
    players['player1'] = player_initial_setup()

    # create a list of suits
    suits_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    # create a list of ranks
    ranks_list = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                  'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    #create a dictionary of values to test on
    values_dictionary = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
                         'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
                         'Queen':10, 'King':10, 'Ace':11}
    # create the deck
    deck = Deck(suits_list, ranks_list, values_dictionary)
    # shuffle the deck
    deck.shufflecards()

    # create the dealer
    dealer = Dealer()

    return (players, deck, dealer)

def player_options(player, deck, dealer):
    '''
    Function that helps us show the options to the player, collect the answer
    and perform the required operations.
    Arguments:
        player -- player object
        deck -- deck object
        dealer -- dealer object
    '''

    answer = 'h'
    while (answer == 'h' or answer == 'hit') and player.hand.total_value < 20:
        # give the player the options to hit or stay
        while answer.lower() not in ['h','s','hit','stay']:
            answer = input('Please choose if you want to hit or stay: ')
        # evaluate the option chosen
        if answer.lower() == 'hit' or answer.lower() == 'h':
        	# add a card
            player.hand.add_card(deck.take_card())
            # clear screen
            clear_screen()
            # print dealer
            print(dealer)
            # print player
            print(player)
            # check for the ace
            if player.hand.check_ace():
                print('You got an ace!')
                change_ace = 'n'
                # ask if the player wants to modify the ace value
                while change_ace.lower() not in ['y','n','yes','no']:
                    change_ace = input('Do you want to change the ace value to 1?\n')
                # evaluate the answer
                if change_ace.lower() == 'y' or change_ace.lower() == 'yes':
                    player.hand.adjust_ace(True)
                else:
                	player.hand.adjust_ace(False)

def evaluate_player(player, dealer):
	'''
	Function that helps us determine if a player
	win, lose, or draw.
	Arguments:
	    player -- player object
	    dealer -- dealer object
	'''
    # verify the player total points
    if player.hand.total_value <= 21:
    	# compare dealer points with the player
    	player_points = player.hand.total_value
    	dealer_points = dealer.hand.total_value
        if player_points > dealer_points and player_points != 21:
            player.receive_money(player.bet*2)
        elif player_points > dealer_points and player_points == 21:
            player.receive_money(player.bet*2.5)
        elif player_points == dealer_points: # no win nor lose
            player.receive_money(player.bet)
        else:
        	# loose the bet
        	print('You lose')
    else: # player is over 21 points
        print(f'{player.name} has BUSTS!')

    # clear bet and hand for next round
    player.clear_bet()
    player.clear_hand()

# driver
if __name__ == '__main__':
    # setup the game
    players, deck, dealer = setup()

    # clear the screen
    clear_screen()

    # iterate the below statements (until we don't have enough cards, about 8 cards)

        # verify if player have money, money == 0, end game
            # player places a bet
            # give player first card
            # give dealer first card
            # give player second card
            # give dealer second card
            # print the dealer
            # print the player
            # check for ace for both the dealer and the player

    
            # give the player the options to hit or stay
            player_options(players['player1'], deck, dealer)

            # after player/s turn, flip dealer second card and print

            # check the total points of the dealer, if dealer is <= 16
            # take another card and print, if dealer >= 17 stay with the hand

            # evaluate player total points
            evaluate_player(players['player1'], dealer)

            # clear dealer hand
            dealer = Dealer()
            # clear the screen before the next round
            clear_screen()
