"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""

import Queue


# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def check_tree(root):
    """
    non-recursive
    """
    q = Queue()
    q.put(root)
    q.put(root)
    while not q.isEmpty:
        t1 = q.get()
        t2 = q.get()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        q.put(t1.left)
        q.put(t2.right)
        q.put(t1.right)
        q.put(t2.left)
    return True


def check_tree_rec(t1, t2):
    """
    recursive
    """
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.val == t2.val and check_tree_rec(t1.left, t2.right) and check_tree_rec(t1.right, t2.left)


def is_symmetric(root):
    return check_tree_rec(root, root)
