def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print (is_prime(5))
print (is_prime(4))
print (is_prime(15))
print (is_prime(13))

def sum_primes():
    res = 0
    prime_total = []
    for i in range(0, 1000):
        if is_prime(i):
            res += i
    return res



print (sum_primes())

