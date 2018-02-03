"""
Given n strings of brackets, determine whether each sequence of brackets is
balanced.
"""


def is_matched(expression):
    l = list(expression)
    s = []
    for e in l:
        if e is '[':
            s.append(e)
        if e is ']':
            if s.pop() is not '[':
                return False
        if e is '{':
            s.append(e)
        if e is '}':
            if s.pop() is not '{':
                return False
        if e is '(':
            s.append(e)
        if e is ')':
            if s.pop() is not '(':
                return False
    return len(s) == 0


print is_matched("{{[[(())]]}}")
print is_matched("{{[[(())]]}]")
