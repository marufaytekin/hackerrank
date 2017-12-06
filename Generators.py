# A list comprehension

print max([num ** 2 for num in range(7)])

# A generator expression
print max(num ** 2 for num in range(7))


# A generator function
def genfunc(endfunc):
    num = 0
    while True:
        if endfunc(num):
            return
        yield num
        num = num + 1


def endfn(number):
    if number == 7:
        return True
    return False


print "Iterate over generator function"
for n in genfunc(endfn):
    print n
