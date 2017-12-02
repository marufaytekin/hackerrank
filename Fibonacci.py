# Recursive
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Tail Recursive
def fibonacci_tr(n, a, b):
    print a, b
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_tr(n - 1, b, a + b)


k = 10
print(fibonacci(k))

print(fibonacci_tr(k, 0, 1))
