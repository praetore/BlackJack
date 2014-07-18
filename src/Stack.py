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


def main():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


if __name__ == '__main__':
    main()