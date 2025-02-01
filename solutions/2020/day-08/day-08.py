# advent of code 2020
# day 08

file = 'solutions/2020/day-08/input.txt'

class GameBoy:
    def __init__(self, instructions):
        self.instructions = instructions
        self.test_instructions = instructions.copy()

    def followInstructions(self):
        accumulator = 0
        pointer = 0
        executed_instructions = set()
        while pointer < len(self.test_instructions):
            if pointer in executed_instructions:
                return (accumulator, False)
            else:
              executed_instructions.add(pointer)
              operator, operand = self.test_instructions[pointer].split()
              if operator == 'nop':
                  pointer += 1
              elif operator == 'acc':
                  accumulator += int(operand)
                  pointer += 1
              else:
                  pointer += int(operand)
        return (accumulator, True)
    
    def testSubstitutions(self):
        for i in range(len(self.instructions)):
            self.test_instructions = self.instructions.copy()
            self.test_instructions[i] = self.test_instructions[i].replace('nop', 'x').replace('jmp', 'y').replace('x', 'jmp').replace('y', 'nop')
            acc, success = self.followInstructions()
            if success:
                return acc
            
def part_1(gameBoy):
    print('Part 1:', gameBoy.followInstructions()[0])

def part_2(gameBoy):
    print('Part 2:', gameBoy.testSubstitutions())

def main():
    instructions = open(file, 'r').read().splitlines()
    gameBoy = GameBoy(instructions)
    part_1(gameBoy)
    part_2(gameBoy)
    

if __name__ == '__main__':
    main()