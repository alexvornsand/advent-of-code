### [--- Day 23: Amphipod ---](https://adventofcode.com/2021/day/23)

A group of [amphipods](https://en.wikipedia.org/wiki/Amphipoda) notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: **Amber** (`A`), **Bronze** (`B`), **Copper** (`C`), and **Desert** (`D`). They live in a burrow that consists of a **hallway** and four **side rooms**. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a **diagram of the situation** (your puzzle input), including locations of each amphipod (`A`, `B`, `C`, or `D`, each of which is occupying an otherwise open space), walls (`#`), and open space (`.`).

For example:

```
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```
The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted `A`-`D` going left to right, like this:

```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```
Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of **energy** to move one step: Amber amphipods require `1` energy per step, Bronze amphipods require `10` energy, Copper amphipods require `100`, and Desert ones require `1000`. The amphipods would like you to find a way to organize the amphipods that requires the **least total energy**.

However, because they are timid and stubborn, the amphipods have some extra rules:

- Amphipods will never **stop on the space immediately outside any room**. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
- Amphipods will never **move from the hallway into a room** unless that room is their destination room **and** that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
- Once an amphipod stops moving in the hallway, it will **stay in that spot until it can move into a room**. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)
In the above example, the amphipods can be organized using a minimum of **`12521`** energy. One way to do this is shown below.

Starting configuration:

```
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
```
One Bronze amphipod moves into the hallway, taking 4 steps and using `40` energy:

```
#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########
```
The only Copper amphipod not in its side room moves there, taking 4 steps and using `400` energy:

```
#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########
```
A Desert amphipod moves out of the way, taking 3 steps and using `3000` energy, and then the Bronze amphipod takes its place, taking 3 steps and using `30` energy:

```
#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########
```
The leftmost Bronze amphipod moves to its room using `40` energy:

#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########
Both amphipods in the rightmost room move into the hallway, using `2003` energy in total:

```
#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########
```
Both Desert amphipods move into the rightmost room using `7000` energy:

```
#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########
```
Finally, the last Amber amphipod moves into its room, using `8` energy:

```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
```
**What is the least energy required to organize the amphipods?**

### --- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

```
  #D#C#B#A#
  #D#B#A#C#
```
So, the above example now becomes:

```
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
```
The amphipods still want to be organized into rooms similar to before:

```
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
```
In this updated example, the least energy required to organize these amphipods is **`44169`**:

```
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
 ```
Using the initial configuration from the full diagram, **what is the least energy required to organize the amphipods?**

