'''
The script that contains the Card Class
'''
class Card:
    '''
    Class that simulates a general card
    that contains suit, rank, and
    an associated value to the rank
    '''

    def __init__(self, suit, rank, value):
        '''
        Card Class Constructor

        Arguments:
        suit: String representation of the suit
        rank: String representation of the rank
        value: Integer representation of the rank
        '''

        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        '''
        Method that enable us to print the Card Class
        '''

        return f"{self.rank} of {self.suit}"
