# advent of code 2015
# day 22

# part 1
rules = [int(stat.split(': ')[1]) for stat in open('solutions/2015/day-22/input.txt', 'r').read().splitlines()]

def winBattle(rules, partTwo=False):
    hp, damage = rules
    def bestNextMove(attacks, damage, pHP, bHP, m, mS, sTR, pTR, rTR, best):
        if partTwo is True:
            pHP -= 1
        if pHP < 1 or mS > best:
            return(attacks, 999999)
        else:
            next_bHP = bHP
            next_sTR = sTR
            next_pTR = pTR
            next_rTR = rTR
            next_m = m
            damageSuffered = damage
            if sTR > 0:
                next_sTR -= 1
            if pTR > 0:
                next_bHP -= 3
                next_pTR -= 1
            if rTR > 0:
                next_m += 101
                next_rTR -= 1
            if bHP < 1:
                return(attacks, mS)
            attackOptions = []
            if next_m >= 53: # magic missile
                # player's turn
                sit_attacks = attacks + 'm'
                sit_m = next_m - 53
                sit_mS = mS + 53
                sit_bHP = next_bHP - 4
                if sit_bHP < 1:
                    attackOptions.append([sit_attacks, sit_mS])
                else:
                    # boss' turn
                    sit_sTR = next_sTR
                    sit_pTR = next_pTR
                    sit_rTR = next_rTR
                    sit_damageSuffered = damageSuffered
                    if sit_sTR > 0:
                        sit_damageSuffered = max(damageSuffered - 7, 1)
                        sit_sTR -= 1
                    if sit_pTR > 0:
                        sit_bHP -= 3
                        sit_pTR -= 1
                    if sit_rTR > 0:
                        sit_m += 101
                        sit_rTR -= 1     
                    if sit_bHP < 1:
                        attackOptions.append([sit_attacks, sit_mS])
                    else:
                        sit_pHP = pHP - sit_damageSuffered
                        if sit_pHP < 1:
                            attackOptions.append([sit_attacks, 999999])
                        else:
                            sit_result = bestNextMove(sit_attacks, damage, sit_pHP, sit_bHP, sit_m, sit_mS, sit_sTR, sit_pTR, sit_rTR, best)
                            if sit_result[1] < best:
                                best = sit_result[1]
                            attackOptions.append(sit_result)
            if next_m >= 73: # drain
                # player's turn
                sit_attacks = attacks + 'd'
                sit_m = next_m - 73
                sit_mS = mS + 73
                sit_bHP = next_bHP - 2
                sit_pHP = pHP + 2
                if sit_bHP < 1:
                    attackOptions.append([sit_attacks, sit_mS])
                else:
                    # boss' turn
                    sit_sTR = next_sTR
                    sit_pTR = next_pTR
                    sit_rTR = next_rTR
                    sit_damageSuffered = damageSuffered
                    if sit_sTR > 0:
                        sit_damageSuffered = max(damageSuffered - 7, 1)
                        sit_sTR -= 1
                    if sit_pTR > 0:
                        sit_bHP -= 3
                        sit_pTR -= 1
                    if sit_rTR > 0:
                        sit_m += 101
                        sit_rTR -= 1     
                    if sit_bHP < 1:
                        attackOptions.append([sit_attacks, sit_mS])
                    else:
                        sit_pHP -= sit_damageSuffered
                        if sit_pHP < 1:
                            attackOptions.append([sit_attacks, 999999])
                        else:
                            sit_result = bestNextMove(sit_attacks, damage, sit_pHP, sit_bHP, sit_m, sit_mS, sit_sTR, sit_pTR, sit_rTR, best)
                            if sit_result[1] < best:
                                best = sit_result[1]
                            attackOptions.append(sit_result)
            if next_m >= 113 and next_sTR == 0: # shield
                # player's turn
                sit_attacks = attacks + 's'
                sit_m = next_m - 113
                sit_mS = mS + 113
                sit_bHP = next_bHP
                sit_sTR = 6
                if sit_bHP < 1:
                    attackOptions.append([sit_attacks, sit_mS])
                else:
                    # boss' turn
                    sit_pTR = next_pTR
                    sit_rTR = next_rTR
                    sit_damageSuffered = damageSuffered
                    if sit_sTR > 0:
                        sit_damageSuffered = max(damageSuffered - 7, 1)
                        sit_sTR -= 1
                    if sit_pTR > 0:
                        sit_bHP -= 3
                        sit_pTR -= 1
                    if sit_rTR > 0:
                        sit_m += 101
                        sit_rTR -= 1     
                    if sit_bHP < 1:
                        attackOptions.append([sit_attacks, sit_mS])
                    else:
                        sit_pHP = pHP - sit_damageSuffered
                        if sit_pHP < 1:
                            attackOptions.append([sit_attacks, 999999])
                        else:
                            sit_result = bestNextMove(sit_attacks, damage, sit_pHP, sit_bHP, sit_m, sit_mS, sit_sTR, sit_pTR, sit_rTR, best)
                            if sit_result[1] < best:
                                best = sit_result[1]
                            attackOptions.append(sit_result)
            if next_m >= 173 and next_pTR == 0: # poison
                # player's turn
                sit_attacks = attacks + 'p'
                sit_m = next_m - 173
                sit_mS = mS + 173
                sit_bHP = next_bHP
                sit_pTR = 6
                if sit_bHP < 1:
                    attackOptions.append([sit_attacks, sit_mS])
                else:
                    # boss' turn
                    sit_sTR = next_sTR
                    sit_rTR = next_rTR
                    sit_damageSuffered = damageSuffered
                    if sit_sTR > 0:
                        sit_damageSuffered = max(damageSuffered - 7, 1)
                        sit_sTR -= 1
                    if sit_pTR > 0:
                        sit_bHP -= 3
                        sit_pTR -= 1
                    if sit_rTR > 0:
                        sit_m += 101
                        sit_rTR -= 1     
                    if sit_bHP < 1:
                        attackOptions.append([sit_attacks, sit_mS])
                    else:
                        sit_pHP = pHP - sit_damageSuffered
                        if sit_pHP < 1:
                            attackOptions.append([sit_attacks, 999999])
                        else:
                            sit_result = bestNextMove(sit_attacks, damage, sit_pHP, sit_bHP, sit_m, sit_mS, sit_sTR, sit_pTR, sit_rTR, best)
                            if sit_result[1] < best:
                                best = sit_result[1]
                            attackOptions.append(sit_result)
            if next_m >= 229 and next_rTR == 0:
                # player's turn
                sit_attacks = attacks + 'r'
                sit_m = next_m - 229
                sit_mS = mS + 229
                sit_bHP = next_bHP
                sit_rTR = 5
                if sit_bHP < 1:
                    attackOptions.append([sit_attacks, sit_mS])
                else:
                    # boss' turn
                    sit_sTR = next_sTR
                    sit_pTR = next_pTR
                    sit_damageSuffered = damageSuffered
                    if sit_sTR > 0:
                        sit_damageSuffered = max(damageSuffered - 7, 1)
                        sit_sTR -= 1
                    if sit_pTR > 0:
                        sit_bHP -= 3
                        sit_pTR -= 1
                    if sit_rTR > 0:
                        sit_m += 101
                        sit_rTR -= 1     
                    if sit_bHP < 1:
                        attackOptions.append([sit_attacks, sit_mS])
                    else:
                        sit_pHP = pHP - sit_damageSuffered
                        if sit_pHP < 1:
                            attackOptions.append([sit_attacks, 999999])
                        else:
                            sit_result = bestNextMove(sit_attacks, damage, sit_pHP, sit_bHP, sit_m, sit_mS, sit_sTR, sit_pTR, sit_rTR, best)
                            if sit_result[1] < best:
                                best = sit_result[1]
                            attackOptions.append(sit_result)
            if len(attackOptions) == 0:
                return(attacks, 999999)
            elif len(attackOptions) == 1:
                return(attackOptions[0])
            else:
                return(min(attackOptions, key=lambda o: o[1]))
    return(bestNextMove('', damage, 50, hp, 500, 0, 0, 0, 0, 999999)[0])

winBattle(rules)

# part 2
winBattle(rules, True)