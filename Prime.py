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
    for i in range(0, 1000):
        if is_prime(i):
            res += i
    return res


print (sum_primes())


def is_prime_generator(my_list):
    for num in my_list:
        if is_prime(num):
            yield num
        num += 1

prime_list = is_prime_generator(range(2, 20))

for item in prime_list:
    print item
