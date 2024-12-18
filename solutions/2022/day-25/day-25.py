# advent of code 2022
# day 25

# part 1
fuels = [[-2 if d == '=' else -1 if d == '-' else int(d) for d in r] for r in open('input.txt', 'r').read()[:-1].split('\n')]

def countFuel(fuels):
    def formatNumber(number):
        digits = []
        i = 0
        remainingTotal = number
        while(True):
            digit = (remainingTotal % (5 ** (i + 1)) / (5 ** i))
            if digit > 2:
                remainingTotal -= digit * (5 ** i)
                remainingTotal += (5 ** (i + 1))
                digit -= 5
            else:
                remainingTotal -= digit * (5 ** i)
            digits.append(int(digit))
            i += 1
            if remainingTotal == 0:
                return(''.join(['=' if d == -2 else '-' if d == -1 else str(d) for d in digits[::-1]]))
    total = sum([sum([fuel[::-1][i] * (5 ** i) for i in range(len(fuel))]) for fuel in fuels])
    return(formatNumber(total))

countFuel(fuels)