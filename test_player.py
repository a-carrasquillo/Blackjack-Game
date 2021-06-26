'''
Script to perform unit test on player.py
'''
# imports
import io
import unittest
from unittest.mock import patch

from games.board.cards.card import Card
from games.board.cards.blackjack.errors import NotEnoughCardsToPrint
from games.board.cards.blackjack.errors import NotEnoughFunds

# import any of the files that we want to verify
from games.board.cards.blackjack.player import Player

class TestPlayer(unittest.TestCase):
    '''
    Class used to test the Player Class script
    '''

    def setUp(self):
        '''Method that runs at the beginning of each test'''
        # instantiate a new object
        self.player = Player('Player 1',150)

    def tearDown(self):
        '''Method that runs at the end of each test'''
        # eliminate the reference to the object
        del self.player

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''

        # test player name
        self.assertEqual(self.player.name,'Player 1')
        # test player total money
        self.assertEqual(self.player.total_money, 150)
        # test empty hand
        self.assertEqual(len(self.player.hand.cards),0)
        # test empty bet
        self.assertEqual(self.player.bet,0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        '''
        Support method that helps mock the print functionality
        and test for equality
        '''
        print(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_two_cards(self):
        '''
        Tests that we can print the cards
        '''

        # create first card
        card1 = Card("Hearts","Two",2)
        # create second card
        card2 = Card("Clubs","Jack",10)
        # add cards to the hand
        self.player.hand.add_card(card1)
        self.player.hand.add_card(card2)
        # set the bet directly without using the defined function for it
        self.player.bet = 10
        # print
        self.assert_stdout(self.player,"Player Name: Player 1\n"
        	                          +"Total Money: $150\n"
        	                          +"Actual Bet: $10\nTwo of Hearts\t"
        	                          +"Jack of Clubs\t\n")

    def test_try_print_one_card(self):
        '''
        Tests that the exception is raised since only one card is in the hand
        '''

        # create first card
        card = Card("Hearts","Two",2)
        # add card to the hand
        self.player.hand.add_card(card)
        # test the exception
        with self.assertRaises(NotEnoughCardsToPrint):
            # try to print, so the exception is thrown
            self.assert_stdout(self.player,"")

    def test_place_bet_correct_funds(self):
        '''
        Tests that we can perform a bet
        '''

        # place the correct bet
        self.player.place_bet(50)
        # verify the bet
        self.assertEqual(self.player.bet,50)
        # verify the total money
        self.assertEqual(self.player.total_money,100)

    def test_place_bet_incorrect_funds(self):
        '''
        Tests that an exception is raised since we do not possess enough funds
        '''

        with self.assertRaises(NotEnoughFunds):
            self.player.place_bet(151)

    def test_clear_bet(self):
        '''
        Tests that we can delete the current bet amount
        '''

        # set the bet value directly
        self.player.bet = 50
        # verify the change
        self.assertEqual(self.player.bet,50)
        # clear the bet
        self.player.clear_bet()
        # verify the change
        self.assertEqual(self.player.bet,0)

    def test_receive_money(self):
        '''
        Tests that we can add money to the total amount
        '''

        # verify the total money before method call
        self.assertEqual(self.player.total_money,150)
        # receive money
        self.player.receive_money(50)
        # verify the total money after receiving money
        self.assertEqual(self.player.total_money,200)

    def test_clear_hand(self):
        '''
        Tests that we can delete the hand and create a new one
        '''

        # create two cards
        card1 = Card("Hearts","Two",2)
        card2 = Card("Clubs","Jack",10)
        # add cards to the hand
        self.player.hand.add_card(card1)
        self.player.hand.add_card(card2)
        # verify that they were added
        self.assertEqual(len(self.player.hand.cards),2)
        # clear the hand
        self.player.clear_hand()
        # verify that the cards where delete it
        self.assertEqual(len(self.player.hand.cards),0)

    def test_is_active(self):
        '''
        Tests that when the player runs out of money, it turns into an inactive player
        '''
        self.assertTrue(self.player.is_active())
        self.player.total_money = 0
        self.assertFalse(self.player.is_active())

if __name__ == '__main__':
    unittest.main()
