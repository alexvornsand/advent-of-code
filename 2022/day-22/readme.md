### [--- Day 22: Monkey Map ---](https://adventofcode.com/2022/day/22)

The monkeys take you on a surprisingly easy trail through the jungle. They're even going in roughly the right direction according to your handheld device's Grove Positioning System.

As you walk, the monkeys explain that the grove is protected by a **force field**. To pass through the force field, you have to enter a password; doing so involves tracing a specific **path** on a strangely-shaped board.

At least, you're pretty sure that's what you have to do; the elephants aren't exactly fluent in monkey.

The monkeys give you notes that they took when they last saw the password entered (your puzzle input).

For example:

```

        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
10R5L5R10L4R5L5
```
The first half of the monkeys' notes is a **map of the board**. It is comprised of a set of **open tiles** (on which you can move, drawn `.`) and **solid walls** (tiles which you cannot enter, drawn `#`).

The second half is a description of **the path you must follow**. It consists of alternating numbers and letters:

- A **number** indicates the **number of tiles to move** in the direction you are facing. If you run into a wall, you stop moving forward and continue with the next instruction.
- A **letter** indicates whether to turn 90 degrees **clockwise** (`R`) or **counterclockwise** (`L`). Turning happens in-place; it does not change your current tile.
So, a path like `10R5` means "go forward 10 tiles, then turn clockwise 90 degrees, then go forward 5 tiles".

You begin the path in the leftmost open tile of the top row of tiles. Initially, you are facing to the right (from the perspective of how the map is drawn).

If a movement instruction would take you off of the map, you **wrap around** to the other side of the board. In other words, if your next tile is off of the board, you should instead look in the direction opposite of your current facing as far as you can until you find the opposite edge of the board, then reappear there.

For example, if you are at `A` and facing to the right, the tile in front of you is marked `B`; if you are at `C` and facing down, the tile in front of you is marked `D`:

```
        ...#
        .#..
        #...
        ....
...#.D.....#
........#...
B.#....#...A
.....C....#.
        ...#....
        .....#..
        .#......
        ......#.
```
It is possible for the next tile (after wrapping around) to be a **wall**; this still counts as there being a wall in front of you, and so movement stops before you actually wrap to the other side of the board.

By drawing the **last facing you had** with an arrow on each tile you visit, the full path taken by the above example looks like this:

```
        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#...v..v#    
>>>v...>#.>>    
..#v...#....    
...>>>>v..#.    
        ...#....
        .....#..
        .#......
        ......#.
```
To finish providing the password to this strange input device, you need to determine numbers for your final **row**, **column**, and **facing** as your final position appears from the perspective of the original map. Rows start from 1 at the top and count downward; columns start from `1` at the left and count rightward. (In the above example, row 1, column 1 refers to the empty space with no tile on it in the top-left corner.) Facing is `0` for right (`>`), `1` for down (`v`), `2` for left (`<`), and `3` for up (`^`). The **final password** is the sum of 1000 times the row, 4 times the column, and the facing.

In the above example, the final row is `6`, the final column is `8`, and the final facing is `0`. So, the final password is 1000 * 6 + 4 * 8 + 0: **`6032`**.

Follow the path given in the monkeys' notes. **What is the final password?**

#### --- Part Two ---

As you reach the force field, you think you hear some Elves in the distance. Perhaps they've already arrived?

You approach the strange **input device**, but it isn't quite what the monkeys drew in their notes. Instead, you are met with a large **cube**; each of its six faces is a square of 50x50 tiles.

To be fair, the monkeys' map **does** have six 50x50 regions on it. If you were to **carefully fold the map**, you should be able to shape it into a cube!

In the example above, the six (smaller, 4x4) faces of the cube are:

```
        1111
        1111
        1111
        1111
222233334444
222233334444
222233334444
222233334444
        55556666
        55556666
        55556666
        55556666
```
You still start in the same position and with the same facing as before, but the **wrapping** rules are different. Now, if you would walk off the board, you instead **proceed around the cube**. From the perspective of the map, this can look a little strange. In the above example, if you are at A and move to the right, you would arrive at B facing down; if you are at C and move down, you would arrive at D facing up:

```
        ...#
        .#..
        #...
        ....
...#.......#
........#..A
..#....#....
.D........#.
        ...#..B.
        .....#..
        .#......
        ..C...#.
```
Walls still block your path, even if they are on a different face of the cube. If you are at E facing up, your movement is blocked by the wall marked by the arrow:

```
        ...#
        .#..
     -->#...
        ....
...#..E....#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.
```
Using the same method of drawing the **last facing you had** with an arrow on each tile you visit, the full path taken by the above example now looks like this:

```
        >>v#    
        .#v.    
        #.v.    
        ..v.    
...#..^...v#    
.>>>>>^.#.>>    
.^#....#....    
.^........#.    
        ...#..v.
        .....#v.
        .#v<<<<.
        ..v...#.
```
The final password is still calculated from your final position and facing from the perspective of the map. In this example, the final row is `5`, the final column is `7`, and the final facing is `3`, so the final password is 1000 * 5 + 4 * 7 + 3 = **`5031`**.

