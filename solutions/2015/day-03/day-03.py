# advent of code 2015
# day 3

file = 'input.txt'

class Path:
    def __init__(self):
        self.santa_cursor = [0,0]
        self.robot_cursor = [0,0]
        self.locations_visited = set([(0,0)])
        self.children_visited = len(self.locations_visited)
        
    def santa_move(self, movement):
        if movement == '^':
            shift = [0,1]
        elif movement == '>':
            shift = [1,0]
        elif movement == 'v':
            shift = [0,-1]
        elif movement == '<':
            shift = [-1,0]
        else:
            shift = [0,0]
        self.santa_cursor = [x + y for x,y in zip(self.santa_cursor, shift)]
        self.locations_visited.add(tuple(self.santa_cursor))
        self.children_visited = len(self.locations_visited)

    
    def robot_move(self, movement):
        if movement == '^':
            shift = [0,1]
        elif movement == '>':
            shift = [1,0]
        elif movement == 'v':
            shift = [0,-1]
        elif movement == '<':
            shift = [-1,0]
        else:
            shift = [0,0]
        self.robot_cursor = [x + y for x,y in zip(self.robot_cursor, shift)]
        self.locations_visited.add(tuple(self.robot_cursor))
        self.children_visited = len(self.locations_visited)

def part_1(directions):
    path = Path()
    print(path.locations_visited)
    for x in directions:
        path.santa_move(x)
    print('Part 1:', path.children_visited, sep='\n')

def part_2(directions):
    path = Path()
    print(path.locations_visited)
    i = 0
    for x in directions:
        if i % 2 == 0:
            path.santa_move(x)
            i += 1
        else:
            path.robot_move(x)
            i += 1
    print('Part 2:', path.children_visited, sep='\n')

def main():
    directions = [d for d in open(file, 'r').read().rstrip()]
    part_1(directions)
    part_2(directions)

if __name__ == '__main__':
    main()
