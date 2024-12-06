### [--- Day 6: Guard Gallivant ---](https://adventofcode.com/2024/day/6)

The Historians use their fancy [device](https://adventofcode.com/2024/day/4) again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year [1518](https://adventofcode.com/2018/day/5)! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single **guard** is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

The map shows the current position of the guard with `^` (to indicate the guard is currently facing **up** from the perspective of the map). Any **obstructions** - crates, desks, alchemical reactors, etc. - are shown as `#`.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

```
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

```
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Reaching another obstacle (a spool of several **very** long polymers), she turns right again and continues downward:

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
```

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
```

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. **Including the guard's starting position**, the positions visited by the guard before leaving the area are marked with an X:

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

In this example, the guard will visit **`41`** distinct positions on your map.

Predict the path of the guard. **How many distinct positions will the guard visit before leaving the mapped area?**

### --- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and [record](https://adventofcode.com/2018/day/4) the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are **pretty sure** that adding a single new obstruction **won't** cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get **stuck in a loop**, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know **all** of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only **`6`** different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, `|` to show a position where the guard moves up/down, `-` to show a position where the guard moves left/right, and `+` to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

```
....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
```

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
```

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
```

Option four, put an alchemical retroencabulator near the bottom left corner:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
```

Option five, put the alchemical retroencabulator a bit to the right instead:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
```

Option six, put a tank of sovereign glue right next to the tank of universal solvent:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
```

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are **`6`** different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. **How many different positions could you choose for this obstruction?**

### [--- Solution ---](day-06.py)
```Python
# advent of code 2024
# day 06

file = 'input.txt'

class GuardMap:
    def __init__(self, map):
        self.map_dict = {(i, j): map[j][i] for j in range(len(map)) for i in range(len(map[j]))}
        self.guard = list(self.map_dict.keys())[list(self.map_dict.values()).index('^')]

    def takeStep(self, md, g):
        dirs = ['^', '>', 'v', '<']
        paths = ['|', '-']
        steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        try_step = steps[dirs.index(md[g])]
        new_loc = (g[0] + try_step[0], g[1] + try_step[1])
        if new_loc in md:
            if md[new_loc] != '#':
                md[new_loc] = md[g]
                md[g] = paths[dirs.index(md[g]) % 2]
                g = new_loc
            else:
                md[g] = dirs[(dirs.index(md[g]) + 1) % 4]
        else:
            md[g] = paths[dirs.index(md[g]) % 2]
            g = (-1, -1)
        return md, g
    
    def printMap(md):
        minX = min([key[0] for key in md.keys()])
        maxX = max([key[0] for key in md.keys()])
        minY = min([key[1] for key in md.keys()])
        maxY = max([key[1] for key in md.keys()])
        print('\n'.join([''.join([md[(i, j)] for i in range(minX, maxX + 1)]) for j in range(minY, maxY + 1)]))

    def navigateMap(self, md, g, prints=False):
        history = [(g[0], g[1], md[g])]
        counter = 0
        while True:
            if prints:
                print(counter)
                self.printMap(md)
            md, g = self.takeStep(md, g)
            if g == (-1, -1):
                return [key for key in md if md[key] in ('|', '-')]
            map_state = (g[0], g[1], md[g])
            if map_state in history:
                return [(-1, -1)]
            else:
                history.append(map_state)
                counter += 1

    def testCandidate(self, md, g, candidate, prints=False):
        test_map = md.copy()
        test_map[candidate] = '#'
        return self.navigateMap(test_map, g, prints) == [(-1, -1)]

    def findRouteLength(self):
        return len(self.navigateMap(self.map_dict.copy(), self.guard))
    
    def findAllCycles(self):
        candidates = self.navigateMap(self.map_dict.copy(), self.guard)
        candidates.remove(self.guard)
        return sum([self.testCandidate(self.map_dict.copy(), self.guard, candidate) for candidate in candidates])

def part_1(guardMap):
    print('Part 1:', guardMap.findRouteLength())

def part_2(guardMap):
    print('Part 2:', guardMap.findAllCycles())

def main():
    map = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    guardMap = GuardMap(map)
    part_1(guardMap)
    part_2(guardMap)

if __name__ == '__main__':
    main()
```