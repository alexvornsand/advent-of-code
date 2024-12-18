# advent of code
# day 2

# part 1
directions = [(x.split(' ')[0], int(x.split(' ')[1]))
              for x in open('day-02.txt', 'r').read().split('\n')[:-1]]


def calculatePosition(directions, partTwo=False):
    if(partTwo is False):
        print(
            sum([x[1] for x in directions if x[0] == 'down']
                + [-x[1] for x in directions if x[0] == 'up'])
            * sum([x[1] for x in directions if x[0] == 'forward'])
        )
    else:
        x = 0
        z = 0
        a = 0
        for i in directions:
            if(i[0] == 'down'):
                a += i[1]
            elif(i[0] == 'up'):
                a -= i[1]
            else:
                x += i[1]
                z += a * i[1]
        print(x * z)


calculatePosition(directions)

# part 2
calculatePosition(directions, partTwo=True)
