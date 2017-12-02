def collatz(num, count):
    if num == 1:
        return count
    elif num % 2 == 0:
        return collatz(num / 2, count + 1)
    else:
        return collatz(3 * num + 1, count + 1)

print collatz(100, 0)
