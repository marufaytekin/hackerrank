import random
from swap import swap


def shuffle(my_list):
    N = len(my_list)
    for i in range (1, N):
        j = random.randint(0, i-1)
        swap(my_list, i, j)
    return my_list

l1 = [1,9,3,5,7,0,2,3,4]

l2 = [1,2,3,4,5,6,7,8,9]


print shuffle(l1)
print shuffle(l2)
