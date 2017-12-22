import random
from swap import swap


def shuffle(my_list):
    n = len(my_list)
    for i in range (1, n):
        j = random.randint(0, i-1)
        swap(my_list, i, j)
    return my_list


def shuffle_string(s):
    n = len(s)
    arr = list(s)
    for i in range(1, n):
        j = random.randint(0, i-1)
        swap(arr, i, j)
    return ''.join(arr)


l = [1,9,3,5,7,0,-3,2,3,4]

print shuffle(l)
print shuffle_string("ahmet aytekin")