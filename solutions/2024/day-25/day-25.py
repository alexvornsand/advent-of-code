# advent of code 2024
# day 25

file = 'input.txt'

class LocksAndKeys:
    def __init__(self, tools):
        def summarizeTool(tool):
            rows = [[x for x in line] for line in tool.splitlines()]
            if all([x == '#' for x in rows[0]]):
                tool_type = 'lock'
            else:
                tool_type = 'key'
            pins = [[row[i] for row in rows].count('#') - 1 for i in range(5)]
            return [tool_type, pins]
        tools = [summarizeTool(tool) for tool in tools]
        self.keys = [tool[1] for tool in tools if tool[0] == 'key']
        self.locks = [tool[1] for tool in tools if tool[0] == 'lock']

    def countMates(self):
        count = 0
        for key in self.keys:
            for lock in self.locks:
                if all([key[i] + lock[i] <= 5 for i in range(5)]):
                    count += 1
        return count
    
def part_1(locksAndKeys):
    print('Part 1:', locksAndKeys.countMates())

def main():
    tools = open(file, 'r').read().split('\n\n')
    locksAndKeys = LocksAndKeys(tools)
    part_1(locksAndKeys)

if __name__ == '__main__':
    main()