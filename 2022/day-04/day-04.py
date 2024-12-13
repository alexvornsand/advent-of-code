# advent of code 2022
# day 4

# part 1
assignments = [a.split(',') for a in open('input.txt', 'r').read().split('\n')[:-1]]

def countOverlaps(assignments, partTwo=False):
    return(sum([1 if len(r1.intersection(r2)) >= (min(len(r1), len(r2)) if partTwo is False else 1) else 0 for r1, r2 in [[set(list(range(int(section.split('-')[0]), int(section.split('-')[1]) + 1))) for section in pair] for pair in assignments]]))

countOverlaps(assignments)

# part 2
countOverlaps(assignments, True)
