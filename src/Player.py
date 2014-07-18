__author__ = 'Darryl'


class Player(object):
    def __init__(self):
        self._hand = []

    def receive_card(self, card):
        self._hand.append(card)

    def check_hand(self):
        [print(card) for card in self._hand]

    def get_hand_value(self):
        value = sum(card.get_value() for card in self._hand)

        # Checking for a soft hand
        aces_in_hand = sum(1 for card in self._hand if card.get_name() == "Ace")
        while value > 21 and aces_in_hand > 0:
            aces_in_hand -= 1
            value -= 10
        return value

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_player.txt")