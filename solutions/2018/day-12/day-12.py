# advent of code 2018
# day 12

from collections import defaultdict

file = 'solutions/2018/day-12/input.txt'

class ConwayPlants:
    def __init__(self, pots, substitutions):
        self.pots = defaultdict(lambda: '.')
        for x in range(len(pots.split(': ')[1])):
            self.pots[x] = pots.split(': ')[1][x]
        self.substitutions = {substitution.split(' => ')[0]: substitution.split(' => ')[1] for substitution in substitutions.splitlines()}

    def simulatePlants(self, times, log=False):
        pots = self.pots.copy()
        end_time = None
        print_content = [(''.join([pots[key] for key in sorted(list(pots.keys()))]).strip('.'), min([key for key in pots.keys() if pots[key] == '#']), max([key for key in pots.keys() if pots[key] == '#']))]
        for t in range(1, times + 1):
            new_pots = defaultdict(lambda: '.')
            min_pot = min(pots.keys())
            max_pot = max(pots.keys())
            for pot in range(min_pot - 2, max_pot + 3):
                neighborhood = ''.join([pots[x] for x in range(pot - 2, pot + 3)])
                new_pots[pot] = self.substitutions[neighborhood] if neighborhood in self.substitutions else '.'
            pots = new_pots
            print_content.append((''.join([pots[key] for key in sorted(list(pots.keys()))]).strip('.'), min([key for key in pots.keys() if pots[key] == '#']), max([key for key in pots.keys() if pots[key] == '#'])))
            if all([sum([pots[n] == '#' for n in range(x - 2, x + 3)]) <= 1 for x in range(min(pots), max(pots) + 1)]):
                print_content.append(('', 0, 0))
                print_content.append(('...stability achieved...', 0, 0))
                print_content.append(('', 0, 0))
                end_time = t
                break
        if log:
            min_index = min([m for _1, m, _2 in print_content]) - 1
            max_index = max([m for _1, _2, m in print_content]) + 1
            for d in range(len(str(max_index))):
                print('    ' + ''.join([str(i).rjust(len(str(max_index)), ' ')[d] if i % 10 == 0 else ' ' for i in range(min_index, max_index + 1)]))
            print('\n'.join([(str(i) + ':').ljust(len(str(times)) + 2, ' ') + '.' * (print_content[i][1] - min_index) + print_content[i][0] + '.' * (max_index - print_content[i][2]) for i in range(len(print_content))]))
        if end_time is not None:
            return sum(pot for pot in pots if pots[pot] == '#') + (times - end_time) * list(pots.values()).count('#')
        return sum(pot for pot in pots if pots[pot] == '#')
    
def part_1(conwayPlants):
    print('Part 1:', conwayPlants.simulatePlants(20))

def part_2(conwayPlants):
    print('Part 2:', conwayPlants.simulatePlants(50000000000))


def main():
    pots, substitutions = open(file, 'r').read().split('\n\n')
    conwayPlants = ConwayPlants(pots, substitutions)
    part_1(conwayPlants)
    part_2(conwayPlants)

if __name__ == '__main__':
    main()