'''
Script to perform unit test on hand.py
'''
# imports
import unittest

from games.board.cards.card import Card

# import any of the files that we want to verify
from games.board.cards.blackjack.hand import Hand

class TestHand(unittest.TestCase):
    '''
    Class used to test the Hand Class script
    '''

    def test_initialization(self):
        '''
        Tests that the initialization of an object is correct
        '''

        # instantiate a new object
        myhand = Hand()
        # test the hand cards length
        self.assertEqual(len(myhand.cards), 0)
        # test the total points
        self.assertEqual(myhand.total_value, 0)
        # test the ace flag
        self.assertFalse(myhand.ace)

    def test_add_card_single_not_ace(self):
        '''
        Tests that we can add a single card and that card is not an ace
        '''

        # instantiate a new object
        myhand = Hand()
        # create a card
        card = Card("Hearts","Two",2)
        # add the card to the hand
        myhand.add_card(card)
        # verify the cards list length is one since we add one card
        self.assertEqual(len(myhand.cards), 1)
        # verify the total_value amount is two since a Two of Hearts was added
        self.assertEqual(myhand.total_value, 2)
        # verify the ace flag is still false, since an ace was not added
        self.assertFalse(myhand.ace)

    def test_add_card_single_ace(self):
        '''
        Tests that we can add a single card and that card is an ace
        '''

        # instantiate a new object
        myhand = Hand()
        # create a card
        card = Card("Diamonds","Ace",11)
        # add the card to the hand
        myhand.add_card(card)
        # verify the cards list length is one since we add one card
        self.assertEqual(len(myhand.cards), 1)
        # verify the total_value amount is eleven since an Ace of Diamonds was added
        self.assertEqual(myhand.total_value, 11)
        # verify the ace flag is true, since an ace was added
        self.assertTrue(myhand.ace)

    def test_add_card_multiple_not_ace(self):
        '''
        Tests that we can add multiple cards and none of them is an ace
        '''

        # instantiate a new object
        myhand = Hand()
        # create a first card
        card = Card("Diamonds","Jack",10)
        # add the card to the hand
        myhand.add_card(card)
        #create a second card
        card = Card("Spades","Ten", 10)
        # add the second card to the hand
        myhand.add_card(card)
        # verify the cards list length is two since we add two cards
        self.assertEqual(len(myhand.cards), 2)
        # verify the total_value amount is twenty since a Jack and a Ten was added
        self.assertEqual(myhand.total_value, 20)
        # verify the ace flag is false, since an ace was not added
        self.assertFalse(myhand.ace)

    def test_add_card_multiple_ace_not_pass_21(self):
        '''
        Tests that we can add multiple cards and one of them
        is an ace, and the sum of the values does not pass 21
        '''

        # instantiate a new object
        myhand = Hand()
        # create a first card
        card = Card("Diamonds","Ace",11)
        # add the card to the hand
        myhand.add_card(card)
        #create a second card
        card = Card("Spades","Ten", 10)
        # add the second card to the hand
        myhand.add_card(card)
        # verify the cards list length is two since we add two cards
        self.assertEqual(len(myhand.cards), 2)
        # verify the total_value amount is twenty one since an Ace and a Ten was added
        self.assertEqual(myhand.total_value, 21)
        # verify the ace flag is true, since an ace was added
        self.assertTrue(myhand.ace)

    def test_add_card_multiple_ace_pass_21(self):
        '''
        Tests that we can add multiple cards and one of them
        is an ace, and the sum of the values pass 21, hence
        the self adjustment is performed
        '''

        # instantiate a new object
        myhand = Hand()
        # create a first card
        card = Card("Diamonds","Jack",10)
        # add the card to the hand
        myhand.add_card(card)
        #create a second card
        card = Card("Spades","Ten", 10)
        # add the second card to the hand
        myhand.add_card(card)
        #create a third card
        card = Card("Spades","Ace", 11)
        # add the third card to the hand
        myhand.add_card(card)
        # verify the cards list length is three since we add three cards
        self.assertEqual(len(myhand.cards), 3)
        # verify the total_value amount is twenty one since the self adjustment was performed
        self.assertEqual(myhand.total_value, 21)
        # verify the ace flag is false, since an ace was added but it was self adjusted
        self.assertFalse(myhand.ace)

    def test_check_ace(self):
        '''
        Tests that the check_ace method returns the correct value
        '''

        # instantiate a new object
        myhand = Hand()
        # verify the initial value of the flag
        self.assertFalse(myhand.ace)
        #create an ace card
        card = Card("Spades","Ace", 11)
        # add the card to the hand
        myhand.add_card(card)
        # verify the ace flag is true, since an ace was added
        self.assertTrue(myhand.ace)

    def test_adjust_ace_as1(self):
        '''
        Tests that we can adjust the ace value to 1
        '''

        # instantiate a new object
        myhand = Hand()
        #create an ace card
        card = Card("Spades","Ace", 11)
        # add the card to the hand
        myhand.add_card(card)
        # verify that the flag is true
        self.assertTrue(myhand.ace)
        # adjust the value
        myhand.adjust_ace(True)
        # verify the adjustment
        self.assertEqual(myhand.total_value, 1)
        # verify that the flag was set to false
        self.assertFalse(myhand.ace)

    def test_adjust_ace_as11(self):
        '''
        Tests that we can let the ace as an 11
        '''

        # instantiate a new object
        myhand = Hand()
        #create an ace card
        card = Card("Spades","Ace", 11)
        # add the card to the hand
        myhand.add_card(card)
        # verify that the flag is true
        self.assertTrue(myhand.ace)
        # do not adjust the value
        myhand.adjust_ace(False)
        # verify that the adjustment was not performed
        self.assertEqual(myhand.total_value, 11)
        # verify that the flag was set to false
        self.assertFalse(myhand.ace)

if __name__ == '__main__':
    unittest.main()
