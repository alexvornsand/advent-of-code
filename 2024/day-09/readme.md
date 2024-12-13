###[ --- Day 9: Disk Fragmenter ---](https://adventofcode.com/2024/day/9)

Another push of the button leaves you in the familiar hallways of some friendly [amphipods](https://adventofcode.com/2021/day/23)! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.

He shows you the **disk map** (your puzzle input) he's already generated. For example:

`2333133121414131402`

The disk map uses a dense format to represent the layout of **files** and **free space** on the disk. The digits alternate between indicating the length of a file and the length of free space.

So, a disk map like `12345` would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like `90909` would represent three nine-block files in a row (with no free space between them).

Each file on disk also has an **ID number** based on the order of the files as they appear **before** they are rearranged, starting with ID `0`. So, the disk map `12345` has three files: a one-block file with ID `0`, a three-block file with ID `1`, and a five-block file with ID `2`. Using one character for each block where digits are the file ID and `.` is free space, the disk map `12345` represents these individual blocks:

`0..111....22222`

The first example above, `2333133121414131402`, represents these individual blocks:

`00...111...2...333.44.5555.6666.777.888899`

The amphipod would like to **move file blocks one at a time** from the end of the disk to the leftmost free space block (until there are no gaps remaining between file blocks). For the disk map `12345`, the process looks like this:

```
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
```

The first example requires a few more steps:

```
00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............
```

The final step of this file-compacting process is to update the **filesystem checksum**. To calculate the checksum, add up the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in position `0`. If a block contains free space, skip it instead.

Continuing the first example, the first few blocks' position multiplied by its file ID number are `0 * 0 = 0`, `1 * 0 = 0`, `2 * 9 = 18`, `3 * 9 = 27`, `4 * 8 = 32`, and so on. In this example, the checksum is the sum of these, **`1928`**.

Compact the amphipod's hard drive using the process he requested. **What is the resulting filesystem checksum?** (Be careful copy/pasting the input for this puzzle; it is a single, very long line.)

### --- Part Two ---

Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that [file system fragmentation](https://en.wikipedia.org/wiki/File_system_fragmentation) was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on his disk by moving **whole files** instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of **decreasing file ID number** starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

```
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```

The process of updating the filesystem checksum is the same; now, this example's checksum would be **`2858`**.

Start over, now compacting the amphipod's hard drive using this new method instead. **What is the resulting filesystem checksum?**

### [--- Solution ---](day-09.py)
```Python
# advent of code 2024
# day 09

file = 'input.txt'

class Disk:
    def __init__(self, disk_map):
        self.disk_map = disk_map

    def defragByBit(self):
        shell = []
        for i in range(len(self.disk_map)):
            if i % 2 == 0:
                shell += [int(i / 2)] * self.disk_map[i]
            else:
                shell += [None] * self.disk_map[i]
        while None in shell:
            move = None
            while move is None:
                move = shell.pop()
            if None in shell:
                shell[shell.index(None)] = move
            else:
                shell.append(move)
        return sum([i * shell[i] for i in range(len(shell))])
    
    def defragByFile(self):
        def findOpenSpace(map, spaces, files, file_index):
            length = map[file_index]
            stack_index = 0
            while True:
                if spaces[stack_index]:
                    if stack_index >= files.index(file_index):
                        break
                    if map[spaces[stack_index]] >= length:
                        return stack_index
                stack_index += 1
            return None
        disk_map_copy = self.disk_map.copy()
        files = [i if i % 2 == 0 else None for i in range(len(self.disk_map))]
        spaces = [i if i % 2 == 1 else None for i in range(len(self.disk_map))]
        disk_map_copy.append(0)
        for file_index in [x for x in files if x][::-1]:
            stack_index_new_home = findOpenSpace(disk_map_copy, spaces, files, file_index)
            if stack_index_new_home:
                space_index = spaces[stack_index_new_home]
                disk_map_copy[space_index] -= disk_map_copy[file_index]
                if disk_map_copy[space_index] == 0:
                    files.pop(spaces.index(space_index))
                    spaces.remove(space_index)
                spaces[files.index(file_index)] = file_index
                files[files.index(file_index)] = None
                files.insert(stack_index_new_home, file_index)       
                spaces.insert(stack_index_new_home, None)
        new_files = [b for a in [[int(x / 2)] * disk_map_copy[x] if x is not None else [0] * disk_map_copy[y] for x, y in zip(files, spaces)] for b in a]
        return sum([i * new_files[i] for i in range(len(new_files))])

def part_1(disk):
    print('Part 1:', disk.defragByBit())

def part_2(disk):
    print('Part 2:', disk.defragByFile())

def main():
    disk_map = [int(x) for x in open(file, 'r').read().strip()]
    disk = Disk(disk_map)
    part_1(disk)
    part_2(disk)

if __name__ == '__main__':
    main()
```