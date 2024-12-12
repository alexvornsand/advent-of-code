# advent of code 2024
# day 07

from functools import cache

file = 'input.txt'

class Manual:
    def __init__(self, equations):
        self.equations = equations

    @cache
    def testEquation(self, equation, simple=True):
        value, expression = equation
        expression = list(expression)
        if len(expression) == 1:
            if value[0] == expression[0]:
                return int(value[0])
            else:
                return 0
        else:
            a = expression.pop(0)
            b = expression.pop(0)
            operators = ['+', '*'] if simple else ['+', '*', '']
            for operator in operators:
                new_term = str(eval(a + operator + b))
                if int(new_term) <= int(value[0]):
                    new_equation = tuple([value, tuple([new_term] + expression)])
                    if self.testEquation(new_equation, simple) != 0:
                        return int(value[0])
            return 0
        
    def callibrateEquationsSimple(self):
        return sum([self.testEquation(equation,) for equation in self.equations])

    def callibrateEquationsHard(self):
        return sum([self.testEquation(equation, False) for equation in self.equations])


def part_1(manual):
    print('Part 1:', manual.callibrateEquationsSimple())

def part_2(manual):
    print('Part 2:', manual.callibrateEquationsHard())

def main():
    equations = [tuple([tuple(x.split()) for x in line.split(':')]) for line in open(file, 'r').read().splitlines()]
    manual = Manual(equations)
    part_1(manual)
    part_2(manual)

if __name__ == '__main__':
    main()