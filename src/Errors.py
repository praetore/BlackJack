__author__ = 'darryl'


class DuplicateCardError(Exception):
    def __init__(self):
        Exception.__init__(self, "Card already in deck")


class EmptyDeckError(Exception):
    def __init__(self):
        Exception.__init__(self, "No cards left in deck")


class NotEnoughMoneyError(Exception):
    def __init__(self):
        Exception.__init__(self, "Player does not have enough money")


class NegativeMoneyError(Exception):
    def __init__(self):
        Exception.__init__(self, "A negative monetary value was given")