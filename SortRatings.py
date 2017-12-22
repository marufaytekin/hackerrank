data = [("a", 1), ("b", 2), ("d", 10), ("e", 5), ("f", 3)]

sorted_data = sorted(data, key=lambda x: x[1])

print sorted_data


"""
Quick sort for tuple
"""
def quick_sort(my_list):
    if len(my_list) == 0:
        return []
    else:
        pivot = my_list[0]
        left = [element for element in my_list if element[1] < pivot[1]]
        pivots = [element for element in my_list if element[1] == pivot[1]]
        right = [element for element in my_list if element[1] > pivot[1]]
        return quick_sort(left) + pivots + quick_sort(right)

print quick_sort(data)



