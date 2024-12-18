# advent of code 2022
# day 1

# part 1
foods = [[int(f) for f in b.split('\n')] for b in open('input.txt', 'r').read()[:-1].split('\n\n')]

def mostFoods(foods, partTwo=False):
    if partTwo is True:
        n = 3
    else:
        n = 1
    return(sum(sorted([sum(food) for food in foods], reverse=True)[:n]))

mostFoods(foods)

# part 2
mostFoods(foods, True)
