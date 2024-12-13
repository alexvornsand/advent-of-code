### [--- Day 4: The Ideal Stocking Stuffer ---](https://adventofcode.com/2015/day/4)

Santa needs help [mining](https://en.wikipedia.org/wiki/Bitcoin#Mining) some AdventCoins (very similar to [bitcoins](https://en.wikipedia.org/wiki/Bitcoin)) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find [MD5](https://en.wikipedia.org/wiki/MD5) hashes which, in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal), start with at least **five zeroes**. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

For example:

- If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043` starts with five zeroes (`000001dbbfa`...), and it is the lowest such number to do so.
- If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef`....

### --- Part Two ---

Now find one that starts with **six zeroes**.

### --- Solution ---
```Python
# advent of code 2015
# day 4

from hashlib import md5 as md5

file = 'input.txt'

class Key:
    def __init__(self, key):
        self.key = key
        self.index = 0

    def leading_five(self):
        while(True):
            test_key = self.key + str(self.index)
            if md5(test_key.encode()).hexdigest()[0:5] == '00000':
                return(self.index)
            else:
                self.index += 1

    def leading_six(self):
        while(True):
            test_key = self.key + str(self.index)
            if md5(test_key.encode()).hexdigest()[0:6] == '000000':
                return(self.index)
            else:
                self.index += 1

def part_1(key):
    print('Part 1:', key.leading_five(), sep = '\n')

def part_2(key):
    print('Part 2:', key.leading_six(), sep = '\n')
            
def main():
    key = Key(open(file, 'r').read().rstrip())
    part_1(key)
    part_2(key)

if __name__ == '__main__':
    main()
```