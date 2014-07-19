from src.Errors import NotEnoughMoneyError, NegativeMoneyError
from src.Player import Player

__author__ = 'Darryl'


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self._money = 0

    def receive_card(self, card):
        print("You received a %s" % card)
        super().receive_card(card)

    def check_hand(self):
        if len(self._hand):
            print("You have the following cards in your hand:")
            super().check_hand()
            print("You thereby have a total of %d" % self.get_hand_value())
        else:
            print("Player has no cards in hand")

    def place_bet(self, bet=0):
        if bet == 0:
            bet = int(input("Place your bet: "))
        if bet > 0:
            if self._money >= bet:
                self._money -= bet
                return bet
            else:
                raise NotEnoughMoneyError
        else:
            raise NegativeMoneyError

    def receive_money(self, amount):
        if amount > 0:
            self._money += amount
        else:
            raise NegativeMoneyError

    def check_money(self):
        return self._money

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_humanplayer.txt")