# advent of code 2018
# day 24

import re

file = 'solutions/2018/day-24/input.txt'

class ImmuneSystem:
    def __init__(self, groups):
        self.groups = {key: value for key, value in groups.items()}
        for group in self.groups:
            self.groups[group]['units_remaining'] = self.groups[group]['units']
            self.groups[group]['adjusted_attack_points'] = self.groups[group]['attack_points']
            self.groups[group]['living'] = True

    def resetGroups(self):
        for group in self.groups:
            self.groups[group]['units_remaining'] = self.groups[group]['units']
            self.groups[group]['adjusted_attack_points'] = self.groups[group]['attack_points']
            self.groups[group]['living'] = True
            self.groups[group]['targeted'] = False

    def describeArmies(self):
        immune_groups = [group for group in self.groups if group[0] == '1' and self.groups[group]['living']]
        infection_groups = [group for group in self.groups if group[0] == '0' and self.groups[group]['living']]
        print('Immune System:')
        if len(immune_groups) > 0:
            for group in immune_groups:
                print('Group', self.groups[group]['group_id'], 'contains', self.groups[group]['units_remaining'], 'units' if self.groups[group]['units_remaining'] > 1 else 'unit')
        else:
            print('No groups remain.')
        print('Infection:')
        if len(infection_groups) > 0:
            for group in infection_groups:
                print('Group', self.groups[group]['group_id'], 'contains', self.groups[group]['units_remaining'], 'units' if self.groups[group]['units_remaining'] > 1 else 'unit')
        else:
            print('No groups remain.')
        print('')

    def identifyTarget(self, attacker, log=False):
        enemy_army_id = abs(attacker['army_id'] - 1)
        enemy_options = []
        for target in [group for group in self.groups if self.groups[group]['army_id'] == enemy_army_id and self.groups[group]['targeted'] is False and self.groups[group]['living'] == True]:
            attack_coefficient = 2 if attacker['attack_type'] in self.groups[target]['weaknesses'] else 0 if attacker['attack_type'] in self.groups[target]['immunities'] else 1
            effective_power = attacker['units_remaining'] * attacker['adjusted_attack_points']
            total_damage = effective_power * attack_coefficient
            if total_damage > 0:
                enemy_options.append((attack_coefficient * effective_power, self.groups[target]['units_remaining'] * self.groups[target]['adjusted_attack_points'], self.groups[target]['initiative'], self.groups[target]['unique_id'], attack_coefficient))
                if log:
                    print(attacker['subject_name'], 'group', attacker['group_id'], 'would deal defending group', self.groups[target]['group_id'], attack_coefficient * effective_power, 'damage')
        target, attack_coefficient = sorted(enemy_options, reverse=True)[0][3:] if len(enemy_options) > 0 else (None, None)
        if target:
            self.groups[target]['targeted'] = True
            return (target, attack_coefficient)
    
    def targetSelection(self, log=False):
        for group in self.groups:
            self.groups[group]['targeted'] = False
        pairings = {}
        for group in sorted([group for group in self.groups if self.groups[group]['army_id'] == 0 and self.groups[group]['living']], key=lambda x: (self.groups[x]['units_remaining'] * self.groups[x]['adjusted_attack_points'], self.groups[x]['initiative']), reverse=True):
            target = self.identifyTarget(self.groups[group], log=log)
            if target:
                pairings[group] = target
        for group in sorted([group for group in self.groups if self.groups[group]['army_id'] == 1 and self.groups[group]['living']], key=lambda x: (self.groups[x]['units_remaining'] * self.groups[x]['adjusted_attack_points'], self.groups[x]['initiative']), reverse=True):
            target = self.identifyTarget(self.groups[group], log=log)
            if target:
                pairings[group] = target
        return pairings
    
    def attacking(self, pairings, log=False):
        for group in sorted([group for group in self.groups if group in pairings], key=lambda x: self.groups[x]['initiative'], reverse=True):
            if self.groups[group]['living']:
                target, attack_coefficient = pairings[group]
                effective_power = self.groups[group]['units_remaining'] * self.groups[group]['adjusted_attack_points']
                attack_points = attack_coefficient * effective_power
                units_killed = min(self.groups[target]['units_remaining'], attack_points // self.groups[target]['hit_points'])
                units_remaining = self.groups[target]['units_remaining'] - units_killed
                if log:
                    print(self.groups[group]['subject_name'], ' group ', self.groups[group]['group_id'], ' attacks defending group', ' ', self.groups[target]['group_id'], ', killing ', units_killed, ' unit' if units_killed == 1 else ' units', sep='')
                self.groups[target]['units_remaining'] = units_remaining
                if units_remaining == 0:
                    self.groups[target]['living'] = False

    def doRoundOfBattle(self, log=False):
        if log:
            self.describeArmies()
        pairings = self.targetSelection(log=log)
        if log:
            print('')
        self.attacking(pairings, log=log)

    def goToWar(self, log=False):
        immune_alive = any([group[0] == '1' and self.groups[group]['living'] for group in self.groups]) 
        infection_alive = any([group[0] == '0' and self.groups[group]['living'] for group in self.groups])
        prev_state = [self.groups[group]['units_remaining'] for group in self.groups]
        while immune_alive and infection_alive:
            self.doRoundOfBattle(log=log)
            if log:
                print('')
            immune_alive = any([group[0] == '1' and self.groups[group]['living'] for group in self.groups]) 
            infection_alive = any([group[0] == '0' and self.groups[group]['living'] for group in self.groups])
            current_state = [self.groups[group]['units_remaining'] for group in self.groups]
            if prev_state == current_state:
                return (0, 'Infection')
            else:
                prev_state = current_state
        if log:
            self.describeArmies()
        return (sum(self.groups[group]['units_remaining'] for group in self.groups if self.groups[group]['living']), 'Immune' if immune_alive is True else 'Infection')
    
    def testImmuneBoost(self, boost, log=False):
        self.resetGroups()
        for group in [group for group in self.groups if group[0] == '1']:
            self.groups[group]['adjusted_attack_points'] += boost
        units, winner = self.goToWar(log=log)
        if winner == 'Immune':
            return True, units
        else:
            return False, units

    def findMinimumBoost(self, log=False):
        boost = 0
        while True:
            survive, units = self.testImmuneBoost(boost)
            if log:
                print('boost:', boost)
                self.describeArmies()
                print('')
            if survive:
                return units
            else:
                boost += 1
    
def part_1(immuneSystem):
    print('Part 1:', immuneSystem.goToWar()[0])

def part_2(immuneSystem):
    print('Part 2:', immuneSystem.findMinimumBoost())

def main():
    groups = {str(army_id) + '-' + str(group_id + 1): {
        'subject_name': ['Infection', 'Immune System'][army_id],
        'army_id': army_id,
        'group_id': group_id + 1,
        'unique_id': str(army_id) + '-' + str(group_id + 1),
        'units': int(re.search(r"(\d+)\sunits?", group).groups()[0]),
        'hit_points': int(re.search(r"(\d+)\shit\spoints?", group).groups()[0]),
        'weaknesses': [x.strip() for item in re.findall(r"weak\sto\s(.*?)[;\)]", group) for x in item.split(',')],
        'immunities': [x.strip() for item in re.findall(r"immune\sto\s(.*?)[;\)]", group) for x in item.split(',')],
        'attack_points': int(re.search(r"that\sdoes\s(\d+)", group).groups()[0]),
        'attack_type': re.search(r"\s(\w+?)\sdamage", group).groups()[0],
        'initiative': int(re.search(r"at\sinitiative\s(\d+)", group).groups()[0]),
        'targeted': False
    } for army_id, army in enumerate(open(file, 'r').read().split('\n\n')[::-1]) for group_id, group in enumerate(army.splitlines()[1:])}
    immuneSystem = ImmuneSystem(groups)
    part_1(immuneSystem)
    part_2(immuneSystem)

if __name__ == '__main__':
    main()