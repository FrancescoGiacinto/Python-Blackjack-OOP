from card_player import Card_player

class Dealer(Card_player):
    """
    Represents a dealer in a card game, which extends from the Card_player class.
    
    The dealer has the additional ability to draw a card from a deck.
    """
    def draw_card(self, deck)-> str:
        """
        Draws a card from the provided deck.

        Args:
            deck (Deck): The deck from which a card will be drawn.

        Returns:
            Card: The card drawn from the deck.
        """
        card = deck.take_card()
        return card