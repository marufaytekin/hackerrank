"""
I saw this on Quora as an interesting sorting algorithm.
"""


from multiprocessing import Pool
from time import sleep


def sleep_sort(item):
    sleep(item)
    print item

l = [8, 5, 3, 1, 2]


Pool(processes=len(l)).map(sleep_sort, l)

