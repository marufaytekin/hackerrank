def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci2(n, a, b):
    #print(a, b)
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci2(n-1, b, a+b)

print(fibonacci(0), fibonacci2(0, 0, 1))
print(fibonacci(1), fibonacci2(1, 0, 1))
print(fibonacci(2), fibonacci2(2, 0, 1))
print(fibonacci(3), fibonacci2(3, 0, 1))
print(fibonacci(5), fibonacci2(5, 0, 1))
print(fibonacci(10), fibonacci2(10, 0, 1))
print(fibonacci(25), fibonacci2(25, 0, 1))

