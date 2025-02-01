# advent of code 2020
# day 04

file = 'solutions/2020/day-04/input.txt'

class PassportScanner:
    def __init__(self, passports):
        self.passports = passports
        self.fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    def checkPassportFields(self, passport):
        response = []
        for field in self.fields[:-1]:
            if field in passport:
                if field == 'byr':
                    response.append([True, len(passport[field]) == 4 and 1920 <= int(passport[field]) <= 2002])
                elif field == 'iyr':
                    response.append([True, len(passport[field]) == 4 and 2010 <= int(passport[field]) <= 2020])
                elif field == 'eyr':
                    response.append([True, len(passport[field]) == 4 and 2020 <= int(passport[field]) <= 2030])
                elif field == 'hgt':
                    response.append([True, passport[field][-2:] in ['in', 'cm'] and (150 if passport[field][-2:] == 'cm' else 59) <= int(passport[field][:-2]) <= (193 if passport[field][-2:] == 'cm' else 76)])
                elif field == 'hcl':
                    response.append([True, passport[field][0] == '#' and len(passport[field]) == 7 and all([x.isdigit() or x in ['a', 'b', 'c', 'd', 'e', 'f'] for x in passport[field][1:]])])
                elif field == 'ecl':
                    response.append([True, passport[field] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']])   
                else:
                    response.append([True, len(passport[field]) == 9 and passport[field].isdigit()])
            else:
                response.append([False, False])
        return response

    def countValidPassports(self, detailed=True):
        return sum([all([all(field) if detailed else field[0] for field in self.checkPassportFields(passport)]) for passport in self.passports])

def part_1(passportScanner):
    print('Part 1:', passportScanner.countValidPassports(False))

def part_2(passportScanner):
    print('Part 2:', passportScanner.countValidPassports())

def main():
    passports = [{key: value for key, value in [item.split(':') for line in passport.splitlines() for item in line.split()]} for passport in open(file, 'r').read().split('\n\n')]
    passportScanner = PassportScanner(passports)
    part_1(passportScanner)
    part_2(passportScanner)

if __name__ == '__main__':
    main()