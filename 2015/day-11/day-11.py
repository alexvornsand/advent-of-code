# advent of code 2015
# day 11

# part 1
input = open('day-11.txt', 'r').read()

def findNextPassword(input, partTwo = False):
    def numberToBase(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]
    def b26NumToString(b26num):
        return(''.join([letters[x] for x in b26num]))
    def validNumber(num):
        b26num = numberToBase(num, 26)
        condA = False
        for i in range(len(b26num) - 2):
            if b26num[i + 1] == b26num[i] + 1 and b26num[i + 2] == b26num[i] + 2:
                condA = True
                break
        condB = True
        if letters.index('i') in b26num or letters.index('l') in b26num or letters.index('o') in b26num:
            condB = False
        condC = False
        condCCount = 0
        numString = b26NumToString(b26num)
        for l in letters:
            double = ''.join([l, l])
            while double in numString:
                condCCount += 1
                ind = numString.index(double)
                numStringSep = [x for x in numString]
                numStringSep[ind] = '.'
                numStringSep[ind + 1] = '.'
                numString = ''.join(numStringSep)
                if condCCount >= 2:
                    condC = True
                    break
        return(condA and condB and condC)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    startValue = sum([letters.index(input[::-1][i]) * 26 ** i for i in range(len(input[::-1]))])
    value = startValue
    while True:
        if validNumber(value):
            if partTwo == False:
                return(b26NumToString(numberToBase(value, 26)))
            else:
                value += 1
                while True:
                    if validNumber(value):
                        return(b26NumToString(numberToBase(value, 26)))
                    else:
                        value += 1
        else:
            value += 1

findNextPassword(input)

# part 2
findNextPassword(input, partTwo = True)
