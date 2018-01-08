def binary_search(sorted_list, left, right, k):
    """
    binary search on a sorted list
    """
    if left > right:
        return False
    mid = (left + right) / 2
    if k < sorted_list[mid]:
        return binary_search(sorted_list, left, mid - 1, k)
    elif k > sorted_list[mid]:
        return binary_search(sorted_list, mid + 1, right, k)
    else:
        return sorted_list[mid]

# create a sorted list
my_list = []
for i in range(0, 10):
    my_list.append(i)

# run binary search on the sorted list
print binary_search(my_list, 0, len(my_list) - 1, 8)
print binary_search(my_list, 0, len(my_list) - 1, 11)



