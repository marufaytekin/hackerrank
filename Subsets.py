"""
Given as an array, find and print all subsets of the array.
"""


def find_subsets(my_list):
    print "[ ]"

    def subsets(l):
        if not l:
            return
        else:
            print l
            subsets(l[1:])

    for i in range(len(my_list) + 1):
        subsets(my_list[:i])


arr = [1, 2, 3, 4, 5]
find_subsets(arr)

print pow(2, len(arr) - 1), "different subsets..."
