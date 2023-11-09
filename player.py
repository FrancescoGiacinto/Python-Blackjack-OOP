from card_player import Card_player

class Player(Card_player):
    '''This is the players class'''
    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self)-> int:
        '''this show upp how much money the players has.'''
        return self.balance

    def add_money(self, amount)-> int:
        """ this one add the money if the players has won the game"""
        self.balance += amount
        return amount 

    def remove_money(self, amount)->int:
        '''This function deducts money if the player has lost the game.'''
        self.balance -= amount
        return amount