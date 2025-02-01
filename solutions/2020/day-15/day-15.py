# advent of code
# day 15

# part 1
import sys
import time

input = [int(x) for x in open('input.txt', 'r').read().split()]

def play(end):
    lastPlayed = {}
    for i in range(len(input) - 1):
        lastPlayed[input[i]] = i
    next = input[-1]
    for i in range(len(input), end + 1):
        last = next
        if(last in lastPlayed.keys()):
            next = i - 1 - lastPlayed[last]
            lastPlayed[last] = i - 1
        else:
            lastPlayed[last] = i - 1
            next = 0
    print(last)

start_time = time.time()
play(2020)
end_time = time.time()
print('%s seconds' % (end_time - start_time))

# part 2
start_time = time.time()
play(30000000)
end_time = time.time()
print('%s seconds' % (end_time - start_time))
