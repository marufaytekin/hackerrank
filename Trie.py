class Node():
    def __init__(self, key, val):
        self.key = key
        self.data = val
        self.children = dict()

    def add_child(self, key, val=None):
        if isinstance(key, Node):
            self.children[key.key] = key
        else:
            self.children[key] = Node(key, val)


