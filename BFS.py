class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)


class Node:
    def __init__(self, val):
        self._left = None
        self._right = None
        self._val = val

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_val(self):
        return self._val


def bfs(root, target):
    queue = Queue()
    queue.push(root)
    while len(queue) != 0:
        temp = queue.pop()
        print temp.get_val()
        if temp.get_val() == target:
            return target
        left = temp.get_left()
        right = temp.get_right()
        if left is not None:
            queue.push(left)
        if right is not None:
            queue.push(right)
    return None

root = Node(6)
leaf = Node(4)
leaf.set_left(Node(3))
leaf.set_right(Node(5))
root.set_left(leaf)
leaf = Node(8)
leaf.set_left(Node(7))
leaf.set_right(Node(9))
root.set_right(leaf)

print bfs(root, 5)


