# advent of code 2019
# day 01

# part 1
import math

masses = [int(mass) for mass in open('solutions/2019/day-01/input.txt', 'r').read().splitlines()]

def measureFuel(masses, partTwo=False):
    if partTwo is False:
        return(sum([math.floor(mass / 3) - 2 for mass in masses]))
    else:
        fuel = 0
        for mass in masses:
            outStandingMass = mass
            while(True):
                newFuel = math.floor(outStandingMass / 3) - 2
                if newFuel > 0:
                    fuel += newFuel
                    outStandingMass = newFuel
                else:
                    break
        return(fuel)

print(measureFuel(masses))

# part 2
print(measureFuel(masses, True))