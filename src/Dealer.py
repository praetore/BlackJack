from src.Player import Player

__author__ = 'Darryl'


class Dealer(Player):
    def __init__(self):
        super().__init__()
        self._hidden = None

    def receive_card(self, card):
        print("Dealer received a %s" % card)
        super().receive_card(card)

    def receive_hidden(self, card):
        self._hidden = card

    def get_hidden(self):
        if not self._hidden:
            print("Dealer has revealed all cards")
        else:
            return self._hidden

    def reveal_hidden(self):
        self._hand.append(self._hidden)
        self._hidden = None

    def check_hand(self):
        if len(self._hand):
            print("Dealer has:")
            super().check_hand()
            print("Dealer thus has a total of %d" % self.get_hand_value())
        else:
            print("Dealer has no cards in hand")


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_dealer.txt")