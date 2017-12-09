import random


def quick_sort(my_list):
    """
    O(n log(n)
    """
    if not my_list:
        return my_list
    pivot = my_list[0]
    less_list = [elem for elem in my_list if elem < pivot]
    pivots = [elem for elem in my_list if elem == pivot]
    high_list = [elem for elem in my_list if elem > pivot]
    print less_list, pivots, high_list
    return quick_sort(less_list) + pivots + quick_sort(high_list)

l = [1, 33, 11, -9, 6, 6, 2, 9, 4, 0, 16]
random.shuffle(l)

print quick_sort(l)
