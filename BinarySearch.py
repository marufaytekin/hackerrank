import sys


class Node:
    """
    simple binary search tree node
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BST:
    """
    simple binary search tree
    """

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, curr, val):
        if val < curr.val:
            if curr.left is None:
                curr.left = Node(val)
            else:
                self.insert_node(curr.left, val)
        elif val > curr.val:
            if curr.right is None:
                curr.right = Node(val)
            else:
                self.insert_node(curr.right, val)
        else:
            curr.val = val


def create_bst(a, t, left, right):
    """
    creates a balanced binary search tree from a sorted list
    """
    if left > right:
        return
    mid = (left + right) / 2
    t.insert(a[mid])
    create_bst(a, t, left, mid - 1)
    create_bst(a, t, mid + 1, right)


def binary_search(sorted_list, left, right, k):
    """
    binary search on sorted list
    """
    if left > right:
        return False
    mid = (left + right) / 2
    # print left, right
    if k < sorted_list[mid]:
        return binary_search(sorted_list, left, mid - 1, k)
    elif k > sorted_list[mid]:
        return binary_search(sorted_list, mid + 1, right, k)
    else:
        return sorted_list[mid]


my_list = []

for i in range(0, 10):
    my_list.append(i)

print binary_search(my_list, 0, len(my_list) - 1, 99)

tree = BST()
create_bst(my_list, tree, 0, len(my_list) - 1)


def print_tree(root):
    curr_level = [root]
    while curr_level:
        next_level = list()
        sys.stdout.write (' '.join(str(node) for node in curr_level))
        for curr in curr_level:
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
        print
        curr_level = next_level
    return


def print_tree2(root):
    if root is None:
        return
    sys.stdout.write("(")
    print_tree(root.left)
    sys.stdout.write(str(root.val))
    print_tree(root.right)
    sys.stdout.write(")")


print_tree(tree.root)

#print_tree2(tree.root)


def dfs(root):
    if root is None:
        return
    sys.stdout.write(str(root.val) + ' ')
    if root.left:
        dfs(root.left)
    if root.right:
        dfs(root.right)


def bfs(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while len(queue) != 0:
        curr = queue.pop(0)
        sys.stdout.write(str(curr.val) + ' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

#
# print
# dfs (tree.root)
# print
# bfs(tree.root)


def pre_order(root):
    if not root:
        return
    sys.stdout.write(str(root.val) + ' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    if not root:
        return
    in_order(root.left)
    sys.stdout.write(str(root.val) + ' ')
    in_order(root.right)


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    sys.stdout.write(str(root.val) + ' ')

print "\npreorder:"
pre_order(tree.root)
print "\nin order:"
in_order(tree.root)
print "\npost order:"
post_order(tree.root)