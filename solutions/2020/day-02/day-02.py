# advent of code
# day 02

file = 'solutions/2020/day-02/input.txt'

class PasswordVault:
    def __init__(self, passwords):
        self.passwords = passwords

    def checkPasswordCount(self, password):
        rule, pw = password
        rule_range, char = rule.split()
        rule_min, rule_max = [int(x) for x in rule_range.split('-')]
        count = pw.count(char)
        result = rule_min <= count <= rule_max
        return result

    def checkPasswordPosition(self, password):
        rule, pw = password
        rule_range, char = rule.split()
        rule_min, rule_max = [int(x) for x in rule_range.split('-')]
        result = sum([pw[pos - 1] == char for pos in [rule_min, rule_max]]) == 1
        return result

    def countValidPasswords(self, rule):
        if rule == 'count':
          return sum(self.checkPasswordCount(password) for password in self.passwords)
        else:
          return sum(self.checkPasswordPosition(password) for password in self.passwords)

def part_1(passwordVault):
    print('Part 1:', passwordVault.countValidPasswords('count'))

def part_2(passwordVault):
    print('Part 2:', passwordVault.countValidPasswords('position'))

def main():
    passwords = [line.split(': ') for line in open(file, 'r').read().splitlines()]
    passwordVault = PasswordVault(passwords)
    part_1(passwordVault)
    part_2(passwordVault)
  
if __name__ == '__main__':
    main()