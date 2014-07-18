from src.Constants import FACE_CARDS, VALUES, SUITS

__author__ = 'darryl'


class Card:
    """
    Represents a basic playing card.
    """

    def __init__(self, value, suit):
        if value in FACE_CARDS or value in VALUES:
            self._name = value
            if value in FACE_CARDS:
                self._value = FACE_CARDS.index(value) + 9
            if value in VALUES:
                self._value = VALUES.index(value)
        if suit in SUITS:
            self._suit = suit

    def __repr__(self):
        return "Value: (%s - Rank: %d) - Suit: %s" % (self._name, self._value, self._suit)

    def __str__(self):
        return "%s of %s" % (self._name, self._suit)

    def __gt__(self, y):
        return self._value > y.get_value()

    def __ge__(self, y):
        return self._value >= y.get_value()

    def __lt__(self, y):
        return self._value < y.get_value()

    def __le__(self, y):
        return self._value <= y.get_value()

    def __eq__(self, y):
        return self._value == y.get_value() and self._suit == y.get_suit()

    def __ne__(self, y):
        return self._value != y.get_value() or self._suit != y.get_suit()

    def get_name(self):
        return self._name

    def get_suit(self):
        return self._suit

    def get_value(self):
        return self._value


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_card.txt")