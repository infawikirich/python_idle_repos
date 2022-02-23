"""
Script file: wizcoin.py


Purpose: This program learns about the
OOP (Object oriented programming)

Date: 08/22/21

Author: Mr. Asiamah

"""


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # NOTE: ___init__() methods NEVER have a return statement

    def value(self):
        """The value (in knuts) in all the coins in this WizCoin object."""
        return(self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)


    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103 ) + (self.sickles * 11.34 ) + (self.knuts * 5.0)
        
