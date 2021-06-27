'''
The main script that contains the game play/game logic of the blackjack
'''
# imports
#needed to clear the screen
from os import system, name
# import sleep to stop for some time period
from time import sleep

from games.board.cards.deck import Deck
from games.board.cards.blackjack.dealer import Dealer
from games.board.cards.blackjack.player import Player
from games.board.cards.blackjack.errors import NotEnoughFunds

def clear_screen():
    '''Function to clear the screen'''
    # wait 3 sec before clear screen
    sleep(3)
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
    # players dictionary
    players_dict = {}
    # NOTE: more players can be added
    # player initial setup
    players_dict['player1'] = player_initial_setup()

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
    deck_card = Deck(suits_list, ranks_list, values_dictionary)
    # shuffle the deck
    deck_card.shufflecards()

    # create the dealer
    dealer_init = Dealer()

    return (players_dict, deck_card, dealer_init)

def got_an_ace(hand):
    '''
    Function that helps with the process of having an ace.
    Argument:
        hand -- hand object
    '''
    print('You got an ace!')
    change_ace = ''
    # ask if the player/dealer wants to modify the ace value
    while change_ace.lower() not in ['y','n','yes','no']:
        change_ace = input('Do you want to change the ace value to 1?\n')
        # evaluate the answer
        if change_ace.lower() in ['y', 'yes']:
            hand.adjust_ace(True)
        else:
            hand.adjust_ace(False)

def player_options(player, deck_card, dealer_ob):
    '''
    Function that helps us show the options to the player, collect the answer
    and perform the required operations.
    Arguments:
        player -- player object
        deck_card -- deck object
        dealer_ob -- dealer object
    '''

    answer = 'h'
    while answer in ['h', 'hit'] and player.hand.total_value < 20:
        answer = ''
        # give the player the options to hit or stay
        while answer.lower() not in ['h','s','hit','stay']:
            answer = input('Please choose if you want to hit or stay: ')
        # evaluate the option chosen
        if answer.lower() in ['hit', 'h']:
        	# add a card
            player.hand.add_card(deck_card.take_card())
            # clear screen
            clear_screen()
            # print dealer
            print(dealer_ob)
            # print player
            print(player)
            # check for the ace
            if player.hand.check_ace():
                # ask the player what he/she wants to do with the ace
                got_an_ace(player.hand)

def evaluate_player(player, dealer_ob):
    '''
    Function that helps us determine if a player
    win, lose, or draw.
    Arguments:
        player -- player object
        dealer_ob -- dealer object
    '''
    # verify the player total points
    if player.hand.total_value <= 21:
        # compare dealer points with the player
        player_points = player.hand.total_value
        dealer_points = dealer_ob.hand.total_value
        if (dealer_points>21 and player_points==21 and len(player.hand.cards)==2):
            player.receive_money(player.bet*2.5)
            print('You win by Blackjack!')
        elif(player_points==21 and len(player.hand.cards)==2 and
                dealer_points==21 and len(dealer_ob.hand.cards)>2):
            player.receive_money(player.bet*2.5)
            print('You win by Blackjack!')
        elif (player_points>dealer_points or dealer_points>21) and player_points <=21:
            player.receive_money(player.bet*2)
            print('You win!')
        elif player_points==dealer_points and player_points<=21: # no win nor lose
            player.receive_money(player.bet)
            print('You draw')
        else:
        	# loose the bet
            print('You lose')
    else: # player is over 21 points
        print(f'{player.name} has BUSTS!')

    # clear bet and hand for next round
    player.clear_bet()
    # print player
    print(player)
    sleep(1)
    #clear hand
    player.clear_hand()

def bet(player):
    '''
    Allows the player to perform a bet
    Argument:
        player -- player object
    '''

    while True:
        try:
            amount = int(input(f'{player.name} please enter a valid bet amount: $'))
            # try to perform the bet
            try:
                player.place_bet(amount)
                break
            except NotEnoughFunds:
                print(f'Your current bid of ${amount} exceeds your'
                    + f' total money, which is ${player.total_money}.')
        except ValueError:
            print('Please enter an integer value!')

# driver
if __name__ == '__main__':
    clear_screen()
    print('Welcome to Blackjack 21!')
    # setup the game
    players, deck, dealer = setup()

    print('\n')

    # determine the number of players
    number_players = len(players)

    # iterate the below statements (until we don't have enough cards,
    # about 8 cards for one player, or we run out of players)
    while len(deck) > 8*number_players and number_players > 0:

        # iterate over the players
        for player_key in players:
            # verify if the player is active
            if players[player_key].is_active():
                # player place the bet
                bet(players[player_key])
                # give player first card
                players[player_key].hand.add_card(deck.take_card())

        # give dealer first card
        dealer.hand.add_card(deck.take_card())

        # iterate over the players to give the second card
        for player_key in players:
            # verify if the player is active
            if players[player_key].is_active():
                # give player second card
                players[player_key].hand.add_card(deck.take_card())

        # give dealer second card
        dealer.hand.add_card(deck.take_card())

        # print the dealer
        print(dealer)

        # iterate over the players
        for player_key in players:
            # verify if the player is active
            if players[player_key].is_active():
                # print the player
                print(players[player_key])

                # check for ace in player hand
                if players[player_key].hand.check_ace():
                    # ask the player what he/she wants to do with the ace
                    got_an_ace(players[player_key].hand)

                # give the player the options to hit or stay
                player_options(players[player_key], deck, dealer)

        # after player/s turn, flip dealer second card and print
        dealer.flip_card()
        print(dealer)

        # check for ace in dealer hand
        if dealer.hand.check_ace():
            # ask the dealer what he/she wants to do with the ace
            got_an_ace(dealer.hand)
            sleep(2)

        # check the total points of the dealer, if dealer is <= 16
        # take another card and print, if dealer >= 17 stay with the hand
        while dealer.hand.total_value <= 16:
            dealer.hand.add_card(deck.take_card())
            # print dealer hand
            print(dealer)
            # check for ace in dealer hand
            if dealer.hand.check_ace():
                # ask the dealer what he/she wants to do with the ace
                got_an_ace(dealer.hand)

        # clear the screen
        clear_screen()
        # print the dealer hand
        print(dealer)
        # iterate over the players
        for player_key in players:
            # verify if the player is active
            if players[player_key].is_active():
                # print the player
                print(players[player_key])

        # reset the number of players
        number_players = 0
        # iterate over the players
        for player_key in players:
            # verify if the player is active
            if players[player_key].is_active():
                # evaluate player total points
                evaluate_player(players[player_key], dealer)
                # add 1 for each active player
                number_players += 1

        # clear dealer hand
        dealer = Dealer()
        print('\n')

    print('Not enough players or cards to continue to play')
