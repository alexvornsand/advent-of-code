# advent of code 2020
# day 06

file = 'solutions/2020/day-06/input.txt'

class DeclarationsReport:
    def __init__(self, declaration_sheets):
        self.declaration_sheets = declaration_sheets

    def declarationsUnion(self):
        items = set(self.declaration_sheets[0])
        for sheet in self.declaration_sheets[1:]:
            items.update(set(sheet))
        return len(items)

    def declarationsIntersection(self):
        items = set(self.declaration_sheets[0])
        for sheet in self.declaration_sheets[1:]:
            items.intersection_update(set(sheet))
        return len(items)

def part_1(reports):
    print('Part 1:', sum(DeclarationsReport(report).declarationsUnion() for report in reports))

def part_2(reports):
    print('Part 2:', sum(DeclarationsReport(report).declarationsIntersection() for report in reports))

def main():
    reports = [[[item for item in sheet] for sheet in report.splitlines()] for report in open(file, 'r').read().split('\n\n')]
    part_1(reports)
    part_2(reports)

if __name__ == '__main__':
    main()