import random
from src.Card import Card
from src.Constants import SUITS, VALUES, FACE_CARDS
from src.Errors import DuplicateCardError, EmptyDeckError
from src.Stack import Stack

__author__ = 'darryl'


class Deck():
    """
    Represents a deck of playing cards
    """

    def __init__(self):
        self._deck = Stack()
        [self._deck.push(Card(value, suit)) for suit in SUITS for value in VALUES]
        [self._deck.push(Card(value, suit)) for suit in SUITS for value in FACE_CARDS]
        self.shuffle_deck()

    def add_card(self, card):
        check = [self._deck.pop() for i in range(self._deck.get_size())]
        check.reverse()
        if card not in check:
            check.append(card)
            [self._deck.push(i) for i in check]
        else:
            [self._deck.push(i) for i in check]
            raise DuplicateCardError

    def take_card(self):
        if self._deck.get_size() > 0:
            return self._deck.pop()
        else:
            raise EmptyDeckError

    def shuffle_deck(self):
        deck = [self._deck.pop() for i in range(self._deck.get_size())]
        deck = random.sample(deck, len(deck))
        [self._deck.push(i) for i in deck]

    def size(self):
        return self._deck.get_size()

    def __repr__(self):
        current = [str(card) for card in self._deck]
        return "Current cards in deck: %s" % ", ".join(current)

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_deck.txt")