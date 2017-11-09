

s1 = []
s2 = []


def push(val):
    s1.insert(0, val)

def pop():
    if len(s2) == 0:
        while len(s1) != 0:
            s2.insert(0, s1.pop(0))
    return s2.pop(0)

l = [1,2,3,4]

for i in l:
    push(i)

print(s1)
print(pop())

print(s1)
print(s2)
print(pop())
print(pop())
print(pop())



