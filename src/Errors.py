__author__ = 'darryl'


class DuplicateCardError(Exception):
    def __init__(self):
        Exception.__init__(self, "Card already in deck")


class EmptyDeckError(Exception):
    def __init__(self):
        Exception.__init__(self, "No cards left in deck")