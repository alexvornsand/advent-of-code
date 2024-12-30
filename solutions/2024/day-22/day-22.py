# advent of code 2024
# day 22

file = 'input.txt'

class PseudoRNGs:
    def __init__(self, seeds):
        self.seeds = seeds

    def generateNextPseudoRandomNumber(self, n):
        n = ((n << 6) ^ n) & 16777215
        n = ((n >> 5) ^ n) & 16777215
        n = ((n << 11) ^ n) & 16777215
        return n

    def generateNumbers(self, seed, n):
        seq = [seed]
        num = seed
        price = seed % 10
        delta_queue = []
        delta_chain = {}
        for _ in range(n):
            num = self.generateNextPseudoRandomNumber(num)
            price_delta = (num % 10) - price
            price = num % 10
            if len(delta_queue) == 4:
                delta_queue.pop(0)
                delta_queue.append(price_delta)
                if tuple(delta_queue) not in delta_chain:
                    delta_chain[tuple(delta_queue)] = price
            else:
                delta_queue.append(price_delta)
            seq.append(num)
        return seq, delta_chain
    
    def generatePriceNumbers(self, n=2000):
        self.sequences = []
        self.delta_chain = {}
        for seed in self.seeds:
            numbers, delta_chain = self.generateNumbers(seed, n)
            self.sequences.append(numbers)
            for key, value in delta_chain.items():
                if key in self.delta_chain:
                    self.delta_chain[key] += value
                else:
                    self.delta_chain[key] = value
    
    def sumOfLastNumber(self):
        return sum([seq[-1] for seq in self.sequences])
    
    def maximizeSalePrice(self):
        return max(self.delta_chain.values())


def part_1(pseudoRNGs):
    print('Part 1:', pseudoRNGs.sumOfLastNumber())

def part_2(pseudoRNGs):
    print('Part 2:', pseudoRNGs.maximizeSalePrice())

def main():
    seeds = [int(x) for x in open(file, 'r').read().splitlines()]    
    pseudoRNGs = PseudoRNGs(seeds)
    pseudoRNGs.generatePriceNumbers()
    part_1(pseudoRNGs)
    part_2(pseudoRNGs)

if __name__ == '__main__':
    main()