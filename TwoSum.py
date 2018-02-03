"""
Given n distinct positive integers and a number target.
Find two numbers where sum is target.
Calculate how many solutions there are?
"""


def sum_to(my_list, target):
    """
    O(n^2)
    """
    if not my_list or not target:
        return None
    result = []
    size = len(my_list)
    for i in range(size):
        for j in range(i + 1, size):
            if (my_list[i] + my_list[j]) == target:
                result.append((my_list[i], my_list[j]))
    return result


def sum_to2(my_list, target):
    """
    O(n)
    """
    if not my_list or not target:
        return None
    result = []
    size = len(my_list)
    dd = {}
    for i in range(size):
        curr = my_list[i]
        dd[curr] = curr
    for j in range(size):
        curr = my_list[j]
        complement = target - curr
        if complement in dd and complement != curr:
            result.append((curr, complement))
            dd.pop(complement)
            dd.pop(curr)
    return result


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
t = 20

print sum_to(l, t)
print sum_to2(l, t)

