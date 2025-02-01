# advent of code 2018
# day 08

import uuid
from functools import cache

file = 'solutions/2018/day-08/input.txt'

class Tree:
    def __init__(self, license):
        self.license = license.copy()
        self.nodes = {}

    def navigateTree(self, childOf=None, log=False, depth=0):
        indent = '\t' * depth
        n_children = self.license.pop(0)
        n_metadata = self.license.pop(0)
        id = uuid.uuid4().hex
        if log:
            print(indent, 'unpacking node ', id, ' (', n_children, ' children; ', n_metadata, ' metadata entries)', sep='')
        self.nodes[id] = {}
        self.nodes[id]['parent'] = childOf
        self.nodes[id]['children'] = []
        for _ in range(n_children):
            self.nodes[id]['children'].append(self.navigateTree(childOf=id, log=log, depth=depth+1))
        self.nodes[id]['metadata'] = self.license[:n_metadata]
        self.license = self.license[n_metadata:]
        return id

    def totalMetadata(self):
        return sum([sum(self.nodes[node]['metadata']) for node in self.nodes])
    
    @cache
    def totalNestedValue(self, node=None):
        if node is None:
            node = list(self.nodes.keys())[0]
        if len(self.nodes[node]['children']) == 0:
            return sum(self.nodes[node]['metadata'])
        else:
            return sum([self.totalNestedValue(self.nodes[node]['children'][index - 1]) for index in self.nodes[node]['metadata'] if index - 1 < len(self.nodes[node]['children'])])

def part_1(tree):
    print('Part 1:', tree.totalMetadata())

def part_2(tree):
    print('Part 2:', tree.totalNestedValue())

def main():
    license = [int(x) for x in open(file, 'r').read().split()]
    tree = Tree(license)
    tree.navigateTree()
    part_1(tree)
    part_2(tree)

if __name__ == '__main__':
    main()