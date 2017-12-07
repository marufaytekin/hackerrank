"""
Given n distinct positive integers, integer k (k <= n) and a number target.
Find k numbers where sum is target. Calculate how many solutions there are?
"""


def sum_to(l, t):
    ret = []
    size = len(l)
    for i in range(size):
        for j in range(i + 1, size):
            if (l[i] + l[j]) == t:
                ret.append((l[i], l[j]))
    return ret


l = [1, 2, 3, 4]
k = 2
target = 5.

print(sum_to(l, target))


def sum_to_rec(l, t):
    pass
