# advent of code 2021
# day 16

# part 1
import binascii
import math

code = open('input.txt', 'r').read().rstrip()

def decodeTransmission(code, partTwo=False):
    def parsePacket(packet):
        version = int(packet[:3], 2)
        typeID = int(packet[3:6], 2)
        if typeID == 0:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, sum(value), packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, sum(value), subpackets)
        elif typeID == 1:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, math.prod(value), packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, math.prod(value), subpackets)        
        elif typeID == 2:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, min(value), packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, min(value), subpackets)  
        elif typeID == 3:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    if partTwo is False:
                        version += ver
                    else:
                        value.append(val)
                return(version, max(value), packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, max(value), subpackets)  
        elif typeID == 4:
            literal = packet[6:]
            literalVal = ''
            i = 0
            while(literal[i] == '1'):
                literalVal += literal[i + 1:i + 5]
                i += 5
            literalVal += literal[i + 1:i + 5]
            i += 5
            return(version, int(literalVal, 2), literal[i:])
        elif typeID == 5:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] > value[1] else 0, packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] > value[1] else 0, subpackets)
        elif typeID == 6:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] < value[1] else 0, packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] < value[1] else 0, subpackets)  
        elif typeID == 7:
            lenTypeID = int(packet[6])
            if lenTypeID == 0:
                subpacketLen = int(packet[7:22], 2)
                subpackets = packet[22:(22 + subpacketLen)]
                value = []
                while(len(subpackets) > 0):
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] == value[1] else 0, packet[22 + subpacketLen:])
            elif lenTypeID == 1:
                subpacketCnt = range(int(packet[7:18], 2))
                subpackets = packet[18:]
                value = []
                for i in subpacketCnt:
                    ver, val, subpackets = parsePacket(subpackets)
                    version += ver
                    value.append(val)
                return(version, 1 if value[0] == value[1] else 0, subpackets)  
        else:
            print('PANIK!')
    translation = '0123456789ABCDEF'
    binCode = ''.join(['{0:b}'.format(translation.index(digit)).zfill(4) for digit in code])
    if partTwo is False:
        return(parsePacket(binCode)[0])       
    else:
        return(parsePacket(binCode)[1])

decodeTransmission(code)

# part 2
decodeTransmission(code, True)