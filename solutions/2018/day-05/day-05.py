# advent of code 2018
# day 05

from string import ascii_lowercase as alc

file = 'input.txt'

class Polymer:
    def __init__(self, string):
        self.string = string
        self.string_list = [c for c in string]

    def reducePolymer(self, str):
        while True:
            break_flag = True
            for i in range(len(str) - 1):
                if str[i] == str[i + 1].swapcase():
                    str[i] = ''
                    str[i + 1] = ''
                    break_flag = False
            str = [i for i in ''.join(str)]
            if break_flag:
                break
        return(len(str))
    
    def reduceStartingPolymer(self):
        return(self.reducePolymer(self.string_list.copy()))
    
    def findShortestPolymer(self):
        return(min([self.reducePolymer([a for a in self.string_list if a != c and a != c.swapcase()]) for c in alc]))
    
def part_1(polymer):
    print('Part 1:', polymer.reduceStartingPolymer())

def part_2(polymer):
    print('Part 2:', polymer.findShortestPolymer())

def main():
    polymer_string = open(file, 'r').read().strip()
    polymer = Polymer(polymer_string)
    part_1(polymer)
    part_2(polymer)

if __name__ == '__main__':
    main()
