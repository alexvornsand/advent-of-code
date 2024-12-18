# advent of code 2021
# day 21

# part 1
startingPositions = [int(l[-1]) for l in open('input.txt', 'r').read().rstrip().split('\n')]

def playDice(startingPositions, partTwo=False):
    def takeTurn(player, d):
        move = 0
        move += (d - 1) % 100 + 1
        d += 1
        move += (d - 1) % 100 + 1
        d += 1
        move += (d - 1) % 100 + 1
        d += 1
        player['pos'] = (player['pos'] + move - 1) % 10 + 1
        player['score'] += player['pos']
        return(player, d)
    def playDiceRecursively(players, up):
        wins = 0
        losses = 0
        # player rolls 3
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 2) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 1
            else:
                losses += 1
        else:
            int(players[abs(up - 1)]['pos'])
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 1 * futureResults[0]
            losses += 1 * futureResults[1]
        # player rolls 4
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 3) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 3
            else:
                losses += 3
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 3 * futureResults[0]
            losses += 3 * futureResults[1]
        # player rolls 5
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 4) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 6
            else:
                losses += 6
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 6 * futureResults[0]
            losses += 6 * futureResults[1]
        # player rolls 6
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 5) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 7
            else:
                losses += 7
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 7 * futureResults[0]
            losses += 7 * futureResults[1]
        # player rolls 7
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 6) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 6
            else:
                losses += 6
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 6 * futureResults[0]
            losses += 6 * futureResults[1]
        # player rolls 8
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 7) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 3
            else:
                losses += 3
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 3 * futureResults[0]
            losses += 3 * futureResults[1]
        # player rolls 9
        pos = int(players[up]['pos'])
        score = int(players[up]['score'])
        pos = (pos + 8) % 10 + 1
        score += pos
        if score >= 21:
            if up == 0:
                wins += 1
            else:
                losses += 1
        else:
            futureResults = playDiceRecursively({up: {'pos': pos, 'score': score}, abs(up - 1): {'pos': int(players[abs(up - 1)]['pos']), 'score': int(players[abs(up - 1)]['score'])}}, abs(up - 1))
            wins += 1 * futureResults[0]
            losses += 1 * futureResults[1]
        return(wins, losses)
    players = {
        0: {
            'pos': startingPositions[0],
            'score': 0
        },
        1: {
            'pos': startingPositions[1],
            'score': 0
        }
    }
    upNext = 0
    if partTwo is False:
        d = 1
        while(True):
            players[upNext], d = takeTurn(players[upNext], d)
            if players[upNext]['score'] >= 1000:
                return(players[abs(upNext - 1)]['score'] * (d - 1))
            upNext = abs(upNext - 1)
    else:
        return(max(playDiceRecursively(players, upNext)))

playDice(startingPositions)

# part 2
playDice(startingPositions, True)
