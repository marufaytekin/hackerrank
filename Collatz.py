"""
The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
start with any positive integer n.
Then each term is obtained from the previous term as follows:
   if the previous term is even, the next term is one half the previous term.
Otherwise, the next term is 3 times the previous term plus 1.
The conjecture is that no matter what value of n, the sequence will always reach 1.
"""


def collatz(num, l):
    l.append(num)
    if num == 1:
        return
    elif num % 2 == 0:
        curr = num / 2
        collatz(curr, l)
    else:
        curr = 3 * num + 1
        collatz(curr, l)

l = []
collatz(12, l)
print l
