# advent of code 2015
# day 14

# part 1
input = open('day-14.txt', 'r').read()

def reindeerRace(input, partTwo = False):
    reindeerStamina = {}
    reindeerSpeed = {}
    reindeerRest = {}
    for r in input.split('\n'):
        reindeerStamina[r.split(' ')[0]] = int(r.split(' ')[6])
        reindeerSpeed[r.split(' ')[0]] = int(r.split(' ')[3])
        reindeerRest[r.split(' ')[0]] = int(r.split(' ')[13])
    if partTwo == False:
        def runRace(rdeer):
            fullBlocks = 2503 // (reindeerStamina[rdeer] + reindeerRest[rdeer])
            surplus = 2503 % (reindeerStamina[rdeer] + reindeerRest[rdeer])
            extras = surplus if surplus <= reindeerStamina[rdeer] else reindeerStamina[rdeer]
            return(reindeerSpeed[rdeer] * (fullBlocks * reindeerStamina[rdeer] + extras))
        return(max([runRace(r) for r in reindeerStamina.keys()]))
    else:
        reindeerDistance = {}
        reindeerPoints = {}
        for r in reindeerStamina.keys():
            reindeerDistance[r] = 0
            reindeerPoints[r] = 0
        t = 0
        while t < 2503:
            for r in reindeerStamina.keys():
                if t % (reindeerStamina[r] + reindeerRest[r]) < reindeerStamina[r]:
                    reindeerDistance[r] += reindeerSpeed[r]
            leaderDistance = max(reindeerDistance.values())
            for r in reindeerStamina.keys():
                if reindeerDistance[r] == leaderDistance:
                    reindeerPoints[r] += 1
            t += 1
        return(max(reindeerPoints.values()))

reindeerRace(input)

# part 2
reindeerRace(input, partTwo = True)