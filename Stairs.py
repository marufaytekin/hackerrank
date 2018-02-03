"""
Davis has  staircases in his house and he likes to climb each staircase 
1,2 , or 3 steps at a time. Being a very precocious child, he wonders how
many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, 
find and print the number of ways he can climb each staircase on a new line.
"""


def climb(steps):
    """
    iterative
    """
    if steps < 0:
        return 0
    if steps <= 1:
        return 1
    paths = []
    paths.insert(0, 1)
    paths.insert(1, 1)
    paths.insert(2, 2)
    for i in range(3, steps+1):
        paths.insert(i, paths[i-1] + paths[i-2] + paths[i-3])
    return paths[steps]


def clim_r(n):
    """
    recursive
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return clim_r(n - 1) + clim_r(n - 2) + clim_r(n - 3)


print(climb(1))
print(climb(3))
print(climb(10))

print(clim_r(1))
print(clim_r(3))
print(clim_r(10))
