'''
The script that contains the Player Class
'''
# import the hand class
from .hand import Hand
# import the error classes
from .errors import NotEnoughCardsToPrint

class Player:
    '''Class that simulates a player of blackjack

    Attributes:
        name -- player name
        total_money -- total amount of money that the player has
        hand -- cards currently in the player's hand
        bet -- current bet
    '''

    def __init__(self, name, total_money):
        '''Constructor
        Defines the player name, initial money,
        an empty hand and an empty bet
        '''

        self.name = name
        self.total_money = total_money
        self.hand = Hand()
        self.bet = 0

    def __str__(self):
        '''
        Method that will be called when the
        print function is called on this type of object
        '''

        string = f'Player Name: {self.name}\nTotal Money: {self.total_money}\n'
        string += f'Actual Bet: {self.bet}\n'
        if len(self.hand.cards) > 0:
            for card in self.hand.cards:
                string += f'{card.rank} of {card.suit}\t'
            return string
        else:
            raise NotEnoughCardsToPrint('The player does not possess enough'
        	    + f'cards to be printed. Currently he/she possess {len(self.hand.cards)} cards')

    def place_bet(self, bet):
        '''Set the current bet for the round
        Argument:
            bet -- bet amount, should be an integer
        '''

        self.bet = bet
        #substract the bet from the total money
        self.total_money -= bet

    def clear_bet(self):
        '''Clears the current bet'''

        self.bet = 0

    def receive_money(self, amount):
        '''Method to receive the money from the table

        Argument:
            amount -- amount to be added
        '''

        self.total_money += amount

    def clear_hand(self):
        '''Clears the actual player's hand'''

        #deletes the reference to the previous hand so the garbage collector can delete it
        del self.hand
        # creates a new hand for the next round
        self.hand = Hand()
