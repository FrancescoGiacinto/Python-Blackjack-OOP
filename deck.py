from card import Card
from typing import List
import random

class Deck:
    """
    Represents a standard deck of playing cards.
    
    A deck consists of multiple cards and provides functionalities for shuffling, drawing, and 
    replenishing the cards. In the context of Blackjack, the deck is used to deal cards to both 
    the player and the dealer.

    Attributes:
        cards (list[Card]): List of cards currently in the deck.
    """
    def __init__(self)->None:
        """
        Initialize a new deck of 52 cards and shuffle them.
        """
        self.cards = []
    
    def generate_deck(self) -> List:
        """
        Generate a new deck of 52 cards.
        """
        self.cards = [Card(i) for i in range(52)]
        return self.cards

        

    def shuffle_deck(self)->None:
        """
        esta es la razon por la que tengo que importar radom
        Shuffle the deck of cards in place.
        """
        random.shuffle(self.cards)

    def take_card(self)->None:
        """
        Draw and return the top card from the deck.
        
        Returns:
            Card: The top card from the deck.
        """
        return self.cards.pop()
