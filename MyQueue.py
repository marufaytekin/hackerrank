"""
Implement a queue with two stacks.
"""
class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.insert(0, self.first.pop(0))
        return self.second[0]

    def pop(self):
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.insert(0, self.first.pop(0))
        return self.second.pop(0)

    def put(self, value):
        self.first.insert(0, value)


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
