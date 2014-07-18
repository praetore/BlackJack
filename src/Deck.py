import random
from src.Card import Card
from src.Constants import SUITS, VALUES, FACE_CARDS
from src.Errors import DuplicateCardError, EmptyDeckError
from src.Stack import Stack

__author__ = 'darryl'


class Deck(Stack):
    """
    Represents a deck of playing cards
    """

    def __init__(self):
        super().__init__()
        [self.push(Card(value, suit)) for suit in SUITS for value in VALUES]
        [self.push(Card(value, suit)) for suit in SUITS for value in FACE_CARDS]
        self.shuffle_deck()

    def add_card(self, card):
        if card not in self._items:
            self.push(card)
        else:
            raise DuplicateCardError

    def take_card(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise EmptyDeckError

    def shuffle_deck(self):
        self._items = random.sample(self._items, len(self._items))

    def __repr__(self):
        current = [str(card) for card in self._items]
        return "Current cards in deck: %s" % ", ".join(current)

if __name__ == '__main__':
    import doctest
    doctest.testfile("../tests/test_deck.txt")