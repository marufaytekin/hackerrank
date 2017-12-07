from swap import swap


def insertion_sort(my_list):
    """
    insertion sort
    O(n^2)
    """
    N = len(my_list)
    for i in range(N):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j-1]:
                swap(my_list, j-1, j)
    return my_list

l = [4, 9, 2, 0, 1, 3, 4, 6, 5]

print (insertion_sort(l))



