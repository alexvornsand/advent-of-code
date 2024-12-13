# advent of code
# day 11

# part 1

grid = open('day-11.txt', 'r').read().split('\n')[:-1]


def countFlashes(grid, partTwo=False):
    energies = dict([(str(c) + '-' + str(r), int(grid[r][c]))
                    for r in range(len(grid)) for c in range(len(grid[r]))])

    def iterateEnergy(energies):
        for octopus in energies:
            energies[octopus] = (energies[octopus] + 1) % 10
        return energies

    def chainedUpdates(energies):
        updates = True
        oldFlashers = []
        while updates:
            updates = False
            flashers = list(set([id for id, energy in energies.items(
            ) if energy == 0]).difference(set(oldFlashers)))
            if len(flashers) > 0:
                updates = True
                oldFlashers += flashers
            for octopus in flashers:
                r = int(octopus.split('-')[1])
                c = int(octopus.split('-')[0])
                neighbors = [
                    str(c + 1) + '-' + str(r),
                    str(c + 1) + '-' + str(r - 1),
                    str(c) + '-' + str(r - 1),
                    str(c - 1) + '-' + str(r - 1),
                    str(c - 1) + '-' + str(r),
                    str(c - 1) + '-' + str(r + 1),
                    str(c) + '-' + str(r + 1),
                    str(c + 1) + '-' + str(r + 1)
                ]
                for neighbor in neighbors:
                    if neighbor in energies:
                        if energies[neighbor] != 0:
                            energies[neighbor] = (energies[neighbor] + 1) % 10
        return(energies)
    flashes = 0
    if partTwo is False:
        for i in range(100):
            energies = chainedUpdates(iterateEnergy(energies))
            flashes += list(energies.values()).count(0)
        print(flashes)
    else:
        i = 0
        while True:
            i += 1
            energies = chainedUpdates(iterateEnergy(energies))
            if list(energies.values()).count(0) == 100:
                print(i)
                break


countFlashes(grid)

# part 2
countFlashes(grid, partTwo=True)
