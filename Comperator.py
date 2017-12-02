"""
Comparators are used to compare two objects. In this challenge, you'll create
a comparator and use it to sort an array. The Player class is provided in the
editor below; it has two fields:

A string, .
An integer, .
Given an array of  Player objects, write a comparator that sorts them in order
of decreasing score; if  or more players have the same score, sort those players
alphabetically by name. To do this, you must create a Checker class that
implements the Comparator interface, then write an int compare(Player a, Player b)
method implementing the Comparator.compare(T o1, T o2) method.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return 'Player(name=%s, score=%s)' % (self.name, self.score)

    def comparator(self, b):
        if self.score > b.score:
            return -1
        elif b.score > self.score:
            return 1
        elif self.name > b.name:
            return 1
        else:
            return -1


n = 5
test_data = {"amy": 100, "david": 100, "heraldo": 50, "aakansha": 75, "aleksa": 150}
data = []
for k in test_data.keys():
    name, score = k, test_data[k]
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score
