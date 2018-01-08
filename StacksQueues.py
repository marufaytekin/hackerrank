class Stack:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def __str__(self):
        return str(self._items)

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)


class Queue:
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
        self._items.append(item)
        if not self._min or item < self._min[0]:
            self._min.insert(0, item)

    def pop(self):
        top = self._items.pop(0)
        if top == self._min[0]:
            self._min.pop(0)
        return top

    def get_min(self):
        if not self._min:
            return None
        else:
            return self._min[0]


container = Stack()
container.push(1)
container.push(3)
container.push(4)
container.push(5)
print container.pop()


container = Queue()
container.push(1)
container.push(2)
container.push(3)
container.push(4)
print container.get_min()
print container.pop()

print len(container)
print container.get_min()


