"""
implementation of binary search tree
"""
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, curr, val):
        curr_val = curr.val
        left = curr.left
        right = curr.right
        if val < curr_val:
            if left is None:
                curr.left = Node(val)
            else:
                self.insert_node(left, val)
        elif val > curr_val:
            if right is None:
                curr.right = Node(val)
            else:
                self.insert_node(right, val)

    def create_bst(self, a, left, right):
        """
        creates a balanced binary search tree from a sorted list
        """
        if left > right:
            return
        mid = (left + right) / 2
        self.insert(a[mid])
        self.create_bst(a, left, mid - 1)
        self.create_bst(a, mid + 1, right)

    def print_tree(self):
        curr_level = [self.root]
        while curr_level:
            next_level = list()
            sys.stdout.write(' '.join(str(node.val) for node in curr_level))
            for curr in curr_level:
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            print
            curr_level = next_level
        return

    def print_tree_flat(self):
        self.print_tree_flat2(self.root)

    def print_tree_flat2(self, node):
        if node is None:
            return
        sys.stdout.write("(")
        self.print_tree_flat2(node.left)
        sys.stdout.write(str(node.val))
        self.print_tree_flat2(node.right)
        sys.stdout.write(")")


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tree = BST()
tree.create_bst(l, 0, len(l)-1)
tree.print_tree()
tree.print_tree_flat()


