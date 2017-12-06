variable = 5


def func():
    variable = 7
    print(variable)


func()
print(variable)


def func2():
    global variable
    variable = 8


func2()
print(variable)
