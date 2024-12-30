# advent of code 2024
# day 23

import networkx as nx

file = 'input.txt'

class LAN:
    def __init__(self, edges):
        self.graph = nx.Graph()
        for edge in edges:
            a, b = edge.split('-')
            if a not in self.graph:
                self.graph.add_node(a)
            if b not in self.graph:
                self.graph.add_node(b)
            self.graph.add_edge(a, b)
        
    def evaluateGraph(self):
        self.cliques = list(nx.enumerate_all_cliques(self.graph))

    def countThrouples(self):
        return len([clique for clique in self.cliques if len(clique) == 3 and any([member[0] == 't' for member in clique])])
    
    def getPassword(self):
        return ','.join(sorted([clique for clique in self.cliques if len(clique) == max([len(clique) for clique in self.cliques])][0]))

def part_1(lan):
    print('Part 1:', lan.countThrouples())

def part_2(lan):
    print('Part 2:', lan.getPassword())

def main():
    edges = open(file, 'r').read().splitlines()
    lan = LAN(edges)
    lan.evaluateGraph()
    part_1(lan)
    part_2(lan)

if __name__ == '__main__':
    main()