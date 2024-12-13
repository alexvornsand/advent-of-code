# advent of code 2024
# day 05

file = 'input.txt'

class PrintOrders:
    def __init__(self, rules, prints):
        self.rules = rules
        self.prints = prints
        self.wellOrderedPrints = []
        self.correctedPrints = []

    def fixPrint(self, print):
        head = []
        tail = []
        local_rules = []
        for a, b in self.rules:
            if a in print and b in print:
                local_rules.append([a, b])
        while len(local_rules) > 0:
            a_pages = set([])
            b_pages = set([])
            for a, b in local_rules:
                a_pages.add(a)
                b_pages.add(b)
            header =list(a_pages.difference(b_pages))[0]
            footer = list(b_pages.difference(a_pages))[0]
            head.append(header)
            tail.append(footer)
            a_pages.remove(header)
            b_pages.remove(footer)
            local_rules = [[a, b] for a, b in local_rules if a != header and b != footer]
            if len(a_pages) == 1:
                head.append(list(a_pages)[0])
        return head + tail[::-1]
    
    def evaluatePrints(self):
        for print in self.prints:
            for a, b in self.rules:
                if a in print and b in print:
                    if print.index(a) > print.index(b):
                        self.correctedPrints.append(self.fixPrint(print))
                        break
            else:
                self.wellOrderedPrints.append(print)

def part_1(printOrders):
    print('Part 1:', sum([print[int((len(print) - 1) / 2)] for print in printOrders.wellOrderedPrints]))

def part_2(printOrders):
    print('Part 2:', sum([print[int((len(print) - 1) / 2)] for print in printOrders.correctedPrints]))

def main():
    rules, prints = [[eval(x) for x in x.splitlines()] for x in open(file, 'r').read().replace('|', ',').split('\n\n')]
    printOrders = PrintOrders(rules, prints)
    printOrders.evaluatePrints()
    part_1(printOrders)
    part_2(printOrders)

if __name__ == '__main__':
    main()