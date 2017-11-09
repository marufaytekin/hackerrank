class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BTNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BTNode(value)
        return self.right

def btree (node):
    pass


