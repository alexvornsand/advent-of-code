# advent of code 2020
# day 01

file = 'solutions/2020/day-01/input.txt'

class ExpenseReport:
    def __init__(self, expenses):
        self.expenses = expenses

    def findMatchedPair(self):
        return sum([self.expenses[i] * self.expenses[j] for i in range(len(self.expenses) - 1) for j in range(i, len(self.expenses)) if self.expenses[i] + self.expenses[j] == 2020])

    def findMatchedThrouple(self):
        return sum([self.expenses[i] * self.expenses[j] * self.expenses[k] for i in range(len(self.expenses) - 2) for j in range(i, len(self.expenses) - 1) for k in range(j, len(self.expenses)) if self.expenses[i] + self.expenses[j] + self.expenses[k] == 2020])

def part_1(expenseReport):
    print('Part 1:', expenseReport.findMatchedPair())

def part_2(expenseReport):
    print('Part 2:', expenseReport.findMatchedThrouple())

def main():
    expenses = [int(x) for x in open(file, 'r').read().splitlines()]
    expenseReport = ExpenseReport(expenses)
    part_1(expenseReport)
    part_2(expenseReport)

if __name__ == '__main__':
    main()