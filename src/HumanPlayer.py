from src.Errors import NotEnoughMoneyError, NegativeMoneyError
from src.Player import Player

__author__ = 'Darryl'


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._money = 0

    def receive_card(self, card):
        print("%s receives a %s" % (self._name, card))
        super().receive_card(card)

    def check_hand(self):
        if len(self._hand):
            print("%s has the following cards in hand:" % self._name)
            super().check_hand()
            print("%s thereby has a total of %d" % (self._name, self.get_hand_value()))
        else:
            print("%s has no cards in hand" % self._name)

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

    def get_name(self):
        return self._name

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_humanplayer.txt")