from src.Constants import FACE_CARDS, VALUES, SUITS
from src.Errors import InvalidCardError

__author__ = 'darryl'


class Card:
    """
    Represents a basic playing card.
    """

    def __init__(self, card_name, suit):
        if card_name in FACE_CARDS or card_name in VALUES:
            self._name = card_name
            if card_name in FACE_CARDS:
                if card_name != "Ace":
                    self._value = 10
                else:
                    self._value = 11
            elif card_name in VALUES:
                self._value = card_name
        else:
            raise InvalidCardError

        if suit in SUITS:
            self._suit = suit
        else:
            raise InvalidCardError

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
        return self._name == y.get_name() and self._suit == y.get_suit()

    def __ne__(self, y):
        return self._name != y.get_name() or self._suit != y.get_suit()

    def get_name(self):
        return self._name

    def get_suit(self):
        return self._suit

    def get_value(self):
        return self._value


if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_card.txt")