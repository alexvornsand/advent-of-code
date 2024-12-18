# advent of code 2022
# day 15

# part 1
import re

sensors = open('input.txt', 'r').read()[:-1].split('\n')

def analyzeSensors(sensors, partTwo=False):
    n = 2000000
    map = {}
    i = 0
    for sensor in sensors:
        coords = re.match('.*?x=(.*),.*?y=(.*):.*?x=(.*),.*?y=(.*)', sensor).groups()
        xS = int(coords[0])
        yS = int(coords[1])
        xB = int(coords[2])
        yB = int(coords[3])
        d = abs(xS - xB) + abs(yS - yB)
        if partTwo is False:
            if yS == n:
                map[(xS, yS)] = 'S'
            if yB == n:
                map[(xB, yB)] = 'B'
            excessD = d - abs(yS - n)
            if excessD >= 0:
                for x in range(xS - excessD, xS + excessD + 1):
                    if (x, n) not in map.keys():
                        map[(x, n)] = '#'
        else:
            map[i] = {
                'xS': xS,
                'yS': yS,
                'xB': xB,
                'yB': yB,
                'd': d
            }
            i += 1
    if partTwo is False:
        return(sum([map[key] == '#' for key in map]))
    else:
        def perimiterCells(map, i):
            xS = map[i]['xS']
            yS = map[i]['yS']
            origX = map[i]['xS']
            origY = map[i]['yS'] + map[i]['d'] + 1
            x = map[i]['xS']
            y = map[i]['yS'] + map[i]['d'] + 1
            coords = []
            while(True):
                coords.append((x,y))
                if x >= xS and y > yS:
                    y -= 1
                    x += 1
                elif x > xS and y <= yS:
                    x -= 1
                    y -= 1
                elif x <= xS and y < yS:
                    x -= 1
                    y += 1
                else:
                    x += 1
                    y += 1
                if x == origX and y == origY:
                    break
            return(coords)
        for s in map.keys():
            for t in map.keys():
                xS = map[s]['xS']
                yS = map[s]['yS']
                xT = map[t]['xS']
                yT = map[t]['yS']
                dS = map[s]['d']
                dT = map[t]['d']
                if abs(xS - xT) + abs(yS - yT) == dS + dT + 2:
                    sPer = perimiterCells(map, s)
                    tPer = perimiterCells(map, t)
                    candidates = list(set(sPer).intersection(tPer))
                    for candidate in candidates:
                        x = candidate[0]
                        y = candidate[1]
                        if x >= 0 and x <= 2 * n and y >= 0 and y <= 2 * n:
                            for q in map.keys():
                                if abs(x - map[q]['xS']) + abs(y - map[q]['yS']) <= map[q]['d']:
                                    break
                            else:
                                return(2 * n * x + y)
                            continue
                else:
                    continue
            else:
                continue

analyzeSensors(sensors)

# part 2
analyzeSensors(sensors, True)