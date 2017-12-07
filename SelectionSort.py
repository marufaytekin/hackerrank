"""
ELementery Sorting
"""

from swap import swap


def sort(my_list):
    """
    selection sort
    O(n^2) complexity
    """
    size = len(my_list)
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        swap(my_list, i, min_idx)
    return my_list


l = [4, 9, 2, 1, 6, 8, 7, 4, 0]

print (sort(l))
