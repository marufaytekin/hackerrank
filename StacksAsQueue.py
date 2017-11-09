"""
A queue is an abstract data type that maintains the order in which elements 
were added to it, allowing the oldest elements to be removed from the front 
and new elements to be added to the rear. This is called a First-In-First-Out 
(FIFO) data structure because the first element added to the queue (i.e., the 
one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then 
process q queries, where each query is one of the following 3 types:

1. 1 x: Enqueue element  into the end of the queue.
2. 2: Dequeue the element at the front of the queue.
3. 3: Print the element at the front of the queue.
"""


class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.append(self.first.pop())
        return self.second[-1]

    def pop(self):
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.append(self.first.pop())
        return self.second.pop()

    def put(self, value):
        self.first.append(value)


queue = MyQueue()

l = [1, 2, 3, 4]

for i in l:
    queue.put(i)

print(queue.first)
print(queue.second)

queue.pop()
queue.pop()
print(queue.peek())
