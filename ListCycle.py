class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def detect_cycle(l):
    slow = l
    fast = l
    while slow is not None:
        slow = slow.next
        if slow is None:
            return False
        if fast is not None:
            fast = fast.next
        if fast is not None and fast.next is not None:
            fast = fast.next.next
        if slow is fast:
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

