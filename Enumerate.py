from pprint import pprint

my_list = ["apple", "banana", "grapes", "watermelon", "lemon"]
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
print list(enumerate(my_list, 1))

pprint(my_list)

for c, item in enumerate(my_list, 1):
    print c, item
