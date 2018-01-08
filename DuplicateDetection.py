import collections


def remove_duplicate(s):
    """
    O (n^2)
    """
    a = []
    for c in s:
        if c not in a:
            a.append(c)
    return ''.join(a)


def remove_duplicate2(s):
    """
    O (n)
    """
    a = collections.OrderedDict()
    for c in s:
        if c not in a:
            a[c] = c
    return ''.join(a.keys())

print remove_duplicate("asdsdsdsdffff")
print remove_duplicate("aaaaaaaaaa")
print remove_duplicate("test1")
print remove_duplicate("aaaaaamnkbbbbmmmm")
print
print remove_duplicate2("asdsdsdsdffff")
print remove_duplicate2("aaaaaaaaaa")
print remove_duplicate2("test2")
print remove_duplicate2("aaaaaamnkbbbbmmmm")
