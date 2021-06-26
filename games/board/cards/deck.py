'''
The script that contains the Deck Class
'''
# import the shuffle function
from random import shuffle

# import the Card class
from .card import Card

class Deck:
    '''Class that simulates a general deck of cards

    Attribute:
        deck_of_cards -- list containing a group of cards
    '''

    def __init__(self, suits_list, ranks_list, values_dictionary):
        '''
        Deck Class Constructor

        The constructor generates an ordered deck of cards

        Arguments:
        suits_list: list of suits that the cards will have
        ranks_list: list of ranks that the cards will have
        values_dictionary: dictionary containing the
        representation of the ranks in an integer value
        '''

        # create an empty deck
        self.deck_of_cards = list()

        # iterate over lists to generate the deck
        for suit in suits_list:
            for rank in ranks_list:
                # create the card
                new_card = Card(suit, rank, values_dictionary[rank])
                #add the card to the deck
                self.deck_of_cards.append(new_card)

    def __len__(self):
        '''
        Give the length of the deck to the len()
        function when we use it in the object itself
        '''
        return len(self.deck_of_cards)

    def shufflecards(self):
        '''
        Method that shuffles the deck of cards
        '''

        shuffle(self.deck_of_cards)

    def take_card(self):
        '''
        Method that deals one card from the deck
        '''

        return self.deck_of_cards.pop()
