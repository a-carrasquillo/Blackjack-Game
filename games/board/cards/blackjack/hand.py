'''
The script that contains the Hand Class
'''
# import the card class
from ..card import Card

class Hand:
    '''Class that simulates the hand of a player

    Attributes:
        cards -- list of cards
        total_value -- integer value indicating the total points in the hand
        ace -- flag indicating if there is an ace in the hand
    '''

    def __init__(self):
        '''
        Hand Class Constructor
        Creates an empty hand
        '''

        # list of cards
        self.cards = []

        # total points
        self.total_value = 0

        # ace flag set to false
        self.ace = False

    def add_card(self, card):
        '''
        Method that helps us add a car to the hand.
        The card argument needs to be a Card Object
        '''
        # add the card to the list
        self.cards.append(card)

        # verify if the card is an ace
        if card.rank != 'Ace':
            # add the card value to the total value
            self.total_value += card.value
        else: # is an ace

            # self adjust if using the Ace as an 11 get over 21
            if self.total_value+11 > 21:
                # self adjust to 1
                self.total_value += 1
                print("Ace self adjusted to a value of 1\nsince if we use 11 we bust.")
            else:
                # not self adjust, indicate that there is an ace
                self.ace = True
                # add the ace as an 11 (default value)
                self.total_value += card.value

    def check_ace(self):
        '''Returns the ace flag value'''
        return self.ace

    def adjust_ace(self, adjust):
        '''Method that allows the player or dealer
        to change the value of the ace to 1 or let it as 11

        Argument:
            adjust -- boolean value indicating if the player
                      or dealer wants to adjust the ace value to 1
        '''

        if adjust:
            self.total_value -= 10
            print('The value of the Ace has been adjusted to 1.')
        else:
            print('The Ace is going to be used as 11.')
        # since the ace was treated we set the flag to false
        self.ace = False
