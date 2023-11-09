from hand import Hand

class Card_player:
    """
    Represents a card player with a hand and a name.

    Attributes:
        hand (Hand): Represents the player's hand of cards.
        name (str): The name of the player.

    Example:
        >>> player = Card_player("John")
        >>> print(player.get_name())
        John
    """
    def __init__(self, name="Tommy"):
        """
        Initializes a new Card_player instance with a given name and an empty hand.

        Args:
            name (str): The name of the player.
        """
        self.hand = Hand()
        self.name = name

    def get_name(self)-> str:
        """
        Retrieves the name of the player.

        Returns:
            str: The name of the player.
        """
        return self.name
    
    def set_name(self,name) -> str:
        self.name = name
        return name

    def get_hand(self)-> Hand:
        """
        Retrieves the player's current hand.

        Returns:
            Hand: The player's current hand of cards.
        """
        return self.hand

    def set_hand(self, hand)->Hand:
        """
        Sets the player's current hand to the given hand.

        Args:
            hand (Hand): The new hand of cards for the player.
        """
        self.hand = hand
        return hand



