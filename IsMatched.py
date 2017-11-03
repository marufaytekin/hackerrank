"""
Given n strings of brackets, determine whether each sequence of brackets is
balanced. If a string is balanced, print YES on a new line; otherwise, print
NO on a new line.
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


t = 1
for a0 in xrange(t):
    expression = "{{[[(())]]}}"
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
