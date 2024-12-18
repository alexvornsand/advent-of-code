# advent of code 2015
# day 16

# part 1
input = open('day-16.txt', 'r').read()

def identifyAuntSue(input, partTwo = False):
    auntSues = {}
    for a in input.split('\n'):
        auntSues[int(a.split(' ')[1].replace(':', ''))] = {}
        for i in range(1, int(len(a.split(' ')) / 2)):
            auntSues[int(a.split(' ')[1].replace(':', ''))][a.split(' ')[2 * i].replace(':', '')] = int(a.split(' ')[(2 * i) + 1].replace(',', ''))
    mysterySue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    for sue in auntSues.keys():
        legitSue = True
        for key in mysterySue.keys():
            if partTwo == True and (key == 'cats' or key == 'trees'):
                if key in auntSues[sue].keys():
                    if mysterySue[key] >= auntSues[sue][key]:
                        legitSue = False
                        break
            elif partTwo == True and (key == 'pomeranians' or key == 'goldfish'):
                if key in auntSues[sue].keys():
                    if mysterySue[key] <= auntSues[sue][key]:
                        legitSue = False
                        break
            elif key in auntSues[sue].keys():
                if mysterySue[key] != auntSues[sue][key]:
                    legitSue = False
                    break
        for key in auntSues[sue].keys():
            if key not in mysterySue.keys():
                legitSue = False
                break
        if legitSue == True:
            return(sue)

identifyAuntSue(input)

# part 2
identifyAuntSue(input, partTwo = True)