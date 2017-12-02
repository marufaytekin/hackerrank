"""
Google Interview Question:
How would you search a broken commit if you have changes as a range between a and b.
"""


def build(a, b):
    if a < 21 and b > 20:
        return False
    if a == b:
        return False
    return True


def search(start, end):
    print "processing revs: ", start, end
    if start == end:
        return start
    if not build(start, (start + end) / 2):
        return search(start, (start + end) / 2)
    elif not build((start + end) / 2, end):
        return search((start + end) / 2, end)
    else:
        return None


print search(11, 100)
