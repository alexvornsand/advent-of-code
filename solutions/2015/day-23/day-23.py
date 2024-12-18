# advent of code 2015
# day 23

# part 1
input = open('day-23.txt', 'r').read()

def runProgram(input, partTwo = False):
    lines = input.split('\n')
    i = 0
    a = 0
    b = 0
    if partTwo == True:
        a += 1
    while i in range(len(lines)):
        lineContents = lines[i].split(' ')
        if lineContents[0] == 'hlf':
            if lineContents[1] == 'a':
                a /= 2
                i += 1
            else:
                b /= 2
                i += 1
        elif lineContents[0] == 'tpl':
            if lineContents[1] == 'a':
                a *= 3
                i += 1
            else:
                b *= 3
                i += 1
        elif lineContents[0] == 'inc':
            if lineContents[1] == 'a':
                a += 1
                i += 1
            else:
                b += 1
                i += 1
        elif lineContents[0] == 'jmp':
            i += eval(lineContents[1])
        elif lineContents[0] == 'jie':
            if lineContents[1] == 'a,':
                if a % 2 == 0:
                    i += eval(lineContents[2])
                else:
                    i += 1
            else:
                if b % 2 == 0:
                    i += eval(lineContents[2])
                else:
                    i += 1
        else:
            if lineContents[1] == 'a,':
                if a == 1:
                    i += eval(lineContents[2])
                else:
                    i += 1
            else:
                if b == 1:
                    i += eval(lineContents[2])
                else:
                    i += 1
    return(b)

runProgram(input)

# part 2
runProgram(input, partTwo = True)