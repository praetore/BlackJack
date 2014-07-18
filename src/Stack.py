__author__ = 'Darryl'


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def size(self):
        return len(self._items)

    def pop(self):
        item = self._items[-1]
        del self._items[-1]
        return item

    def peek(self):
        return self._items[-1]