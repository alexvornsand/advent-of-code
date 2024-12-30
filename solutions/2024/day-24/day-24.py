# advent of code
# day 24

file = 'input.txt'

class GateNetwork:
    def __init__(self, initial_values, gates):
        self.nodes = {node: value for node, value in [initial_value.split(': ') for initial_value in initial_values]}
        self.gates = gates

    def fillNetwork(self):
        logical_gates = {
            'XOR': '^',
            'OR': '|',
            'AND': '&'
        }
        while len(self.gates) > 0:
            gate = self.gates.pop(0)
            a, logic, b, _, c = gate.split(' ')
            if a in self.nodes and b in self.nodes:
                if c not in self.nodes:
                    self.nodes[c] = eval(str(self.odes[a]) + logical_gates[logic] + str(self.nodes[b]))
            else:
                self.gates.append(gate)

    def getNetworkValue(self):
        filled_nodes = self.fillNetwork()
        return int(''.join([str(filled_nodes[x]) for x in sorted(filled_nodes.keys(), reverse=True) if x[0] == 'z']), 2)
    
    def findBrokenGates(self):
        broken_gates = []
        for gate in self.gates:
            a, logic, b, _, c = gate.split(' ')
            if c[0] == 'z' and int(c[1:]) != 0 and int(c[1:]) != 45:
                if logic != 'XOR':
                    broken_gates.append(c)
            elif c[0] != 'z' and (a[0] not in ('x', 'y') and b[0] not in ('x', 'y')):
                if logic == 'XOR':
                    broken_gates.append(c)
            elif a[0] in ('x', 'y') and b[0] in ('x', 'y') and int(a[1:]) != 0 and int(b[1:]) != 0 and logic == 'XOR':
                if not any([c + ' XOR' in gate2 or 'XOR ' + c in gate2 for gate2 in self.gates]):
                    broken_gates.append(c)
            elif logic == 'AND':
                if not any([c + ' OR' in gate2 or 'OR ' + c in gate2 for gate2 in self.gates]):
                    broken_gates.append(c)
        return(','.join(sorted(broken_gates)))

def part_1(gateNetwork):
    print('Part 1:', gateNetwork.getNetworkValue())

def part_2(gateNetwork):
    print('Part 2:', gateNetwork.findBrokenGates())

def main():
    initial_values, gates = [section.splitlines() for section in open(file, 'r').read().split('\n\n')]
    gateNetwork = GateNetwork(initial_values, gates)
    part_1(gateNetwork)
    part_2(gateNetwork)

if __name__ == '__main__':
    main()