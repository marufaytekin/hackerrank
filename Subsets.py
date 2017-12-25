"""
Find and print all subsets of a given set! (Given as an array.)
"""


def find_subsets(my_list):
    def subsets(l):
        if l == []:
            return
        else:
            print l
            subsets(l[1:])
    for i in range(len(my_list) + 1):
        subsets(my_list[:i])


l = [1, 2, 3, 4, 5]
find_subsets(l)
