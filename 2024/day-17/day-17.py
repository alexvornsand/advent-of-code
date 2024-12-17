# advent of code 2024
# day 17

import re

file = 'input.txt'

class Computer:
    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.pointer = 0
        self.combo_operands = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: A,
            5: B,
            6: C
        }
        self.output = []
    
    def resetMemory(self):
        self.pointer = 0
        self.combo_operands[4] = self.A
        self.combo_operands[5] = self.B
        self.combo_operands[6] = self.C
        self.output = []

    def adv(self, operand, log=False):
        if log:
            print('\t\tsetting register A to', self.combo_operands[4], '// 2 ^', self.combo_operands[operand])
        self.combo_operands[4] = self.combo_operands[4] // (2 ** self.combo_operands[operand])
        if log:
            print('\t\t\tregister A:', self.combo_operands[4])

    def bxl(self, operand, log=False):
        if log:
            print('\t\tsetting register B to', self.combo_operands[5], '^', operand)
        self.combo_operands[5] = self.combo_operands[5] ^ operand
        if log:
            print('\t\t\tregister B:', self.combo_operands[5])

    def bst(self, operand, log=False):
        if log:
            print('\t\tsetting register B to', self.combo_operands[operand], '%', 8)
        self.combo_operands[5] = self.combo_operands[operand] % 8
        if log:
            print('\t\t\tregister B:', self.combo_operands[5])
    
    def jnx(self, operand, log=False):
        if self.combo_operands[4] != 0:
            if log:
                print('\t\tregister A is not 0 so jumping pointer to', operand)
            self.pointer = operand
            if log:
                print('\t\t\tpointer:', self.pointer)
            return True
        else:
            if log:
                print('\t\tregister A is 0 -- do nothing')
            return False

    def bxc(self, log=False):
        if log:
            print('\t\tsetting register B to', self.combo_operands[5], '^', self.combo_operands[6])
        self.combo_operands[5] = self.combo_operands[5] ^ self.combo_operands[6]
        if log:
            print('\t\t\tregister B:', self.combo_operands[5])

    def out(self, operand, log=False):
        if log:
            print('\t\tadding', self.combo_operands[operand], '%', 8, 'to the output')
        self.output.append(self.combo_operands[operand] % 8)
        if log:
            print('\t\t\toutput:', self.output)

    def bdv(self, operand, log=False):
        if log:
            print('\t\tsetting register B to', self.combo_operands[4], '// 2 ^', self.combo_operands[operand])
        self.combo_operands[5] = self.combo_operands[4] // (2 ** self.combo_operands[operand])
        if log:
            print('\t\t\tregister 5:', self.combo_operands[5])

    def cdv(self, operand, log=False):
        if log:
            print('\t\tsetting register C to', self.combo_operands[4], '// 2 ^', self.combo_operands[operand])
        self.combo_operands[6] = self.combo_operands[4] // (2 ** self.combo_operands[operand])
        if log:
            print('\t\t\tregister C:', self.combo_operands[6])

    def processInstruction(self, log=False):
        if log:
            print('pointer:', self.pointer)
            print('registers:', oct(self.combo_operands[4]), self.combo_operands[5], self.combo_operands[6])
        if self.pointer >= len(self.program):
            if log:
                print('\tpointer out of range -- program terminated')
            return False
        else:
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            if log:
                print('\topcode:', opcode)
                print('\toperand:', operand)
            if opcode == 0:
                self.adv(operand, log)
                self.pointer += 2
            elif opcode == 1:
                self.bxl(operand, log)
                self.pointer += 2
            elif opcode == 2:
                self.bst(operand, log)
                self.pointer += 2
            elif opcode == 3:
                if not self.jnx(operand, log):
                    self.pointer += 2
            elif opcode == 4:
                self.bxc(log)
                self.pointer += 2
            elif opcode == 5:
                self.out(operand, log)
                self.pointer += 2
            elif opcode == 6:
                self.bdv(operand, log)
                self.pointer += 2
            elif opcode == 7:
                self.cdv(operand, log)
                self.pointer += 2
            return True

    def runProgram(self, reset=True, log=False):
        if reset:
            self.resetMemory()
        running = True
        while running:
            running = self.processInstruction(log)
        return ','.join([str(x) for x in self.output])
    
    def findNextValue(self, seq, log=False):
        if len(seq) == 16:
            return int(seq, 8)
        for i in range(8):
            test_seq = seq + str(i)
            target_digit = len(test_seq)
            if log:                
                print('\t' * len(test_seq), 'testing ', test_seq.ljust(16, '0'), ' (', int(test_seq.ljust(16, '0'), 8), ')', sep='')
            test_a = int(test_seq.ljust(16, '0'), 8)
            self.resetMemory()
            self.combo_operands[4] = test_a
            self.runProgram(reset=False)
            if self.program[-target_digit] == self.output[-target_digit]:
                if log:
                    print('\t' * (len(test_seq) + 1), 'digit successful!', sep='')
                    print('\t' * (len(test_seq) + 2), test_seq)
                result =  self.findNextValue(test_seq, log)
                if result:
                    return result
            if log:
                print('\t' * (len(test_seq) + 1), 'digit failed!', sep='')
                print('\t' * (len(test_seq) + 2), 'intended output was:', sep='')
                print('\t' * (len(test_seq) + 3), self.program, sep='')
                print('\t' * (len(test_seq) + 2), 'actual output was:', sep='')
                print('\t' * (len(test_seq) + 3), self.output, sep='')
            
    def findMinimumA(self, log=False):
        return self.findNextValue('', log)

def part_1(computer):
    print('Part 1:', computer.runProgram())

def part_2(computer):
    print('Part 2:', computer.findMinimumA())

def main():
    registers, instructions = open(file, 'r').read().split('\n\n')
    A, B, C = [int(re.findall(r'\d+', x)[0]) for x in registers.splitlines()]
    program = list(eval(instructions.split(': ')[1]))
    computer = Computer(A, B, C, program)
    part_1(computer)
    part_2(computer)

if __name__ == '__main__':
    main()