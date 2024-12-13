# advent of code 2021
# day 8

# part 1
notes = open('input.txt', 'r').read().splitlines()

def fixDisplay(notes, partTwo=False):
    def decodeDisplay(note):
        signals, output = [s.split(' ') for s in note.split(' | ')]
        segmentDict = {}
        one = [signal for signal in signals if len(signal) == 2][0]
        segmentDict[''.join(sorted(one))] = 1
        signals.remove(one)
        seven = [signal for signal in signals if len(signal) == 3][0]
        signals.remove(seven)
        segmentDict[''.join(sorted(seven))] = 7
        A = list(set([l for l in seven]).difference([l for l in one]))[0]
        four = [signal for signal in signals if len(signal) == 4][0]
        signals.remove(four)
        segmentDict[''.join(sorted(four))] = 4
        eight = [signal for signal in signals if len(signal) == 7][0]
        signals.remove(eight)
        segmentDict[''.join(sorted(eight))] = 8
        three = [signal for signal in signals if len(signal) == 5 and set([l for l in seven]).difference(set([l for l in signal])) == set()][0]
        signals.remove(three)
        segmentDict[''.join(sorted(three))] = 3
        D = list(set([l for l in four]).intersection(set([l for l in three])).difference(set([l for l in one])))[0]
        B = list(set([l for l in four]).difference(set([l for l in one])).difference(set(D)))[0]
        zero = [signal for signal in signals if set([l for l in signal]) == set([l for l in eight]).difference(set(D))][0]
        signals.remove(zero)
        segmentDict[''.join(sorted(zero))] = 0
        five = [signal for signal in signals if len(signal) == 5 and A in signal and B in signal and D in signal][0]
        signals.remove(five)
        segmentDict[''.join(sorted(five))] = 5
        two = [signal for signal in signals if len(signal) == 5][0]
        signals.remove(two)
        segmentDict[''.join(sorted(two))] = 2
        nine = [signal for signal in signals if len(set([l for l in one]).difference([l for l in signal])) == 0][0]
        signals.remove(nine)
        segmentDict[''.join(sorted(nine))] = 9
        six = signals[0]
        signals.remove(six)
        segmentDict[''.join(sorted(six))] = 6
        return([segmentDict[''.join(sorted(segment))] for segment in output])

    outputs = [decodeDisplay(note) for note in notes]
    if partTwo is False:
        return(sum([len([d for d in output if d in [1, 4, 7, 8]]) for output in outputs]))
    else:
        return(sum([int(''.join([str(d) for d in output])) for output in outputs]))

fixDisplay(notes)

# part 2
fixDisplay(notes, True)