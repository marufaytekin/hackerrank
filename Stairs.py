"""
Davis has  staircases in his house and he likes to climb each staircase 
1,2 , or 3 steps at a time. Being a very precocious child, he wonders how
many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, 
find and print the number of ways he can climb each staircase on a new line.
"""


def climb(n):
    """
    recursive 
    :param n: number of stairs
    :return: number of different ways to climb
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return climb(n - 1) + climb(n - 2) + climb(n - 3)


def climb2(steps):
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


print(climb(1))
print(climb(3))
print(climb(10))

print(climb2(3))
print(climb2(10))
