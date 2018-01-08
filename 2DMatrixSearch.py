"""
Search element in sorted 2D matrix
O(n)
"""


def binary_search(my_list, elem):
    if not my_list:
        return False
    mid = len(my_list) / 2
    if elem == my_list[mid]:
        return elem
    elif elem < my_list[mid]:
        return binary_search(my_list[:mid], elem)
    else:
        return binary_search(my_list[mid:], elem)


def search(elem, matrix):
    curr_line = None
    for line in matrix:
        if elem == line[-1]:
            return elem
        elif elem < line[-1]:
            curr_line = line
            break
    if curr_line is None:
        return False
    else:
        return binary_search(curr_line, elem)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert 1 == search(1, m)
assert 2 == search(2, m)
assert 4 == search(4, m)
assert 6 == search(6, m)
assert 9 == search(9, m)
assert not search(-1, m)
assert not search(10, m)
assert 1 == binary_search([1, 2, 3], 1)
assert 4 == binary_search([1, 2, 3, 4], 4)



