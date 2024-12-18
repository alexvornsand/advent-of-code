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
