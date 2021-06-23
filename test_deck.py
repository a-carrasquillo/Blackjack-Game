'''
Script to perform unit test on deck.py
'''
# imports
import io
import unittest
from unittest.mock import patch

# import any of the files that we want to verify
from games.board.cards.deck import Deck

class TestDeck(unittest.TestCase):
    '''
    Class used to test the Deck Class script
    '''

    def setUp(self):
        '''Method that runs at the beginning of each test'''
        # create a list of suits to test on
        suits_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

        # create a list of ranks to test on
        ranks_list = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                     'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

        #create a dictionary of values to test on
        values_dictionary = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
                            'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
                            'Queen':10, 'King':10, 'Ace':11}

        # create the deck
        self.deck = Deck(suits_list, ranks_list, values_dictionary)

    def tearDown(self):
        '''Method that runs at the end of each test'''
        # eliminate the reference to the object
        del self.deck

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''

        # test the deck length
        self.assertEqual(len(self.deck.deck_of_cards), 52)

        # test the first and last card
        self.assert_stdout(self.deck.deck_of_cards[0], "Two of Hearts\n")
        self.assert_stdout(self.deck.deck_of_cards[-1], "Ace of Clubs\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        '''
        Support method that helps mock the print functionality
        and test for equality
        '''
        print(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_diff(self, n, expected_output, mock_stdout):
        '''
        Support method that helps mock the print functionality
        and test for inequality
        '''
        print(n)
        self.assertNotEqual(mock_stdout.getvalue(), expected_output)

    def test_shuffle(self):
        '''
        Tests that the shuffle method is working properly
        '''

        # perform the shuffle
        self.deck.shufflecards()

        #perform the test in the first and last card
        self.assert_stdout_diff(self.deck.deck_of_cards[0], "Two of Hearts\n")
        self.assert_stdout_diff(self.deck.deck_of_cards[-1], "Ace of Clubs\n")

    def test_take_card(self):
        '''
        Tests that the take_card method is working properly
        '''

        # take one card
        card1 = self.deck.take_card()
        self.assertEqual(card1.suit, 'Clubs')
        self.assertEqual(card1.rank, 'Ace')
        self.assertEqual(card1.value, 11)
        self.assertEqual(len(self.deck.deck_of_cards), 51)

    def test_take_multiple_cards(self):
        '''
        Tests that we are able to take several cards
        by calling take_card multiple times
        '''

        # take a first card
        card1 = self.deck.take_card()
        self.assertEqual(card1.suit, 'Clubs')
        self.assertEqual(card1.rank, 'Ace')
        self.assertEqual(card1.value, 11)
        self.assertEqual(len(self.deck.deck_of_cards), 51)

        # take a second card
        card2 = self.deck.take_card()
        self.assertEqual(card2.suit, 'Clubs')
        self.assertEqual(card2.rank, 'King')
        self.assertEqual(card2.value, 10)
        self.assertEqual(len(self.deck.deck_of_cards), 50)

if __name__ == '__main__':
    unittest.main()
