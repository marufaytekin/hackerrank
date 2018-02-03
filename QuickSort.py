"""
Quick sort algorthm:
1. Select a random element (pivot)
2. Find all smaller elements and move them to the left of the pivot element.
3. Find all larger elements and move them to the right of the pivot element.
4. Repeat the same process for the left side of the pivot element
5. Repeat the same process for the right side of the pivot element
6. Merge and return results from left, pivot, and right side. 
"""
import random


def quick_sort(my_list):
    if len(my_list) == 0:
        return []
    pivot = my_list[0]
    small_arr = [element for element in my_list if element < pivot]
    pivots = [element for element in my_list if element == pivot]
    large_arr = [element for element in my_list if element > pivot]
    return quick_sort(small_arr) + pivots + quick_sort(large_arr)


l1 = []
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 0]
random.shuffle(l3)

print(quick_sort(l1))
print(quick_sort(l2))
print(quick_sort(l3))