Fold the map into a cube, **then** follow the path given in the monkeys' notes. **What is the final password?**

#### [--- Solution ---](day-22.py)

```Python
# advent of code 2022
# day 22

# part 1
import re

map = [[d for d in r] for r in open('input.txt', 'r').read()[:-1].split('\n\n')[0].split('\n')]
instructions = open('input.txt', 'r').read()[:-1].split('\n\n')[1]

def navigateMap(map, instructions, partTwo=False):
    def nextTile(position, direction, mapDict, partTwo=False):
        r = position[0]
        c = position[1]
        if direction == 'U':
            if (r - 1, c) in mapDict.keys():
                if mapDict[(r - 1, c)] == 'blocked':
                    return((r, c), 'U')
                else:
                    return((r - 1, c), 'U')
            else:
                if partTwo is False:
                    if mapDict[max([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0])] == 'blocked':
                        return((r, c), 'U')
                    else:
                        return(max([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0]), 'U')
                else:
                    if c <= 50:
                        if mapDict[(c + 50, 51)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 50, 51), 'R')
                    elif c > 100:
                        if mapDict[(200, c - 100)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((200, c - 100), 'U')
                    else:
                        if mapDict[(c + 100, 1)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 100, 1), 'R')
        elif direction == 'D':
            if (r + 1, c) in mapDict.keys():
                if mapDict[(r + 1, c)] == 'blocked':
                    return((r, c), 'D')
                else:
                    return((r + 1, c), 'D')
            else:
                if partTwo is False:
                    if mapDict[min([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0])] == 'blocked':
                        return((r, c), 'D')
                    else:
                        return(min([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0]), 'D') 
                else:
                    if c <= 50:
                        if mapDict[(1, c + 100)] == 'blocked':
                            return((r, c), 'D')
                        else:
                            return((1, c + 100), 'D')
                    elif c > 100:
                        if mapDict[(c - 50, 100)] == 'blocked':
                            return((r, c), 'D')
                        else:
                            return((c - 50, 100), 'L')
                    else:
                        if mapDict[(c + 100, 50)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 100, 50), 'L')
        elif direction == 'L':
            if (r, c - 1) in mapDict.keys():
                if mapDict[(r, c - 1)] == 'blocked':
                    return((r, c), 'L')
                else:
                    return((r, c - 1), 'L')
            else:
                if partTwo is False:
                    if mapDict[max([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1])] == 'blocked':
                        return((r, c), 'L')
                    else:
                        return(max([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1]), 'L')
                else:
                    if r <= 50:
                        if mapDict[(150 - r + 1, 1)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((150 - r + 1, 1), 'R')
                    elif r <= 100:
                        if mapDict[(101, r - 50)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((101, r - 50), 'D')
                    elif r <= 150:
                        if mapDict[(150 - r + 1, 51)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((150 - r + 1, 51), 'R')
                    else:
                        if mapDict[(1, r - 100)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((1, r - 100), 'D')
        else:
            if (r, c + 1) in mapDict.keys():
                if mapDict[(r, c + 1)] == 'blocked':
                    return((r, c), 'R')
                else:
                    return((r, c + 1), 'R')
            else:
                if partTwo is False:
                    if mapDict[min([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1])] == 'blocked':
                        return((r, c), 'R')
                    else:
                        return(min([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1]), 'R')
                else:
                    if r <= 50:
                        if mapDict[(150 - r + 1, 100)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150 - r + 1, 100), 'L')
                    elif r <= 100:
                        if mapDict[(50, r + 50)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((50, r + 50), 'U')
                    elif r <= 150:
                        if mapDict[(150 - r + 1, 150)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150 - r + 1, 150), 'L')
                    else:
                        if mapDict[(150, r - 100)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150, r - 100), 'U')
    mapDict = {}
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == '.':
                mapDict[(r + 1, c + 1)] = 'open'
            elif map[r][c] == '#':
                mapDict[(r + 1,c + 1)] = 'blocked'
    directions = re.findall('\d+[UDLR]?', instructions)
    turn = {
        'R': {'R': 'D', 'L': 'U'},
        'U': {'R': 'R', 'L': 'L'},
        'D': {'R': 'L', 'L': 'R'},
        'L': {'R': 'U', 'L': 'D'}
    }
    position = min([coord for coord in mapDict.keys() if coord[0] == 1], key=lambda c: c[1])
    facing = 'R'
    facingKey = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    for direction in directions:
        last = re.fullmatch('\d+', direction) is not None
        if last is True:
            steps = int(direction)
        else:
            steps = int(direction[:-1])
        for i in range(steps):
            nextSpot, facing = nextTile(position, facing, mapDict, partTwo)
            if nextSpot == position:
                break
            else:
                position = nextSpot
        if last is False:
            turnDir = direction[-1]
            facing = turn[facing][turnDir]
    return(1000 * (position[0]) + 4 * (position[1]) + facingKey[facing])

navigateMap(map, instructions)

# part 2
navigateMap(map, instructions, True)
```