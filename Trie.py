class Node:
    def __init__(self):
        self.key = None
        self.data = 0
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        curr_node = self.root
        for c in key:
            if c not in curr_node.children.keys():
                curr_node.children[c] = Node()
            curr_node = curr_node.children[c]
        curr_node.key = key

    def search(self, key):
        curr_node = self.root
        depth = -1
        for c in key:
            if c not in curr_node.children.keys():
                return False, 0
            curr_node = curr_node.children[c]
            depth += 1
        return curr_node, depth


t = Trie()

f = open('test.txt', 'r')
o = open('output07.txt', 'r')

file = f.read().split('\n')
output = o.read().split('\n')

for line, res in zip(file, output):
    op, contact = line.strip().split(' ')
    print(line, res)
    if op == 'add':
        t.insert(contact)
    if op == 'find':
        target, level = t.search(contact)
        print(target, level)
        if target is False:
            assert int(res) == level
        else:
            if target.key is None:
                assert int(res) == 0
            else:
                assert int(res) == level
