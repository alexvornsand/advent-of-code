### [--- Day 16: Proboscidea Volcanium ---](https://adventofcode.com/2022/day/16)

The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

You need to get the elephants out of here, quickly. Your device estimates that you have **30 minutes** before the volcano erupts, so you don't have time to go back out the way you came in.

You scan the cave for other options and discover a network of pipes and pressure-release **valves**. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's **flow rate** if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

There's even a valve in the room you and the elephants are currently standing in labeled ``AA``. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

For example, suppose you had the following scan output:

```
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
```
All of the valves begin **closed**. You start at valve `AA`, but it must be damaged or jammed or something: its flow rate is `0`, so there's no point in opening it. However, you could spend one minute moving to valve `BB` and another minute opening it; doing so would release pressure during the remaining **28 minutes** at a flow rate of `13`, a total eventual pressure release of `28 * 13 = 364`. Then, you could spend your third minute moving to valve `CC` and your fourth minute opening it, providing an additional **26 minutes** of eventual pressure release at a flow rate of `2`, or **`52`** total pressure released by valve `CC`.

Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

```
== Minute 1 ==
No valves are open.
You move to valve DD.

== Minute 2 ==
No valves are open.
You open valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You move to valve CC.

== Minute 4 ==
Valve DD is open, releasing 20 pressure.
You move to valve BB.

== Minute 5 ==
Valve DD is open, releasing 20 pressure.
You open valve BB.

== Minute 6 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve AA.

== Minute 7 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve II.

== Minute 8 ==
Valves BB and DD are open, releasing 33 pressure.
You move to valve JJ.

== Minute 9 ==
Valves BB and DD are open, releasing 33 pressure.
You open valve JJ.

== Minute 10 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve II.

== Minute 11 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve AA.

== Minute 12 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve DD.

== Minute 13 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve EE.

== Minute 14 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve FF.

== Minute 15 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve GG.

== Minute 16 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You move to valve HH.

== Minute 17 ==
Valves BB, DD, and JJ are open, releasing 54 pressure.
You open valve HH.

== Minute 18 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve GG.

== Minute 19 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve FF.

== Minute 20 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve EE.

== Minute 21 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve EE.

== Minute 22 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve DD.

== Minute 23 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You move to valve CC.

== Minute 24 ==
Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
You open valve CC.

== Minute 25 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 27 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 28 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 29 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

== Minute 30 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
```
This approach lets you release the most pressure possible in 30 minutes with this valve layout, **`1651`**.

Work out the steps to release the most pressure in 30 minutes. **What is the most pressure you can release?**

#### --- Part Two ---

You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only **26 minutes** to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

In the example above, you could teach the elephant to help you as follows:

```
== Minute 1 ==
No valves are open.
You move to valve II.
The elephant moves to valve DD.

== Minute 2 ==
No valves are open.
You move to valve JJ.
The elephant opens valve DD.

== Minute 3 ==
Valve DD is open, releasing 20 pressure.
You open valve JJ.
The elephant moves to valve EE.

== Minute 4 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve II.
The elephant moves to valve FF.

== Minute 5 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve AA.
The elephant moves to valve GG.

== Minute 6 ==
Valves DD and JJ are open, releasing 41 pressure.
You move to valve BB.
The elephant moves to valve HH.

== Minute 7 ==
Valves DD and JJ are open, releasing 41 pressure.
You open valve BB.
The elephant opens valve HH.

== Minute 8 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You move to valve CC.
The elephant moves to valve GG.

== Minute 9 ==
Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
You open valve CC.
The elephant moves to valve FF.

== Minute 10 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant moves to valve EE.

== Minute 11 ==
Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
The elephant opens valve EE.

(At this point, all valves are open.)

== Minute 12 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 20 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

...

== Minute 26 ==
Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
```
With the elephant helping, after 26 minutes, the best you could do would release a total of **`1707`** pressure.

**With you and an elephant working together for 26 minutes, what is the most pressure you could release?**

#### [--- Solution ---](day-16.py)
```Python
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
```