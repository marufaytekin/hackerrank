def quick_sort(nlist):
    """
    O(n log(n)
    :param nlist:
    :return:
    """
    if not nlist:
        return nlist
    pivot = nlist[0]
    less_list = [elem for elem in nlist if elem < pivot]
    pivots = [elem for elem in nlist if elem == pivot]
    high_list = [elem for elem in nlist if elem > pivot]
    return quick_sort(less_list) + pivots + quick_sort(high_list)

l = [1, 33, 11, -9, 6, 6, 2, 9, 4, 0, 16]
print(quick_sort(l))
