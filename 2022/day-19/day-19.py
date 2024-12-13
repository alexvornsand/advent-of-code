# advent of code 2022
# day 19

# part 1
import re
import math

blueprints = open('input.txt', 'r').read()[:-1].split('\n')

def analyzeBlueprints(blueprints, partTwo=False):
    def scoreBlueprint(blueprint, partTwo=False):
        def findBestPathForward(blueprint, history, rBot, cBot, oBot, r, c, o, g, time, best):
            if g + (time) * (time - 1) / 2 < best:
                return(history + '_' * time, g)
            else:
                candidates = []
                # next bot is r
                tR = max(math.ceil((blueprint['ore']['ore'] - r) / rBot), 0)
                rEnoughTime =  tR + 4 < time
                rNeeded = rBot < max(blueprint['ore']['ore'], blueprint['clay']['ore'], blueprint['obsidian']['ore'], blueprint['geode']['ore']) 
                rBacklog = r + (rBot * tR) + (rBot * (time - tR)) < (time - tR) * max(blueprint['ore']['ore'], blueprint['clay']['ore'], blueprint['obsidian']['ore'], blueprint['geode']['ore'])
                if all([rEnoughTime, rNeeded, rBacklog]):
                    result = findBestPathForward(*[blueprint, history + '_' * tR + 'r', rBot + 1, cBot, oBot, r + rBot * (tR + 1) - blueprint['ore']['ore'], c + cBot * (tR + 1), o + oBot * (tR + 1), g, time - (tR + 1), best])
                    candidates.append(result)
                    if result[1] > best:
                        best = result[1]
                # next bot is c
                tC = max(math.ceil((blueprint['clay']['ore'] - r) / rBot), 0)
                cEnoughTime =  tR + 4 < time
                cNeeded = cBot < blueprint['obsidian']['clay']
                cBacklog = c + (cBot * tC) + (cBot * (time - tC)) < (time - tC) * blueprint['obsidian']['clay']
                if all([cEnoughTime, cNeeded, cBacklog]):
                    result = findBestPathForward(*[blueprint, history + '_' * tC + 'c', rBot, cBot + 1, oBot, r + rBot * (tC + 1) - blueprint['clay']['ore'], c + cBot * (tC + 1), o + oBot * (tC + 1), g, time - (tC + 1), best])
                    candidates.append(result)
                    if result[1] > best:
                        best = result[1]
                # next bot is o
                if cBot > 0:
                    tO = max(math.ceil((blueprint['obsidian']['ore'] - r) / rBot), math.ceil((blueprint['obsidian']['clay'] - c) / cBot), 0)
                    oEnoughTime =  tO + 4 < time
                    oNeeded = oBot < blueprint['geode']['obsidian']
                    oBacklog = o + (oBot * tO) + (oBot * (time - tO)) < (time - tO) * blueprint['geode']['obsidian']
                    if all([oEnoughTime, oNeeded, oBacklog]):
                        result = findBestPathForward(*[blueprint, history + '_' * tO + 'o', rBot, cBot, oBot + 1, r + rBot * (tO + 1) - blueprint['obsidian']['ore'], c + cBot * (tO + 1) - blueprint['obsidian']['clay'], o + oBot * (tO + 1), g, time - (tO + 1), best])
                        candidates.append(result)
                        if result[1] > best:
                            best = result[1]
                # next bot is g
                if oBot > 0:
                    tG = max(math.ceil((blueprint['geode']['ore'] - r) / rBot), math.ceil((blueprint['geode']['obsidian'] - o) / oBot), 0)
                    if tG + 2 <= time:
                        result = findBestPathForward(*[blueprint, history + '_' * tG + 'g', rBot, cBot, oBot, r + rBot * (tG + 1) - blueprint['geode']['ore'], c + cBot * (tG + 1), o + oBot * (tG + 1) - blueprint['geode']['obsidian'], g + time - (tG + 1), time - (tG + 1), best])
                        candidates.append(result)
                        if result[1] > best:
                            best = result[1]
                if len(candidates) > 1:
                    return(max(candidates, key = lambda r: r[1]))
                elif len(candidates) == 1:
                    return(candidates[0])
                else:
                    return(history + '_' * time, g)            
        best = 0
        if partTwo is False:
            queue = [blueprint, '', 1, 0, 0, 0, 0, 0, 0, 24, best]
        else:
            queue = [blueprint, '', 1, 0, 0, 0, 0, 0, 0, 32, best]
        return(findBestPathForward(*queue))
    results = []
    if partTwo is True:
        blueprints = blueprints[:min(3, len(blueprints))]
    blueprintsDict = {}
    for blueprint in blueprints:
        blueprintDetails = re.match('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', blueprint).groups()
        id = int(blueprintDetails[0])
        ore = {'ore': int(blueprintDetails[1])}
        clay = {'ore': int(blueprintDetails[2])}
        obsidian = {
            'ore': int(blueprintDetails[3]),
            'clay': int(blueprintDetails[4])
        }
        geode = {
            'ore': int(blueprintDetails[5]),
            'obsidian': int(blueprintDetails[6])
        }
        blueprintDict = {
            'ore': ore,
            'clay': clay,
            'obsidian': obsidian,
            'geode': geode
        }
        results.append([id, *scoreBlueprint(blueprintDict, partTwo)])
    if partTwo is False:
        return(sum([blueprint[0] * blueprint[2] for blueprint in results]))
    else:
        return(math.prod([blueprint[2] for blueprint in results]))

analyzeBlueprints(blueprints)

# part 2
analyzeBlueprints(blueprints, True)