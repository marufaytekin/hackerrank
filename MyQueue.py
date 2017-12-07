"""
Implement a queue with two stacks.
"""


class MyQueue(object):
    def __init__(self):
        self._first = []
        self._second = []

    def peek(self):
        if len(self._second) == 0:
            while len(self._first) != 0:
                self._second.insert(0, self._first.pop(0))
        return self._second[0]

    def pop(self):
        if len(self._second) == 0:
            while len(self._first) != 0:
                self._second.insert(0, self._first.pop(0))
        return self._second.pop(0)

    def put(self, value):
        self._first.insert(0, value)


queue = MyQueue()
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(1)

print queue.peek()
print queue.pop()
print queue.peek()
print queue.pop()
print queue.peek()
print queue.pop()
print queue.peek()
print queue.pop()
print queue.pop()