# [--- Solution ---](day-23.py)
```Python
# advent of code 2021
# day 23

# part 1
import string
from copy import deepcopy

bugs = [d for l in open('input.txt', 'r').read().rstrip().splitlines()[1:-1] for d in l if d not in ['.', '#', ' ']]

def minimizeMoveCost(bugs, partTwo=False):
    def findNodeRoutes(nodes):
        pathBetweenNodes = {}
        for start in nodes:
            for end in nodes:
                if start < end:
                    queue = [key for key in nodes]
                    distances = dict({key: 999999 for key in nodes})
                    distances[start] = 0
                    currentNode = start
                    while(True):
                        if currentNode == end:
                            path = [end]
                            currentNode = end
                            while(True):
                                for node in nodes[currentNode]['connectedNodes']:
                                    if node == start:
                                        path.append(start)
                                        break
                                    elif distances[node] == distances[currentNode] - 1:
                                        if any([distances[next] == distances[currentNode] - 2 for next in nodes[node]['connectedNodes']]):
                                            nextNode = node
                                else:
                                    currentNode = nextNode
                                    path.append(currentNode)
                                    continue
                                break
                            pathBetweenNodes[(start, end)] = path[::-1][1:]
                            pathBetweenNodes[(end, start)] = path[1:]
                            break
                        for neighbor in nodes[currentNode]['connectedNodes']:
                            if neighbor in queue:
                                if distances[currentNode] + 1 < distances[neighbor]:
                                    distances[neighbor] = distances[currentNode] + 1
                            else:
                                pass
                        queue.remove(currentNode)
                        currentNode = sorted(queue, key=distances.get)[0]
                else:
                    pass
        return(pathBetweenNodes)        
    def eligibleDestinations(bug, nodes, pathBetweenNodes, verbose=False):
        candidateDestinations = ['l1', 'l2', 'h2', 'h4', 'h6', 'r2', 'r1']
        if partTwo is True:
            if bug[0] == 'A':
                if nodes['a1']['occupant'] == '':
                    candidateDestinations.append('a1')
                elif nodes['a1']['occupant'][0] == 'A' and nodes['a2']['occupant'] == '':
                    candidateDestinations.append('a2')
                elif nodes['a1']['occupant'][0] == 'A' and nodes['a2']['occupant'] != '' and nodes['a2']['occupant'][0] == 'A' and nodes['a3']['occupant'] == '':
                    candidateDestinations.append('a3')
                elif nodes['a1']['occupant'][0] == 'A' and nodes['a2']['occupant'] != '' and nodes['a2']['occupant'][0] == 'A' and nodes['a3']['occupant'] != '' and nodes['a3']['occupant'][0] == 'A':
                    candidateDestinations.append('a4')
            elif bug[0] == 'B':
                if nodes['b1']['occupant'] == '':
                    candidateDestinations.append('b1')
                elif nodes['b1']['occupant'][0] == 'B' and nodes['b2']['occupant'] == '':
                    candidateDestinations.append('b2')
                elif nodes['b1']['occupant'][0] == 'B' and nodes['b2']['occupant'] != '' and nodes['b2']['occupant'][0] == 'B' and nodes['b3']['occupant'] == '':
                    candidateDestinations.append('b3')
                elif nodes['b1']['occupant'][0] == 'B' and nodes['b2']['occupant'] != '' and nodes['b2']['occupant'][0] == 'B' and nodes['b3']['occupant'] != '' and nodes['b3']['occupant'][0] == 'B':
                    candidateDestinations.append('b4')
            elif bug[0] == 'C':
                if nodes['c1']['occupant'] == '':
                    candidateDestinations.append('c1')
                elif nodes['c1']['occupant'][0] == 'C' and nodes['c2']['occupant'] == '':
                    candidateDestinations.append('c2')
                elif nodes['c1']['occupant'][0] == 'C' and nodes['c2']['occupant'] != '' and nodes['c2']['occupant'][0] == 'C' and nodes['c3']['occupant'] == '':
                    candidateDestinations.append('c3')
                elif nodes['c1']['occupant'][0] == 'C' and nodes['c2']['occupant'] != '' and nodes['c2']['occupant'][0] == 'C' and nodes['c3']['occupant'] != '' and nodes['c3']['occupant'][0] == 'C':
                    candidateDestinations.append('c4')
            elif bug[0] == 'D':
                if nodes['d1']['occupant'] == '':
                    candidateDestinations.append('d1')
                elif nodes['d1']['occupant'][0] == 'D' and nodes['d2']['occupant'] == '':
                    candidateDestinations.append('d2')
                elif nodes['d1']['occupant'][0] == 'D' and nodes['d2']['occupant'] != '' and nodes['d2']['occupant'][0] == 'D' and nodes['d3']['occupant'] == '':
                    candidateDestinations.append('d3')
                elif nodes['d1']['occupant'][0] == 'D' and nodes['d2']['occupant'] != '' and nodes['d2']['occupant'][0] == 'D' and nodes['d3']['occupant'] != '' and nodes['d3']['occupant'][0] == 'D':
                    candidateDestinations.append('d4')
        else:
            if bug[0] == 'A':
                if nodes['a3']['occupant'] == '':
                    candidateDestinations.append('a3')
                elif nodes['a3']['occupant'][0] == 'A':
                    candidateDestinations.append('a4')
            elif bug[0] == 'B':
                if nodes['b3']['occupant'] == '':
                    candidateDestinations.append('b3')
                elif nodes['b3']['occupant'][0] == 'B':
                    candidateDestinations.append('b4')
            elif bug[0] == 'C':
                if nodes['c3']['occupant'] == '':
                    candidateDestinations.append('c3')
                elif nodes['c3']['occupant'][0] == 'C':
                    candidateDestinations.append('c4')
            elif bug[0] == 'D':
                if nodes['d3']['occupant'] == '':
                    candidateDestinations.append('d3')
                elif nodes['d3']['occupant'][0] == 'D':
                    candidateDestinations.append('d4')       
        destinations = []
        bugLoc = [key for key in nodes if nodes[key]['occupant'] == bug][0]
        if verbose is True:
            print('bug:', bug)
            print('candidates:', candidateDestinations)
        for candidate in candidateDestinations:
            if bugLoc != candidate:
                if verbose is True:
                    print('destination:', candidate)
                steps = pathBetweenNodes[(bugLoc, candidate)]
                stepsUnoccupied = [nodes[step]['occupant'] == '' for step in steps]
                if all(stepsUnoccupied):
                    if bugLoc[0] in ['h', 'l', 'r'] and candidate[0] != bug[0].lower():
                        pass
                        if verbose is True:
                            print('bug not in starting position and candidate not final destination')
                    else:
                        destinations.append((candidate, len(pathBetweenNodes[(bugLoc, candidate)])))
                        if verbose is True:
                            print('all gut')
                else:
                    if verbose is True:
                        print('blocked by', [steps[i] for i in range(len(stepsUnoccupied)) if stepsUnoccupied[i] is False])
        return(destinations)
    def shouldMove(bug, nodes):
        bugLoc = [key for key in nodes if nodes[key]['occupant'] == bug][0]
        if partTwo is True:
            if bugLoc[0] == bug[0].lower():
                if bugLoc[1] == '1':
                    return(False)
                elif bugLoc[1] == '2' and nodes[bug[0].lower() + '1']['occupant'] != '' and nodes[bug[0].lower() + '1']['occupant'][0] == bug[0]:
                    return(False)
                elif bugLoc[1] == '3' and nodes[bug[0].lower() + '2']['occupant'] != '' and nodes[bug[0].lower() + '2']['occupant'][0] == bug[0] and nodes[bug[0].lower() + '1']['occupant'] != '' and nodes[bug[0].lower() + '1']['occupant'][0] == bug[0]:
                    return(False)
                elif bugLoc[1] == '4' and nodes[bug[0].lower() + '3']['occupant'] != '' and nodes[bug[0].lower() + '3']['occupant'][0] == bug[0] and nodes[bug[0].lower() + '2']['occupant'] != '' and nodes[bug[0].lower() + '2']['occupant'][0] == bug[0] and nodes[bug[0].lower() + '1']['occupant'] != '' and nodes[bug[0].lower() + '1']['occupant'][0] == bug[0]:
                    return(False)
                else:
                    return(True)
            else:
                return(True)
        else:
            if bugLoc[0] == bug[0].lower():
                if bugLoc[1] == '3':
                    return(False)
                elif bugLoc[1] == '4' and nodes[bug[0].lower() + '3']['occupant'] != '' and nodes[bug[0].lower() + '3']['occupant'][0] == bug[0]:
                    return(False)
                else:
                    return(True)
            else:
                return(True)
    def navigatePath(state, history, cost, lowestCost, memo):
        if state in memo:
            memo_hist, memo_cost = memo[state]
            return(history + memo_hist, cost + memo_cost)
        else:
            currentNodes = deepcopy(nodes)
            for pair in state:
                bug = pair[:2]
                address = pair[2:]
                currentNodes[address]['occupant'] = bug
            if all(
                [
                    currentNodes['a1']['occupant'] in ['A1', 'A2', 'A3', 'A4'] if partTwo is True else True,
                    currentNodes['a2']['occupant'] in ['A1', 'A2', 'A3', 'A4'] if partTwo is True else True,
                    currentNodes['a3']['occupant'] in ['A1', 'A2', 'A3', 'A4'],
                    currentNodes['a4']['occupant'] in ['A1', 'A2', 'A3', 'A4'],
                    currentNodes['b1']['occupant'] in ['B1', 'B2', 'B3', 'B4'] if partTwo is True else True,
                    currentNodes['b2']['occupant'] in ['B1', 'B2', 'B3', 'B4'] if partTwo is True else True,
                    currentNodes['b3']['occupant'] in ['B1', 'B2', 'B3', 'B4'],
                    currentNodes['b4']['occupant'] in ['B1', 'B2', 'B3', 'B4'],
                    currentNodes['c1']['occupant'] in ['C1', 'C2', 'C3', 'C4'] if partTwo is True else True,
                    currentNodes['c2']['occupant'] in ['C1', 'C2', 'C3', 'C4'] if partTwo is True else True,
                    currentNodes['c3']['occupant'] in ['C1', 'C2', 'C3', 'C4'],
                    currentNodes['c4']['occupant'] in ['C1', 'C2', 'C3', 'C4'],
                    currentNodes['d1']['occupant'] in ['D1', 'D2', 'D3', 'D4'] if partTwo is True else True,
                    currentNodes['d2']['occupant'] in ['D1', 'D2', 'D3', 'D4'] if partTwo is True else True,
                    currentNodes['d3']['occupant'] in ['D1', 'D2', 'D3', 'D4'],
                    currentNodes['d4']['occupant'] in ['D1', 'D2', 'D3', 'D4'],
                ]
            ):            
                memo[state] = (history, cost)
                return(history, cost)
            else:
                nextResults = []
                movementCost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
                buglist = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']
                if partTwo is True:
                    buglist += ['A3', 'A4', 'B3', 'B4', 'C3', 'C4', 'D3', 'D4']
                for bug in [bug for bug in buglist if shouldMove(bug, currentNodes)]:
                    for destination in eligibleDestinations(bug, currentNodes, pathBetweenNodes):
                        destLoc, steps = destination
                        bugLoc = [key for key in currentNodes if currentNodes[key]['occupant'] == bug][0]
                        sit_nodes = deepcopy(currentNodes)
                        sit_nodes[destLoc]['occupant'] = bug
                        sit_nodes[bugLoc]['occupant'] = ''
                        sit_state = tuple([sit_nodes[node]['occupant'] + node for node in sit_nodes if sit_nodes[node]['occupant'] != ''])
                        sit_history = history.copy()
                        sit_history.append(bug + destLoc)
                        sit_cost = cost + (steps * movementCost[bug[0]])
                        if sit_cost < lowestCost:
                            sit_result_history, sit_result_cost = navigatePath(sit_state, sit_history, sit_cost, lowestCost, memo)
                            sit_future_history = sit_result_history[len(sit_history):]
                            sit_future_cost = sit_result_cost - sit_cost
                            memo[sit_state] = (sit_future_history, sit_future_cost)
                            nextResults.append((sit_result_history, sit_result_cost))
                            lowestCost = min(lowestCost, sit_result_cost)
                if len(nextResults) == 0:
                    history.append('|')
                    cost = 999999
                    memo[state] = (history, cost)
                    return(history, cost)
                else:
                    bestNextMove = min(nextResults, key=lambda r: r[1])
                    full_history, full_cost = bestNextMove
                    future_history = full_history[len(history):]
                    future_cost = full_cost - cost
                    memo[state] = (future_history, future_cost)
                    return(bestNextMove)
    nodes = {
        'l1': {'occupant': '', 'connectedNodes': ['l2']},
        'l2': {'occupant': '', 'connectedNodes': ['l1', 'h1']},
        'h1': {'occupant': '', 'connectedNodes': ['l2', 'h2', 'a4']},
        'a4': {'occupant': '', 'connectedNodes': ['a3', 'h1']},
        'a3': {'occupant': '', 'connectedNodes': ['a2', 'a4']},
        'a2': {'occupant': '', 'connectedNodes': ['a1', 'a3']},
        'a1': {'occupant': '', 'connectedNodes': ['a2']},
        'h2': {'occupant': '', 'connectedNodes': ['h1', 'h3']},
        'h3': {'occupant': '', 'connectedNodes': ['h2', 'h4', 'b4']},
        'b4': {'occupant': '', 'connectedNodes': ['b3', 'h3']},
        'b3': {'occupant': '', 'connectedNodes': ['b2', 'b4']},
        'b2': {'occupant': '', 'connectedNodes': ['b1', 'b3']},
        'b1': {'occupant': '', 'connectedNodes': ['b2']},
        'h4': {'occupant': '', 'connectedNodes': ['h3', 'h5']},
        'h5': {'occupant': '', 'connectedNodes': ['h4', 'h6', 'c4']},
        'c4': {'occupant': '', 'connectedNodes': ['c3', 'h5']},
        'c3': {'occupant': '', 'connectedNodes': ['c2', 'c4']},
        'c2': {'occupant': '', 'connectedNodes': ['c1', 'c3']},
        'c1': {'occupant': '', 'connectedNodes': ['c2']},
        'h6': {'occupant': '', 'connectedNodes': ['h5', 'h7']},
        'h7': {'occupant': '', 'connectedNodes': ['h6', 'r2', 'd4']},
        'd4': {'occupant': '', 'connectedNodes': ['d3', 'h7']},
        'd3': {'occupant': '', 'connectedNodes': ['d2', 'd4']},
        'd2': {'occupant': '', 'connectedNodes': ['d1', 'd3']},
        'd1': {'occupant': '', 'connectedNodes': ['d2']},
        'r2': {'occupant': '', 'connectedNodes': ['r1', 'h7']},
        'r1': {'occupant': '', 'connectedNodes': ['r2']},
    }
    if partTwo is True:
        bugsList = bugs[:4] + ['D', 'C', 'B', 'A', 'D', 'B', 'A', 'C'] + bugs[4:]
    ids = []
    bugNos = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    for bug in bugsList:
        ids.append(bug + str(bugNos[bug]))
        bugNos[bug] += 1
    state = tuple([bug + add for bug, add in zip(ids, ['a4', 'b4', 'c4', 'd4', 'a3', 'b3', 'c3', 'd3', 'a2', 'b2', 'c2', 'd2', 'a1', 'b1', 'c1', 'd1'])])
    pathBetweenNodes = findNodeRoutes(nodes)
    memo = {}
    return(navigatePath(state, [], 0, 999999, memo)[1])

minimizeMoveCost(bugs)

# part 2
minimizeMoveCost(bugs, True)
```