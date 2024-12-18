# advent of code 2022
# day 3

# part 1
napsacks = [(n[:int(1/2 * len(n))], n[int(1/2 * len(n)):]) for n in open('input.txt', 'r').read().split('\n')[:-1]]

def countPriority(napsacks, partTwo=False):
    alphaIndex = [chr(x) for x in range(97,123)] + [chr(x) for x in range(65,91)]
    if partTwo is False:
        return(sum([alphaIndex.index(list(set(n[0]).intersection(n[1]))[0]) + 1 for n in napsacks]))
    else:
        return(sum([alphaIndex.index(list(set(''.join(napsacks[3 * i])).intersection(''.join(napsacks[3 * i + 1])).intersection(''.join(napsacks[3 * i + 2])))[0]) + 1 for i in range(int(len(napsacks) / 3))]))

countPriority(napsacks)

# part 2
countPriority(napsacks, True)