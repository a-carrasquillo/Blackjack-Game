'''
Script to perform unit test on dealer.py
'''
# imports
import io
import unittest
from unittest.mock import patch

from games.board.cards.card import Card
from games.board.cards.blackjack.errors import NotEnoughCardsToPrint

# import any of the files that we want to verify
from games.board.cards.blackjack.dealer import Dealer

class TestDealer(unittest.TestCase):
    '''
    Class used to test the Dealer Class script
    '''

    def setUp(self):
        '''Method that runs at the beginning of each test'''
        # instantiate a new object
        self.dealer = Dealer()

    def tearDown(self):
        '''Method that runs at the end of each test'''
        # eliminate the reference to the object
        del self.dealer

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''

        # test length of the dealer's hand
        self.assertEqual(len(self.dealer.hand.cards),0)
        # test that the flipped flag is False
        self.assertFalse(self.dealer.flipped)

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        '''
        Support method that helps mock the print functionality
        and test for equality
        '''
        print(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_flip_card(self):
        '''
        Tests that we can enable the second card
        '''

        # flip the card
        self.dealer.flip_card()
        # test that the card was flipped
        self.assertTrue(self.dealer.flipped)

    def test_print_two_cards_second_not_flipped(self):
        '''
        Tests that we can print two cards, and the second one is facing down
        '''

        # create two cards
        card1 = Card("Hearts","Two",2)
        card2 = Card("Clubs","Jack",10)
        # add the two cards to the hand
        self.dealer.hand.add_card(card1)
        self.dealer.hand.add_card(card2)
        # test the print
        self.assert_stdout(self.dealer,"Two of Hearts\tFACING DOWN\n")

    def test_print_two_cards_second_flipped(self):
        '''
        Tests that we can print two cards, and the second one is facing up
        '''

        # create two cards
        card1 = Card("Hearts","Two",2)
        card2 = Card("Clubs","Jack",10)
        # add the two cards to the hand
        self.dealer.hand.add_card(card1)
        self.dealer.hand.add_card(card2)
        # flip the second card
        self.dealer.flip_card()
        # test the print
        self.assert_stdout(self.dealer,"Two of Hearts\tJack of Clubs\t\n")

    def test_print_one_card(self):
        '''
        Tests that an exception is raised since there are not
        enough cards to be printed
        '''

        # create one card
        card = Card("Hearts","Two",2)
        # add the card to the hand
        self.dealer.hand.add_card(card)
        # test the exception
        with self.assertRaises(NotEnoughCardsToPrint):
            # try to print, so the exception is thrown
            self.assert_stdout(self.dealer,"")

if __name__ == '__main__':
    unittest.main()
