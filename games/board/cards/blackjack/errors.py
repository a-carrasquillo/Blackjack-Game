'''
Script that contains user-defined errors
'''

class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

class NotEnoughCardsToPrint(Error):
    ''' Exception raised when there are not enough cards in a hand to be printed

    Attribute:
        message -- explanation of the error
    '''

    def __init__(self, message):
        '''Constructor'''
        self.message = message

class NotEnoughFunds(Error):
    ''' Exception raised when there are not enough founds to retrieve money

    Attribute:
        message -- explanation of the error
    '''

    def __init__(self, message):
        '''Constructor'''
        self.message = message
