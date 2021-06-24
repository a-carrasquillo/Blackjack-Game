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

    @classmethod
    def setUpClass(cls):
        '''Method that runs at the beginning of all the tests'''
        # initialize two different cards
        cls.card1 = Card("Hearts","Two",2)
        cls.card2 = Card("Clubs","Jack",10)

    @classmethod
    def tearDownClass(cls):
        '''Method that runs at the end of all the tests'''
        # eliminate the reference to the objects
        del cls.card1
        del cls.card2

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''

        # check for correct initialization for first card
        self.assertEqual(self.card1.suit,'Hearts')
        self.assertEqual(self.card1.rank,'Two')
        self.assertEqual(self.card1.value,2)
        # check for correct initialization for second card
        self.assertEqual(self.card2.suit,'Clubs')
        self.assertEqual(self.card2.rank,'Jack')
        self.assertEqual(self.card2.value,10)

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

        # verify first card
        self.assert_stdout(self.card1,"Two of Hearts\n")
        # verify second card
        self.assert_stdout(self.card2,"Jack of Clubs\n")

if __name__ == '__main__':
    unittest.main()
