# advent of code 2022
# day 2

# part 1
rounds = [r.split(' ') for r in open('input.txt', 'r').read().split('\n')[:-1]]

def scoreRounds(rounds, partTwo=False):
    intMap = {
        'A':1,
        'B':2,
        'C':3,
        'X':1,
        'Y':2,
        'Z':3
    }
    if partTwo is False:
        return(sum([intMap[round[1]] + 3 * ((intMap[round[1]] - intMap[round[0]] + 1) % 3) for round in rounds]))
    else: 
        return(sum([(3 * intMap[round[1]]) + ((intMap[round[0]] + intMap[round[1]]) % 3) - 2 for round in rounds]))

scoreRounds(rounds)

# part 2
scoreRounds(rounds, True)
