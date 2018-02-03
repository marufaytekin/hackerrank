"""
Is the list consist of consecutive integers?
"""


def is_consecutive(l):
    size = len(l)
    if len(set(l)) != size:
        return False
    sorted_list = sorted(l)
    first = sorted_list[0]
    last = sorted_list[-1]
    if last - first + 1 != size:
        return False
    else:
        return True


def is_consecutive_rec(l):
    """
    recursive implementation
    l: sorted list
    """
    size = len(l)
    if size == 1:
        return True
    if size == 2:
        return l[1] - l[0] == 1
    mid = size / 2
    left = l[:mid]
    right = l[mid:]
    return is_consecutive_rec(left) and is_consecutive_rec(right) and right[0] - left[-1] == 1


l1 = [1, 2, 3, 4]
l2 = [-1, 2, 3, 4]
l3 = [-1, 0, 1, 2, 3, 4]
l4 = [1, 2, 2, 3, 4]
l5 = [400, 399, 398, 398]
l6 = [1, 2, 3, 4, 6]
print is_consecutive(l1)
print is_consecutive(l2)
print is_consecutive(l3)
print is_consecutive(l4)
print is_consecutive(l5)
print is_consecutive(l6)
print
print is_consecutive_rec(sorted(l1))
print is_consecutive_rec(sorted(l2))
print is_consecutive_rec(sorted(l3))
print is_consecutive_rec(sorted(l4))
print is_consecutive_rec(sorted(l5))
print is_consecutive_rec(sorted(l6))
