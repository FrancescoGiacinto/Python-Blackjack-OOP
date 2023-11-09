from dealer import Dealer
from player import Player
from deck import Deck
from hand import Hand

class BlackJack:
    """
    Represents the core game logic for Blackjack.

    Attributes:
        player_name (str): Name of the player.
        player_balance (int): Player's balance.
        dealer_name (str): Name of the dealer.
        dealer (Dealer): Dealer object.
        player (Player): Player object.
        deck (Deck): Deck of cards used in the game.
    """
    def __init__(self)->None:
        """
        Initializes a BlackJack game with empty player and dealer names, and a fresh deck of cards.
        """
        self.player = Player()        
        self.dealer = Dealer()
        self.deck = Deck()


    def play(self) -> None:
        """Main game loop for playing rounds of Blackjack."""
        
        self.welcome()

        while True:
            self.status()  # Mostra lo stato attuale del giocatore

            # Ottieni la scommessa del giocatore e assicurati che abbiano abbastanza saldo
            while True:
                try:
                    bet = int(input("Enter your bet: "))
                    if bet <= self.player.get_balance():
                        self.player.remove_money(bet)
                        break
                    
                    # Il giocatore non ha abbastanza saldo
                    print("You don't have enough balance.")
                    
                    # Chiedi al giocatore se vuole ricaricare
                    choice = input("Do you want to recharge your balance? (y/n): ").lower()
                    if choice == 'y':
                        while True:
                            try:
                                recharge_amount = int(input("How much would you like to add to your balance? "))
                                self.player.add_money(recharge_amount)
                                print(f"You have added {recharge_amount} to your balance. Your new balance is {self.player.get_balance()}.")
                                break
                            except ValueError:
                                print("Please enter a valid number.")
                    else:
                        print("You still need to bet an amount less than or equal to your balance.")
                        
                except ValueError:
                    print("Please enter a valid number.")
            
            # Reset deck and hands
            self.deck.generate_deck()
            self.deck.shuffle_deck()

            # Create new hands for the player and dealer
            self.player.set_hand(Hand())
            self.dealer.set_hand(Hand())
            self.player_hand = self.player.get_hand()
            self.dealer_hand = self.dealer.get_hand()

            # Initial card dealing
            for _ in range(2):
                self.player_hand.add_card(self.dealer.draw_card(self.deck))
            self.dealer_hand.add_card(self.dealer.draw_card(self.deck))

            # Display the initial card dealing
            print("-------Dealt cards:")
            print("",self.player.name," hand:", self.player_hand, "Total:", self.player_hand.total_sum())
            print("",self.dealer.name,"'s face-up card:", self.dealer_hand.get_first_card(), "Total:", self.dealer_hand.total_sum())

            if self.player_hand.is_blackjack():
                print("Blackjack! You win!")
                self.player.add_money(bet * 2.5)
                continue
            
            while input("Do you want to hit or stand? (h/s) ").lower() == 'h':
                self.player_hand.add_card(self.dealer.draw_card(self.deck))
                print("",self.player.name," hand:", self.player_hand, "Total:", self.player_hand.total_sum())
                if self.player_hand.is_busted():
                    print("Busted!")
                    break

            # Dealer's turn if player hasn't busted
            if not self.player_hand.is_busted():
                print("-------Dealer's turn:")
                while self.dealer_hand.total_sum() < 17:
                    self.dealer_hand.add_card(self.dealer.draw_card(self.deck))
                
                if self.dealer_hand.is_busted():
                    print("Dealer's hand:", self.dealer_hand, "Total:", self.dealer_hand.total_sum())
                    print("You win!")
                    self.player.add_money(bet * 2)
                elif self.player_hand.total_sum() > self.dealer_hand.total_sum():
                    print("",self.dealer.name,"'s hand:", self.dealer_hand, "Total:", self.dealer_hand.total_sum())
                    print("You win!")
                    self.player.add_money(bet * 2)
                else:
                    print("",self.dealer.name," wins!")
                    print("",self.dealer.name,"'s hand:", self.dealer_hand, "Total:", self.dealer_hand.total_sum())
                    self.player.remove_money(bet)

            if self.player.get_balance() <= 0:
                print("Game over")
                if input("Do you want to start a new game? (y/n) ").lower() == 'y':
                    self.welcome()
                else:
                    return



    def welcome(self)->None:
        """
        Welcome screen for the Blackjack game. Takes player's and dealer's names and the initial balance for the player.
        """
        print("="*40)
        print("Welcome to BlackJack!")
        print("="*40)
        print()

        player_name = input("What's your name? ")
        
        while True:
            try:
                initial_balance = int(input(f"How much would you like to play ? "))
                break
            except ValueError:
                print("Please enter a valid number.")

        self.player = Player(initial_balance)
        self.player.set_name(player_name)  

        dealer_name = input("What's the dealer's name today? ")
        self.dealer.set_name(dealer_name)

        print(f"Welcome {player_name} and good luck!")
        print(f"The dealer today is {dealer_name}")
        print("="*40)



    def status(self)->None:
        """
        Displays the current status of the player.
        """
        print("*"*16 + " Status " + "*"*16)
        print(f"player:{self.player.name} balance: {self.player.get_balance()}")
        print("*"*40)





    def dealer_draw_cards(self)->None:
        """
        Makes the dealer draw cards until the sum of their hand is at least 17.
        """
        while self.dealer.get_hand().total_sum() < 17:
            self.dealer.draw_card(None, None, self.deck)


game = BlackJack()
game.play()