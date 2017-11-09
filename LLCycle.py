class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def detect_cycle(l):
    s = l
    f = l
    while s is not None:
        s = s.next
        if s is None:
            return False
        if f is not None:
            f = f.next
        if f is not None and f.next is not None:
            f = f.next.next
        if s is f:
            return True


h = LLNode(-99)
a = h
for i in range(10):
    h.next = LLNode(i)
    h = h.next
    if i is 6:
        b = h

# This line creates the cycle
h.next = b

print(detect_cycle(a))

for i in range(10):
    print(a.value)
    a = a.next

