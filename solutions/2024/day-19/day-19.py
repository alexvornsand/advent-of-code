# advent of code 2024
# day 19

from functools import cache

file = 'input.txt'

class Onsen:
    def __init__(self, towels, patterns):
        self.towels = towels
        self.patterns = patterns
        self.recipe_counts = []

    @cache
    def buildPattern(self, pattern):
        next_towels = [towel for towel in self.towels if towel == pattern[:len(towel)]]        
        valid_recipes_from_here = 0
        for towel in next_towels:
            if towel == pattern:
                valid_recipes_from_here += 1
            else:
                valid_chains = []
                next_pattern = pattern[len(towel):]
                next_chain_results = self.buildPattern(next_pattern)
                valid_chains.append(next_chain_results)
                valid_recipes_from_here += sum(valid_chains)
        return valid_recipes_from_here
            
    def findViablePatterns(self):
        self.recipe_counts = [self.buildPattern(pattern) for pattern in self.patterns]

    def countViablePatterns(self):
        return len([count for count in self.recipe_counts if count > 0])
    
    def countViableRecipes(self):
        return sum(self.recipe_counts)
    
def part_1(onsen):
    print('Part 1:', onsen.countViablePatterns())

def part_2(onsen):
    print('Part 2:', onsen.countViableRecipes())

def main():
    towels, patterns = [x.replace(', ', '\n').split('\n') for x in open(file, 'r').read().split('\n\n')]    
    onsen = Onsen(towels, patterns)
    onsen.findViablePatterns()
    part_1(onsen)
    part_2(onsen)

if __name__ == '__main__':
    main()
