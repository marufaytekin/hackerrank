"""
Write a stack that would return the minimum element in O(1) time.
"""
class Stack:
    def __init__(self):
        self._items = []
        self._min = []

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def __str__(self):
        return str(self._items)

    def push(self, item):
        self._items.insert(0, item)
        if not self._min or item < self._min[0]:
            self._min.insert(0, item)

    def pop(self):
        top = self._items.pop(0)
        if top == self._min[0]:
            self._min.pop(0)
        return top

    def get_min(self):
        return self._min[0]


stack = Stack()

stack.push(2)
stack.push(3)
stack.push(4)
print stack.get_min()
print stack.pop()
print stack.get_min()
print stack.pop()
stack.push(1)
print stack.get_min()
print stack.get_min()

