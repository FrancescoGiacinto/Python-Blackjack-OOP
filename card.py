class Card():
    """A card, belongs to a Deck or a Hand

    Args:
        card_number (int) : Index of a card (0 - 51)

    Example:
        # Generate a full deck of cards:
        deck = []
        for i in range(52):
            deck.append(Card(i))

        # Shuffle the cards (don't forget to include the random module):
        random.shuffle(deck)
    """

    def __init__(self, card_number: int) -> None:
        """Creates a card with folloing attributes

        Attributes:
            + color (str) : The color of the card
            + number (str) : The number of a card (2-10, knight, queen, king, ace)
            + value (int) : The value of a card (2-11)

        Args:
            card_number (int) : Index of a card (0 - 51)
        """
        self.color = self.set_color(card_number)
        self.number = self.set_number(card_number)
        self.value = self.set_value(card_number)

    def set_color(self, card_number: int) -> str:
        """Sets the color of a card

        Args:
            card_number (int) : The index of the card (0-51)

        Returns:
            str : The color of the card
        """
        if card_number < 13:
            return "Hearts"
        elif card_number < 26:
            return "Diamonds"
        elif card_number < 39:
            return "Spades"
        else:
            return "Clubs"

    def get_color(self) -> str:
        """Gets the color of a card

        Returns:
            str : The color of the card
        """
        return self.color

    def set_number(self, card_number: int) -> str:
        """Sets the number of a card

        Args:
            card_number (int) : The index of the card (0-51)

        Returns:
            str : The number of the card
        """
        card_value = card_number % 13

        if card_value < 9:
            return str(card_value + 2)
        elif card_value == 9:
            return "Jack"
        elif card_value == 10:
            return "Queen"
        elif card_value == 11:
            return "King"
        else:
            return "Ace"

    def get_number(self) -> str:
        """Gets the number of a card

        Returns:
            str : The number of the card
        """
        return self.number

    def set_value(self, card_number: int) -> int:
        """Sets the value of a card

        Args:
            card_number (int) : The index of the card (0-51)

        Returns:
            int : The value of the card
        """
        card_value = card_number % 13

        if card_value < 9:
            return card_value + 2
        elif card_value == 12:
            return 11
        else:
            return 10

    def get_value(self, soft: bool) -> int:
        """Gets the value of a card

        Args:

            soft (bool) : If the hand (holder of the n cards) is soft, aces gets the value of 1

        Returns:
            int : The value of the card
        """
        if self.value != 11:
            return self.value
        else:
            if soft:
                return 1
            else:
                return 11

    def __str__(self) -> str:
        """Generates a readable presentation of the card

        Returns:
            str : The readable string, including the cards color and number
        """
        return "{} {}".format(self.color, self.number)