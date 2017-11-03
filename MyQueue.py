class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        first = self.second.pop()
        while len(self.second) is not 0:
            self.first.append(self.second.pop())
        while len(self.first) is not 0:
            self.second.append(self.first.pop())
        self.second.append(first)
        return first

    def pop(self):
        return self.second.pop()

    def put(self, value):
        while len(self.second) is not 0:
            self.first.append(self.second.pop())
        self.first.append(value)
        while len(self.first) is not 0:
            self.second.append(self.first.pop())



queue = MyQueue()
queue.put(2)
queue.put(3)
queue.put(4)
print queue.peek()
print queue.pop()
queue.put(5)
print queue.pop()
queue.put(1)
print queue.pop()
print queue.pop()
print queue.pop()



