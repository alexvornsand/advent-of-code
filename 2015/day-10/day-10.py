# advent of code 2015
# day 10

# part 1
input = open('day-10.txt', 'r').read()

def playIterativeGame(input, partTwo = False):
    string = input
    def iterate(string):
        newString = []
        for i in range(len(string)):
            if i == 0:
                val = string[0]
                count = 1
            else:
                if string[i] == string[i - 1]:
                    count += 1
                else:
                    newString.append(str(count))
                    newString.append(str(val))
                    count = 1
                    val = string[i]
        newString.append(str(count))
        newString.append(str(val))
        return(''.join(newString))
    if partTwo == False:
        for i in range(40):
            string = iterate(string)
        return(len(string))
    else:
        for i in range(50):
            string = iterate(string)
        return(len(string))

playIterativeGame(input)

# part 2
playIterativeGame(input, partTwo = True)

