from src.Dealer import Dealer
from src.Deck import Deck

__author__ = 'Darryl'


class Game:
    def __init__(self, player):
        self._player = player
        self._player.receive_money(100)
        self._dealer = Dealer()
        self._deck = Deck()
        self._result = ""
        self._bet = 0

    def placed_bet(self):
        return self._bet

    def take_bet(self, bet):
        self._bet = bet

    def increase_bet(self, bet):
        self._bet += bet

    def reset(self):
        self._player.clear_hand()
        self._dealer.clear_hand()
        self._deck = Deck()
        self._result = ""

    def get_player(self):
        return self._player

    def get_dealer(self):
        return self._dealer

    def get_deck(self):
        return self._deck

    def get_result(self):
        return self._result

    def set_result(self, result):
        self._result = result


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_game.txt")