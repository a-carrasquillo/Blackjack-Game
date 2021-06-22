'''
The script that contains the Dealer Class
'''
# import the hand class
from .hand import Hand
# import the error classes
from .errors import NotEnoughCardsToPrint

class Dealer:
    '''Class that simulates the card dealer

    Attributes:
        hand -- hand object containing the cards. See the Hand Class.
        flipped -- boolean value to indicate if the second card is flipped.
            flipped values:
                True -- the second card is facing up
                False -- the second card is facing down
    '''

    def __init__(self):
        '''Constructor for the Dealer Class

        It creates an empty hand
        '''
        # creates an empty hand
        self.hand = Hand()
        # set the flag to false so we know taht the second card is upside down
        self.flipped = False

    def __str__(self):
        '''
        Method that will be called when the
        print function is called on this type of object
        '''
        if(not(self.flipped) and len(self.hand.cards)>1):
            return f'{self.hand.cards[0].rank} of {self.hand.cards[0].suit}\tFACING DOWN'
        elif(self.flipped and len(self.hand.cards)>1):
            string = ""
            for card in self.hand.cards:
                string += f'{card.rank} of {card.suit}\t'
            return string
        else:
            raise NotEnoughCardsToPrint('The dealer does not possess enough'
                + f'cards to be printed. Currently he/she possess {len(self.hand.cards)} cards')

    def flip_card(self):
        '''Enables the second card

        Change the flipped flag to True so we can print the second card
        '''
        self.flipped = True
