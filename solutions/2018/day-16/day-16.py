# advent of code 2018
# day 16

import re

file = 'solutions/2018/day-16/input.txt'

class OpcodeComputer:
    def __init__(self, scenarios, code):
        self.scenarios = scenarios
        self.code = code
        self.registers = [None] * 4
        self.opids = {i: set([
            'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
            'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
        ]) for i in range(16)}

    def processOpcode(self, op, a, b, c, log=False, indent=0):
        if op == 'addr':
            if log:
                print(
                    '\t' * indent, 'addr: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') + register', b, 
                    ' (', self.registers[b], ') = ', 
                    self.registers[a] + self.registers[b], sep=''
                )
            self.registers[c] = self.registers[a] + self.registers[b]
        elif op == 'addi':
            if log:
                print(
                    '\t' * indent, 'addi: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') + immediate', b, 
                    ' (', b, ') = ', self.registers[a] + b, sep=''
                )
            self.registers[c] = self.registers[a] + b
        elif op == 'mulr':
            if log:
                print(
                    '\t' * indent, 'mulr: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') * register', b, ' (', 
                    self.registers[b], ') = ', 
                    self.registers[a] * self.registers[b], sep=''
                )
            self.registers[c] = self.registers[a] * self.registers[b]
        elif op == 'muli':
            if log:
                print(
                    '\t' * indent, 'muli: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') * immediate', b, 
                    ' (', b, ') = ', self.registers[a] * b, sep=''
                )
            self.registers[c] = self.registers[a] * b
        elif op == 'banr':
            if log:
                print(
                    '\t' * indent, 'banr: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') AND register', b, ' (', 
                    self.registers[b], ') = ', 
                    self.registers[a] & self.registers[b], sep=''
                )
            self.registers[c] = self.registers[a] & self.registers[b]
        elif op == 'bani':
            if log:
                print(
                    '\t' * indent, 'bani: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') AND immediate', b, ' (', b, 
                    ') = ', self.registers[a] & b, sep=''
                )
            self.registers[c] = self.registers[a] & b
        elif op == 'borr':
            if log:
                print(
                    '\t' * indent, 'borr: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') OR register', b, ' (', 
                    self.registers[b], ') = ', 
                    self.registers[a] | self.registers[b], sep=''
                )
            self.registers[c] = self.registers[a] | self.registers[b]
        elif op == 'bori':
            if log:
                print(
                    '\t' * indent, 'bori: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') OR immediate', b, ' (', b, 
                    ') = ', self.registers[a] | b, sep=''
                )
            self.registers[c] = self.registers[a] | b
        elif op == 'setr':
            if log:
                print(
                    '\t' * indent, 'setr: register ', c, ' = register ', a, 
                    ' (', self.registers[a], ') = ', self.registers[a], sep=''
                )
            self.registers[c] = self.registers[a]
        elif op == 'seti':
            if log:
                print(
                    '\t' * indent, 'seti: register ', c, ' = immediate ', a, 
                    ' (', a, ') = ', a, sep=''
                )
            self.registers[c] = a
        elif op == 'gtir':
            if log:
                print(
                    '\t' * indent, 'gtir: register ', c, ' = 1 if immediate', a,
                    ' (', a, ') > register ', b, ' (', 
                    self.registers[b], ') else 0 = ', 
                    1 if a > self.registers[b] else 0, sep=''
                )
            self.registers[c] = 1 if a > self.registers[b] else 0
        elif op == 'gtri':
            if log:
                print(
                    '\t' * indent, 'gtri: register ', c, ' = 1 if register', a, 
                    ' (', self.registers[a], ') > immediate ', b, 
                    ' (', b, ') else 0 = ', 1 if self.registers[a] > b else 0, 
                    sep=''
                )
            self.registers[c] = 1 if self.registers[a] > b else 0
        elif op == 'gtrr':
            if log:
                print(
                    '\t' * indent, 'gtrr: register ', c, ' = 1 if register', a, 
                    ' (', self.registers[a], ') > register ', b, ' (', 
                    self.registers[b], ') else 0 = ', 
                    1 if self.registers[a] > self.registers[b] else 0, sep=''
                )
            self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0
        elif op == 'eqir':
            if log:
                print(
                    '\t' * indent, 'eqir: register ', c, ' = 1 if immediate', a, 
                    ' (', a, ') == register ', b, ' (', self.registers[b], 
                    ') else 0 = ', 1 if a == self.registers[b] else 0, sep=''
                )
            self.registers[c] = 1 if a == self.registers[b] else 0
        elif op == 'eqri':
            if log:
                print(
                    '\t' * indent, 'eqri: register ', c, ' = 1 if register', a, 
                    ' (', self.registers[a], ') == immediate ', b, ' (', b, 
                    ') else 0 = ', 1 if self.registers[a] == b else 0, sep=''
                )
            self.registers[c] = 1 if self.registers[a] == b else 0
        elif op == 'eqrr':
            if log:
                print(
                    '\t' * indent, 'eqrr: register ', c, ' = 1 if register', a, 
                    ' (', self.registers[a], ') == register ', b, 
                    ' (', self.registers[b], ') else 0 = ', 
                    1 if self.registers[a] == self.registers[b] else 0, sep=''
                )
            self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0

    def testScenario(self, scenario, log=False):
        register_inputs, [opid, a, b, c], register_outputs = scenario
        possible_opcodes = []
        for op in [
            'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
            'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
        ]:
            self.registers = register_inputs.copy()
            self.processOpcode(op, a, b, c, log=log, indent=1)
            if self.registers == register_outputs:
                if log:
                    print('\t\tgood code!')
                possible_opcodes.append(op)
        self.opids[opid].intersection_update(set(possible_opcodes))
        return possible_opcodes

    def testScenarios(self, log=False):
        return sum([len(self.testScenario(scenario, log=log)) >= 3 for scenario in self.scenarios])

    def deduceCodes(self):        
        while any([isinstance(value, set) for value in self.opids.values()]):
            for opid in self.opids:
                if len(self.opids[opid]) == 1:
                    self.opids[opid] = list(self.opids[opid])[0]
                    for other in self.opids:
                        if isinstance(self.opids[other], set):
                            self.opids[other].discard(self.opids[opid])

    def runProgram(self):
        self.registers = [0] * 4
        for line in self.code:
            opid, a, b, c = line
            self.processOpcode(self.opids[opid], a, b, c)
        return self.registers[0]

def part_1(opcodeComputer):
    print('Part 1:', opcodeComputer.testScenarios())

def part_2(opcodeComputer):
    print('Part 2:', opcodeComputer.runProgram())

def main():
    scenarios, code = open(file, 'r').read().split('\n\n\n')
    scenarios = [[[int(x) for x in re.findall(r'\d+', scenario_line)] for scenario_line in scenario.splitlines()] for scenario in scenarios.split('\n\n')]
    code = [[int(x) for x in re.findall(r'\d+', line)] for line in code.strip().splitlines()]
    opcodeComputer = OpcodeComputer(scenarios, code)
    part_1(opcodeComputer)
    opcodeComputer.deduceCodes()
    part_2(opcodeComputer)

if __name__ == '__main__':
    main()