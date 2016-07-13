class Card:
    "Class for a playing card"

    #Initializes a card
    def __init__(self, value, suit):
        """
        Card initializer.

        Args:
            value:  Numeric value of the card.
            suit:   Suit of the card.
        """
        self.value = value
        self.suit = suit

    #Get number value of the card
    def getValue(self):
        """
        Get number value of the card.

        Returns:
            Value of the card.
        """
        return self.value

    #Get suit of the card
    def getSuit(self):
        """
        Get suit of the card.

        Returns:
            Suit of the card.
        """
        return self.suit

    #Print value and suit of the card
    def printCardInfo(self):
        """
        Print value and suit of the card
        """
        print("Value: ", self.value)
        print("Suit: ", self.suit)
        print()
