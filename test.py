import unittest
from card import Card
from hand import Hand  
        #self.dealer = Dealer(self.dealer)
        #self.player = Player(self.player, 0) 

class TestIsBlackjackFunction(unittest.TestCase):

    def setUp(self):
        """This function will run before each test, creating a fresh instance of a Hand for each test."""
        self.hand = Hand()

    def test_blackjack_true(self):
        """Test if is_blackjack() returns True for a valid Blackjack hand."""
        ace_of_spades = Card(38)  # This should create an Ace of Spades, based on your Card class
        ten_of_hearts = Card(8)   # This should create a 10 of Hearts
        
        self.hand.add_card(ace_of_spades)
        self.hand.add_card(ten_of_hearts)
        
        self.assertTrue(self.hand.is_blackjack())

    def test_blackjack_false(self):
        """Test if is_blackjack() returns False for a non-Blackjack hand."""
        two_of_spades = Card(0)   # This should create a 2 of Spades
        three_of_hearts = Card(2) # This should create a 3 of Hearts

        self.hand.add_card(two_of_spades)
        self.hand.add_card(three_of_hearts)
        
        self.assertFalse(self.hand.is_blackjack())

    def test_more_than_two_cards(self):
        """Test if is_blackjack() returns False for hands with more than two cards, even if they total 21."""
        seven_of_spades = Card(5)  # This should create a 7 of Spades
        two_of_hearts = Card(0)    # This should create a 2 of Hearts
        ace_of_diamonds = Card(25) # This should create an Ace of Diamonds
        
        self.hand.add_card(seven_of_spades)
        self.hand.add_card(two_of_hearts)
        self.hand.add_card(ace_of_diamonds)
        
        self.assertFalse(self.hand.is_blackjack())

if __name__ == "__main__":
    unittest.main()
