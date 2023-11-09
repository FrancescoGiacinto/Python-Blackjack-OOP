from card import Card
from typing import List

class Hand:
    """
    Represents a hand of cards in Blackjack.
    
    A hand can have multiple cards and provides functionalities to check for game-specific conditions 
    like blackjack or busted. It also allows calculating the total value of the cards in the hand 
    with special considerations for the card 'Ace', which can have a value of 1 or 11.

    Attributes:
        cards (list[Card]): List of cards currently in the hand.
    """
    def __init__(self)-> None:
        """
        Initialize an empty hand.
        """
        self.cards = []
        self.is_soft = False

    def add_card(self, card)-> List:
        """
        Add a card to the hand.

        Args:
            card (Card): The card to add.
        """

        hand_card = self.cards.append(card)

        if card.get_number() == "Ace" and self.total_sum() <= 11:
            self.is_soft = True
        elif self.is_soft and self.total_sum() > 21:
            self.is_soft = False
        
        return hand_card
        

    def is_busted(self)-> bool:
        """
        Check if the hand's total value exceeds 21.
        
        Returns:
            bool: True if busted, False otherwise.
        """
        return self.total_sum() > 21

    def get_first_card(self)-> Card:
        """
        Get the first card in the hand.

        Returns:
            Card: The first card in the hand.
        """
        return self.cards[0]

    def is_blackjack(self) -> bool:
        """
        Check if the hand is a blackjack (two cards totaling 21).
        
        Returns:
            bool: True if blackjack, False otherwise.
        """
        return len(self.cards) == 2 and self.total_sum() == 21
    
    def total_sum(self) -> int:
        """
        Calculate the total value of the hand, considering the best value for any Aces.

        Returns:
            int: The total value of the hand.
        """
        total = sum(card.get_value(False) for card in self.cards)  # Assume all Aces are 1 initially
        aces_count = sum(1 for card in self.cards if card.get_number() == "Ace")

        # Add 10 for each Ace until total is less than or equal to 21
        while aces_count > 0 and total <= 11:
            total += 10
            aces_count -= 1
            if self.is_soft:
                self.is_soft = False

        return total



    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.cards])
