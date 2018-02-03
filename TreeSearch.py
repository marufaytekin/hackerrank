import sys
from BST import BST


def dfs(root, target):
    """
    depth first search on binary tree
    """
    if root is None:
        return None
    sys.stdout.write(str(root.val) + ' ')
    if root.val == target:
        return root
    if root.left:
        dfs(root.left, target)
    if root.right:
        dfs(root.right, target)


def bfs(root, target):
    """
    breadth first search on binary tree
    """
    if root is None:
        return
    queue = list()
    queue.append(root)
    while len(queue) != 0:
        curr = queue.pop(0)
        sys.stdout.write(str(curr.val) + ' ')
        if curr.val == target:
            return curr
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


# create a test data
my_list = []
for i in range(0, 10):
    my_list.append(i)

tree = BST()
tree.create_bst(my_list, 0, len(my_list) - 1)


print "dfs: "
dfs(tree.root, 7)
print "\nbfs: "
bfs(tree.root, 7)
