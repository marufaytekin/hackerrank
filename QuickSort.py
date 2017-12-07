def quick_sort(my_list):
    """
    O(n log(n)
    :param my_list:
    :return:
    """
    if not my_list:
        return my_list
    pivot = my_list[0]
    less_list = [elem for elem in my_list if elem < pivot]
    pivots = [elem for elem in my_list if elem == pivot]
    high_list = [elem for elem in my_list if elem > pivot]
    return quick_sort(less_list) + pivots + quick_sort(high_list)

l = [1, 33, 11, -9, 6, 6, 2, 9, 4, 0, 16]
print(quick_sort(l))
