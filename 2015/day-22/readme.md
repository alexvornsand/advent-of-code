### [--- Day 22: Wizard Simulator 20XX ---](https://adventofcode.com/2015/day/22)

Little Henry Case decides that defeating bosses with [swords and stuff](https://adventofcode.com/2015/day/21) is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do **magic damage**, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below `1`, it becomes `1` instead - that is, the boss' attacks always deal at least `1` damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost **mana**; you start with **500** mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

- **Magic Missile** costs `53` mana. It instantly does `4` damage.
- **Drain** costs `73` mana. It instantly does `2` damage and heals you for `2` hit points.
- **Shield** costs `113` mana. It starts an **effect** that lasts for `6` turns. While it is active, your armor is increased by `7`.
- **Poison** costs `173` mana. It starts an **effect** that lasts for `6` turns. At the start of each turn while it is active, it deals the boss `3` damage.
- **Recharge** costs `229` mana. It starts an **effect** that lasts for `5` turns. At the start of each turn while it is active, it gives you `101` new mana.

**Effects** all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has `10` hit points and `250` mana, and that the boss has `13` hit points and `8` damage:

```
-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
```
Now, suppose the same initial conditions, except that the boss has `14` hit points instead:

```
-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
```
You start with **50 hit points** and **500 mana points**. The boss's actual stats are in your puzzle input. What is the **least amount of mana** you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)

### --- Part Two ---

On the next run through the game, you increase the difficulty to **hard**.

At the start of each **player turn** (before any other effects apply), you lose `1` hit point. If this brings you to or below `0` hit points, you lose.

With the same starting stats for you and the boss, what is the **least amount of mana** you can spend and still win the fight?

### [--- Solution ---](day-22.py)
```Python
# advent of code 2015
# day 22

# part 1
rules = [int(stat.split(': ')[1]) for stat in open('input.txt', 'r').read()[:-1].split('\n')]

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
```