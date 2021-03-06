'''
The script that contains the Player Class
'''
# import the hand class
from .hand import Hand
# import the error classes
from .errors import NotEnoughCardsToPrint
from .errors import NotEnoughFunds

class Player:
    '''Class that simulates a player of blackjack

    Attributes:
        name -- player name
        total_money -- total amount of money that the player has
        hand -- cards currently in the player's hand
        bet -- current bet
        active -- flag used to indicate if the player has money left to play
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
        self.active = True

    def __str__(self):
        '''
        Method that will be called when the
        print function is called on this type of object
        '''

        string = f'Player Name: {self.name}\nTotal Money: ${self.total_money}\n'
        string += f'Actual Bet: ${self.bet}\n'
        if len(self.hand.cards) > 1:
            for card in self.hand.cards:
                string += str(card)+'\t'
            return string
        raise NotEnoughCardsToPrint('The player does not possess enough'
            + f'cards to be printed. Currently he/she possess {len(self.hand.cards)} cards')

    def place_bet(self, bet):
        '''Set the current bet for the round
        Argument:
            bet -- bet amount, should be an integer
        '''

        if self.total_money - bet >= 0:
            self.bet = bet
            #subtract the bet from the total money
            self.total_money -= bet
        else:
            raise NotEnoughFunds('The player does not possess enough founds to perform'
                                + f' the current bet. The current balance is {self.total_money}'
                                + f' and the bet you are trying to place is {bet}')

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

    def is_active(self):
        '''
        Method used to indicate if the player has money left to play
        Returns a boolean value indicating if the player is active.
        '''
        if self.total_money == 0:
            self.active = False
        return self.active
