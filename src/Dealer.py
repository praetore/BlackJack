from src.Player import Player

__author__ = 'Darryl'


class Dealer(Player):
    def receive_card(self, card):
        print("Dealer received a %s" % card)
        super().receive_card(card)

    def receive_hidden(self, card):
        self._hidden = card

    def get_hidden(self):
        return self._hidden

    def reveal_hidden(self):
        self._hand.append(self._hidden)

    def check_hand(self):
        print("Dealer has:")
        super().check_hand()
        print("Dealer thus has a total of %d" % self.get_hand_value())
        input("Press a key to continue")

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_dealer.txt")