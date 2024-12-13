# advent of code 2022
# day 13

# part 1
packets = [[eval(packet) for packet in pair.split('\n')] for pair in open('input.txt', 'r').read()[:-1].split('\n\n')]

def parsePackets(packets, partTwo=False):
    def compareValues(a, b):
        if type(a) is int and type(b) is int:
            if a < b:
                return('right order')
            elif a > b:
                return('wrong order')
            else:
                return('indeterminate')
        elif type(a) is list and type(b) is list:
            i = 0
            while(True):
                if len(a) >= i + 1:
                    if len(b) >= i + 1:
                        if compareValues(a[i], b[i]) == 'indeterminate':
                            i += 1
                        else:
                            return(compareValues(a[i], b[i]))
                    else:
                        return('wrong order')
                else:
                    if len(b) >= i + 1:
                        return('right order')
                    else:
                        return('indeterminate')
        else:
            if type(a) is list:
                return(compareValues(a, [b]))
            else:
                return(compareValues([a], b))
    if partTwo is False:
        return(sum([i + 1 for i in range(len(packets)) if compareValues(packets[i][0], packets[i][1]) == 'right order']))
    else:
        allPackets = [packet for pair in packets for packet in pair]
        orderedPackets = [[[2]], [[6]]]
        for packet in allPackets:
            for i in range(len(allPackets)):
                if i == 0:
                    if compareValues(packet, orderedPackets[i]) == 'right order':
                        orderedPackets.insert(i, packet)
                        break
                    else:
                        i += 1
                elif i < len(orderedPackets):
                    if compareValues(packet, orderedPackets[i]) == 'right order' and compareValues(orderedPackets[i - 1], packet) == 'right order':
                        orderedPackets.insert(i, packet)
                        break
                    else:
                        i += 1
                else:
                    orderedPackets.append(packet)
                    break
        return((orderedPackets.index([[2]]) + 1) * (orderedPackets.index([[6]]) + 1))
        
parsePackets(packets)

# part 2
parsePackets(packets, True)