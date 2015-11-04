__author__ = 'Pratik'

class Node:
    __slots__ = 'data', 'next'

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getValue(self):
        return self.data
