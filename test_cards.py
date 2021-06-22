'''
Script to perform unit test on card.py
'''
# imports
import io
import unittest
from unittest.mock import patch

# import any of the files that we want to verify
from games.board.cards.card import Card

class TestCard(unittest.TestCase):
    '''
    Class used to test the Card Class script
    '''

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''
        # initialize two different cards
        card1 = Card("Hearts","Two",2)
        card2 = Card("Clubs","Jack",10)
        # check for correct initialization for first card
        self.assertEqual(card1.suit,'Hearts')
        self.assertEqual(card1.rank,'Two')
        self.assertEqual(card1.value,2)
        # check for correct initialization for second card
        self.assertEqual(card2.suit,'Clubs')
        self.assertEqual(card2.rank,'Jack')
        self.assertEqual(card2.value,10)

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        '''
        Support method that helps the test_print method
        to mock the print functionality
        '''
        print(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print(self):
        '''
        Tests that the print of a card class is correct
        '''
        # initialize two different cards
        card1 = Card("Hearts","Two",2)
        card2 = Card("Clubs","Jack",10)
        # verify first card
        self.assert_stdout(card1,"Two of Hearts\n")
        # verify second card
        self.assert_stdout(card2,"Jack of Clubs\n")

if __name__ == '__main__':
    unittest.main()
