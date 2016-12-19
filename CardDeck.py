from random import shuffle
from Card import Card

class CardDeck:
    "Class for a deck of playing cards"

    SuitValues = ["Spades", "Hearts", "Diamonds", "Clubs"]

    #Initializes card deck
    def __init__(self):
        """
        CardDeck initializer.
        """
        self.deck = []
        self.fillDeck()
        self.shuffleDeck()
        
    #Fill deck with cards
    def fillDeck(self):
        """
        Fill the deck with cards.
        """
        #Ace - King (1- 13)
        for i in range(1, 14):
            #Suits (Spades, Hearts, Diamonds, Clubs)
            for j in range(0, 4):
                tmpCard = Card(i, CardDeck.SuitValues[j])
                self.deck.append(tmpCard)

    #Shuffle the deck of cards randomly
    def shuffleDeck(self):
        """
        Shuffle the deck randomly.
        """
        shuffle(self.deck)

    #Get the amount of cards still in the deck
    def getCardCount(self):
        """
        Get the amount of cards still in the deck.

        Returns:
            Amount of cards in the deck.
        """
        return len(self.deck)

    #Draw a card from the deck
    def drawCard(self):
        """
        Draw a card from the deck.
        
        Returns:
            Card drawn from the deck.
        """
        return self.deck.pop()

    #Print the contents of the cards still in the deck
    def printDeck(self):
        """
        Print the contents of the cards still in the deck.
        """
        for i in range(0, self.getCardCount()):
            self.deck[i].printCardInfo()
    
#Testing class features
print("starting\n")
testDeck = CardDeck()
print("deck obj created")
print("card amount in deck: ", testDeck.getCardCount())

print("\nprinting deck: ")
testDeck.printDeck()
print("printed deck\n")

card1 = testDeck.drawCard()
print("drew card")
card1.printCardInfo()
card2 = testDeck.drawCard()
print("drew card")
card2.printCardInfo()
#testDeck.printDeck()
print("card amount still in deck: ", testDeck.getCardCount())
