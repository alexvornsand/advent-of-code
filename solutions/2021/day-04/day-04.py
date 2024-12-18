# advent of code
# day 4

# part 1
import numpy as np


calls = [int(x) for x in open('day-04.txt',
                              'r').read().split('\n\n')[0].split(',')]
cards = [np.asarray([[int(x) for x in line.split(' ') if x != ''] for line in card[:5]]) for card in [
    card.split('\n') for card in open('day-04.txt', 'r').read().split('\n\n')[1:]]]


def playBingo(calls, cards, partTwo=False):
    ncards = len(cards) - 1
    cardIndex = list(range(len(cards)))
    scores = [0] * len(cards)
    place = 0
    for call in calls:
        cards = [np.asarray([[np.nan if call == num else num for num in row]
                            for row in card]) for card in cards]
        for i in cardIndex:
            if(
                0 in np.sum(card[i], axis=0)
                or 0 in np.sum(card[i], axis=1)
            ):
                cards[i] = np.asarray(
                    [[0 if np.isnan(num) else num for num in row] for row in cards[i]])
                scores[place] = call * cards[i].sum()
                place += 1
                if(partTwo is True):
                    cardIndex.remove(i)
        if partTwo is False:
            if scores[0] > 0:
                print(max(scores))
                break
    if partTwo is True:
        print(scores[ncards])


playBingo(calls, cards)

# part 2
playBingo(calls, cards, partTwo=True)
