# advent of code 2015
# day 21

# part 1
input = open('day-21.txt', 'r').read()

def chooseLoadout(input, partTwo = False):
    weapons = {
        'Dagger': {
            'Cost': 8,
            'Damage': 4
        },
        'Shortsword': {
            'Cost': 10,
            'Damage': 5
        },
        'Warhammer': {
            'Cost': 25,
            'Damage': 6
        },
        'Longsword': {
            'Cost': 40,
            'Damage': 7
        },
        'Greataxe': {
            'Cost': 74,
            'Damage': 8
        }
    }
    armor = {
        'Leather': {
            'Cost': 13,
            'Armor': 1
        },
        'Chainmail': {
            'Cost': 31,
            'Armor': 2
        },
        'Splintmail': {
            'Cost': 53,
            'Armor': 3
        },
        'Bandedmail': {
            'Cost': 75,
            'Armor': 4
        },
        'Platemail': {
            'Cost': 102,
            'Armor': 5
        }
    }
    rings = {
        'Damage +1': {
            'Cost': 25,
            'Damage': 1,
            'Armor': 0,
        },
        'Damage +2': {
            'Cost': 50,
            'Damage': 2,
            'Armor': 0,
        },
        'Damage +3': {
            'Cost': 100,
            'Damage': 3,
            'Armor': 0,
        },
        'Defense +1': {
            'Cost': 20,
            'Damage': 0,
            'Armor': 1,
        },
        'Defense +2': {
            'Cost': 40,
            'Damage': 0,
            'Armor': 2,
        },
        'Defense +3': {
            'Cost': 80,
            'Damage': 0,
            'Armor': 3,
        }
    }
    boss = [int(x.split(': ')[1]) for x in input.split('\n')]
    def doBattle(plyr, boss, partTwo):
        playerAttackPoints = max(plyr[1] - boss[2], 1)
        bossAttackPoints = max(boss[1] - plyr[2], 1)
        if partTwo == False:
            return(-(-boss[0] // playerAttackPoints) <= -(-plyr[0] // bossAttackPoints))
        else:
            return(-(-boss[0] // playerAttackPoints) > -(-plyr[0] // bossAttackPoints))
    loadOutCosts = []
    for wpn in weapons.keys():
        cost = weapons[wpn]['Cost']
        player = [100, weapons[wpn]['Damage'], 0]
        if doBattle(player, boss.copy(), partTwo = partTwo):
            loadOutCosts.append(cost)
        for rngId in range(len(list(rings.keys()))):
            cost = weapons[wpn]['Cost'] + rings[list(rings.keys())[rngId]]['Cost']
            player = [100, weapons[wpn]['Damage'] + rings[list(rings.keys())[rngId]]['Damage'], rings[list(rings.keys())[rngId]]['Armor']]
            if doBattle(player, boss.copy(), partTwo = partTwo):
                loadOutCosts.append(cost)
            if rngId < len(list(rings.keys())) - 1:
                for rngId2 in range(rngId + 1, len(list(rings.keys()))):
                    cost = cost = weapons[wpn]['Cost'] + rings[list(rings.keys())[rngId]]['Cost'] + rings[list(rings.keys())[rngId2]]['Cost']
                    player = [100, weapons[wpn]['Damage'] + rings[list(rings.keys())[rngId]]['Damage'] + rings[list(rings.keys())[rngId2]]['Damage'], rings[list(rings.keys())[rngId]]['Armor'] + rings[list(rings.keys())[rngId2]]['Armor']]
                    if doBattle(player, boss.copy(), partTwo = partTwo):
                        loadOutCosts.append(cost)
        for arm in armor.keys():
            cost = weapons[wpn]['Cost'] + armor[arm]['Cost']
            player = [100, weapons[wpn]['Damage'], armor[arm]['Armor']]
            if doBattle(player, boss.copy(), partTwo = partTwo):
                loadOutCosts.append(cost)
            for rngId in range(len(list(rings.keys()))):
                cost = weapons[wpn]['Cost'] + armor[arm]['Cost'] + rings[list(rings.keys())[rngId]]['Cost']
                player = [100, weapons[wpn]['Damage'] + rings[list(rings.keys())[rngId]]['Damage'], armor[arm]['Armor'] + rings[list(rings.keys())[rngId]]['Armor']]
                if doBattle(player, boss.copy(), partTwo = partTwo):
                    loadOutCosts.append(cost)
                if rngId < len(list(rings.keys())) - 1:
                    for rngId2 in range(rngId + 1, len(list(rings.keys()))):
                        cost = cost = weapons[wpn]['Cost'] + armor[arm]['Cost'] + rings[list(rings.keys())[rngId]]['Cost'] + rings[list(rings.keys())[rngId2]]['Cost']
                        player = [100, weapons[wpn]['Damage'] + rings[list(rings.keys())[rngId]]['Damage'] + rings[list(rings.keys())[rngId2]]['Damage'], armor[arm]['Armor'] + rings[list(rings.keys())[rngId]]['Armor'] + rings[list(rings.keys())[rngId2]]['Armor']]
                        if doBattle(player, boss.copy(), partTwo = partTwo):
                            loadOutCosts.append(cost)
    if partTwo == False:
        return(min(loadOutCosts))
    else:
        return(max(loadOutCosts))

chooseLoadout(input)

# part 2
chooseLoadout(input, partTwo = True)

