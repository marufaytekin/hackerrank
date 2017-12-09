class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

    def get_val(self):
        return self._val

    def get_right(self):
        return self._right

    def get_left(self):
        return self._left

    def set_val(self, val):
        self._val = val

    def set_right(self, r):
        self._right = r

    def set_left(self, l):
        self._left = l


class BST:
    def __init__(self):
        self._root = None

    def insert(self, val):
        if self._root is None:
            self._root = Node(val)
        else:
            self.insert_node(self._root, val)

    def insert_node(self, curr, val):
        curr_val = curr.get_val()
        left = curr.get_left()
        right = curr.get_right()
        if val < curr_val:
            if left is None:
                curr.set_left(Node(val))
            else:
                self.insert_node(left, val)
        elif val > curr_val:
            if right is None:
                curr.set_right(Node(val))
            else:
                self.insert_node(right, val)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = BST()

for item in l:
    tree.insert(item)


def create_bst(a, l, r, root):
    print l, r
    if l > r:
        return
    else:
        m = (l + r) / 2
        tree.insert(a[m])
        create_bst(a, l, m-1, root)
        create_bst(a, m+1, r, root)


tree = BST()
create_bst(l, 0, len(l)-1, tree)
pass


