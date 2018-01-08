import sys
from BST import BST


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

my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]

tree = BST()

tree.create_bst(my_list, 0, len(my_list) - 1)

print "\npreorder:"
pre_order(tree.root)
print "\nin order:"
in_order(tree.root)
print "\npost order:"
post_order(tree.root)