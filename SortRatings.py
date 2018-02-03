"""
Yelp interview question:
Sort the lists of ratings in k, v format.
"""


def quick_sort(my_list):
    """
    Quick sort for list of tuples in (X0, X1) format
    """
    if len(my_list) == 0:
        return []
    else:
        pivot = my_list[0]
        left = [element for element in my_list if element[1] < pivot[1]]
        pivots = [element for element in my_list if element[1] == pivot[1]]
        right = [element for element in my_list if element[1] > pivot[1]]
        return quick_sort(left) + pivots + quick_sort(right)


data = [("a", 1), ("b", 2), ("d", 10), ("e", 5), ("f", 3)]

# built in sorted function with a lambda function.
sorted_data = sorted(data, key=lambda x: x[1])
print sorted_data

# quick sort for tuples.
print quick_sort(data)
