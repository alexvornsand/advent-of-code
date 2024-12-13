# advent of code 2022
# day 16

# part 1
import re

valveRates = open('input.txt', 'r').read()[:-1].split('\n')

def releasePressure(valveRates, partTwo=False):
    def parseValves(valveRates):
        valves = {}
        for valve in valveRates:
            valveInfo = re.match('Valve\s([A-Z]{2}).*=(\d+).*valves?\s(.*)', valve).groups()
            name = valveInfo[0]
            rate = int(valveInfo[1])
            connectedValves = valveInfo[2].split(', ')
            valves[name] = {
                'rate': rate,
                'connectedValves': connectedValves
            }
        return(valves)
    def findValveRoutes(valves):
        pathBetweenValves = {}
        for start in valves:
            for end in valves:
                if start < end:
                    queue = [key for key in valves]
                    distances = dict({key: 999999 for key in valves})
                    distances[start] = 0
                    currentValve = start
                    while(True):
                        if currentValve == end:
                            path = [end]
                            currentValve = end
                            while(True):
                                for valve in valves[currentValve]['connectedValves']:
                                    if valve == start:
                                        path.append(start)
                                        break
                                    elif distances[valve] == distances[currentValve] - 1:
                                        if any([distances[next] == distances[currentValve] - 2 for next in valves[valve]['connectedValves']]):
                                            nextValve = valve
                                else:
                                    currentValve = nextValve
                                    path.append(currentValve)
                                    continue
                                break
                            pathBetweenValves[(start, end)] = path[::-1][1:]
                            pathBetweenValves[(end, start)] = path[1:]
                            break
                        for neighbor in valves[currentValve]['connectedValves']:
                            if neighbor in queue:
                                if distances[currentValve] + 1 < distances[neighbor]:
                                    distances[neighbor] = distances[currentValve] + 1
                            else:
                                pass
                        queue.remove(currentValve)
                        currentValve = sorted(queue, key=distances.get)[0]
                else:
                    pass
        for valve in valves:
            pathBetweenValves[(valve,valve)] = []
        return(pathBetweenValves)
    def bestCaseScenario(trH, trE, uv, ovH, ovE):
        trHBCS = trH
        trEBCS = trE
        uvRates = sorted([valves[valve]['rate'] for valve in uv], reverse = True)
        pbPotential = sum([valves[valve]['rate'] * trH for valve in ovH]) + sum([valves[valve]['rate'] * trE for valve in ovE])
        while((trHBCS > 0 or trEBCS > 0) and len(uvRates) > 0):
            if trHBCS > 0:
                pbPotential += (trHBCS - 2) * uvRates[0]
                uvRates.pop(0)
                trHBCS -= 2
            if trEBCS > 0 and len(uvRates) > 0:
                pbPotential += (trEBCS - 2) * uvRates[0]
                uvRates.pop(0)
                trHBCS -= 2
        return(pbPotential)
    def findPairOfPaths(valves, pbv, vsH, vsE, uv, ovH, ovE, trH, trE, pr, best, memo):
        locH = vsH[-1]
        locE = vsE[-1]
        scenarioOptions = []
        optionsH = [valve for valve in uv if len(pbv[(locH, valve)]) + 2 <= trH]
        optionsE = [valve for valve in uv if len(pbv[(locE, valve)]) + 2 <= trE]
        if trH > trE:
            # Human has more time left than Elephant does
            # Human chooses where to go next, Elephant stays where they are
            next_vsE = vsE.copy()
            next_ovE = ovE
            next_trE = trE
            # scenario where Human parks and Elephant continues
            next_vsH = vsH.copy()
            next_ovH = ovH.copy()
            next_trH = 0
            next_uv = uv.copy()
            next_pr = pr
            scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
            scenarioOptions.append(scenario)
            if len(optionsH) > 0:
                # scenarios where Human does a next move
                # loop through each of Human's options
                for option in optionsH:
                    next_vsH = vsH.copy() + [option]
                    next_ovH = ovH.copy() + [option]
                    next_trH = trH - (len(pbv[(locH, option)]) + 1)
                    next_uv = uv.copy()
                    next_uv.remove(option)
                    next_pr = pr + valves[option]['rate'] * (next_trH)
                    scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
                    scenarioOptions.append(scenario)
        elif trH < trE:
            # Elephant has more time left than Human does
            # Elephant chooses where to go next, Human stays where they are
            next_vsH = vsH.copy()
            next_ovH = ovH
            next_trH = trH
            # scenario where Elephant parks and Human continues
            next_vsE = vsE.copy()
            next_ovE = ovE.copy()
            next_trE = 0
            next_uv = uv.copy()
            next_pr = pr
            scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
            scenarioOptions.append(scenario)
            if len(optionsE) > 0:
                # scenarios where Elephant does a next move
                # loop through each of Elephant's options
                for option in optionsE:
                    next_vsE = vsE.copy() + [option]
                    next_ovE = ovE.copy() + [option]
                    next_trE = trE - (len(pbv[(locE, option)]) + 1)
                    next_uv = uv.copy()
                    next_uv.remove(option)
                    next_pr = pr + valves[option]['rate'] * (next_trE)
                    scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
                    scenarioOptions.append(scenario)
        else:
            # Human and Elephant are choosing where to go at the same time
            if trH == 0:
                # Time is at 0
                # End of the scenario
                return(vsH, vsE, pr)
            else:
                # scenario where Elephant parks and Human continues
                next_vsE = vsE.copy()
                next_ovE = ovE
                next_trE = 0
                for option in optionsH:
                    next_vsH = vsH.copy() + [option]
                    next_ovH = ovH.copy() + [option]
                    next_trH = trH - (len(pbv[(locH, option)]) + 1)
                    next_uv = uv.copy()
                    next_uv.remove(option)
                    next_pr = pr + valves[option]['rate'] * (next_trH)
                    scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
                    scenarioOptions.append(scenario)
                # scenario where Human parks and Elephant continues
                next_vsH = vsH.copy()
                next_ovH = ovH
                next_trH = 0
                for option in optionsE:
                    next_vsE = vsE.copy() + [option]
                    next_ovE = ovE.copy() + [option]
                    next_trE = trE - (len(pbv[(locE, option)]) + 1)
                    next_uv = uv.copy()
                    next_uv.remove(option)
                    next_pr = pr + valves[option]['rate'] * (next_trE)
                    scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
                    scenarioOptions.append(scenario)
                # scenario where Humand and Elephant each choose a next step
                if len(optionsH) > 0 and len(optionsE) > 0:
                    for optionH in optionsH:
                        for optionE in optionsE:
                            if optionH != optionE:
                                next_vsH = vsH.copy() + [optionH]
                                next_ovH = ovH.copy() + [optionH]
                                next_trH = trH - (len(pbv[(locH, optionH)]) + 1)
                                next_vsE = vsE.copy() + [optionE]
                                next_ovE = ovE.copy() + [optionE]
                                next_trE = trE - (len(pbv[(locE, optionE)]) + 1)
                                next_uv = uv.copy()
                                next_uv.remove(optionH)
                                next_uv.remove(optionE)
                                next_pr = pr + valves[optionH]['rate'] * (next_trH) + valves[optionE]['rate'] * (next_trE)
                                scenario = [[next_vsH, next_vsE, next_uv, next_ovH, next_ovE, next_trH, next_trE, next_pr], next_pr + bestCaseScenario(next_trH, next_trE, next_uv, next_ovH, next_ovE)]
                                scenarioOptions.append(scenario)
                else:
                    next_vsH = vsH.copy()
                    next_vsE = vsE.copy()
                    next_pr = pr
                    return(next_vsH, next_vsE, next_pr)
        scenarioResults = []
        for scenario in scenarioOptions:
            if scenario[1] > best:
                test_vsH, test_vsE, test_uv, test_ovH, test_ovE, test_trH, test_trE, test_pr = scenario[0]
                if (test_vsH[-1], test_vsE[-1], test_trH, test_trE, tuple(test_uv)) in memo:
                    scenarioResult = (test_vsH, test_vsE, test_pr + memo[(test_vsH[-1], test_vsE[-1], test_trH, test_trE, tuple(test_uv))])
                else:
                    scenarioResult = findPairOfPaths(valves, pbv, *scenario[0], best, memo)
                    memo[(test_vsH[-1], test_vsE[-1], test_trH, test_trE, tuple(test_uv))] = scenarioResult[2] - test_pr
                best = scenarioResult[2] if scenarioResult[2] > best else best
                scenarioResults.append(scenarioResult)
        if len(scenarioResults) > 0:
            return(max(scenarioResults, key=lambda r: r[2]))
        else:
            next_vsH = vsH.copy()
            next_vsE = vsE.copy()
            next_pr = pr
            return(next_vsH, next_vsE, next_pr)
    valves = parseValves(valveRates)
    pathBetweenValves = findValveRoutes(valves)
    usefulValves = [valve for valve in valves if valves[valve]['rate'] > 0]
    valveSequenceHuman = ['AA']
    valveSequenceElephant = ['AA']
    unopenedValves = usefulValves.copy()
    openedValvesHuman = []
    openedValvesElephant = []
    if partTwo is False:
        timeRemainingHuman = 30
        timeRemainingElephant = 0
    else:
        timeRemainingHuman = 26
        timeRemainingElephant = 26
    pressureReleased = 0
    best = 0
    memo = {}
    return(findPairOfPaths(valves, pathBetweenValves, valveSequenceHuman, valveSequenceElephant, unopenedValves, openedValvesHuman, openedValvesElephant, timeRemainingHuman, timeRemainingElephant, pressureReleased, best, memo)[2])

releasePressure(valveRates)

# part 2
releasePressure(valveRates, True)
