# advent of code 2024
# day 02

file = 'input.txt'

class Report:
    def __init__(self, ints):
        self.report_values = ints

    def testReport(self, tryToFix=False):
        abs_diff = abs(self.report_values[1] - self.report_values[0])
        if abs_diff != 0:
            dir = (self.report_values[1] - self.report_values[0]) / abs_diff
            for i in range(len(self.report_values) - 1):
                abs_diff = abs(self.report_values[i + 1] - self.report_values[i])
                if abs_diff == 0 or abs_diff > 3:
                    break
                step_dir = (self.report_values[i + 1] - self.report_values[i]) / abs_diff
                if step_dir * dir == -1:
                    break
            else:
                return True
        if tryToFix:
            for i in range(len(self.report_values)):
                fixed_report = Report(self.report_values[:i] + self.report_values[i + 1:])
                if fixed_report.testReport():
                    return True
        return False

def part_1(reports):
    print('Part 1:', sum([report.testReport() for report in reports]))

def part_2(reports):
    print('Part 2:', sum([report.testReport(True) for report in reports]))

def main():
    reports = [Report([int(x) for x in line.split()]) for line in open(file, 'r').read().splitlines()]
    part_1(reports)
    part_2(reports)

if __name__ == '__main__':
    main()
