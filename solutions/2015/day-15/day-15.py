# advent of code 2015
# day 15

# part 1
input = open('solutions/2015/day-15/input.txt', 'r').read()

def maximizeCookie(input, partTwo = False):
    ingredientsDict = {}
    for ing in input.split('\n'):
        ingredientsDict[ing.split(' ')[0].replace(':', '')] = {
            'capacity': int(ing.split(' ')[2].replace(',', '')),
            'durability': int(ing.split(' ')[4].replace(',', '')),
            'flavor': int(ing.split(' ')[6].replace(',', '')),
            'texture': int(ing.split(' ')[8].replace(',', '')),
            'calories': int(ing.split(' ')[10].replace(',', ''))
        }
    score = []
    for sp in range(0,101):
        for bu in range(0, 101 - sp):
            for ch in range(0, 101 - sp - bu):
                ca = 100 - sp - bu - ch
                calories = sum([
                    sp * ingredientsDict['Sprinkles']['calories'],
                    bu * ingredientsDict['Butterscotch']['calories'],
                    ch * ingredientsDict['Chocolate']['calories'],
                    ca * ingredientsDict['Candy']['calories']
                ])
                if partTwo == False or calories == 500:
                    capacity = sum([
                        sp * ingredientsDict['Sprinkles']['capacity'],
                        bu * ingredientsDict['Butterscotch']['capacity'],
                        ch * ingredientsDict['Chocolate']['capacity'],
                        ca * ingredientsDict['Candy']['capacity']
                    ])
                    capacity = max([capacity, 0])
                    durability = sum([
                        sp * ingredientsDict['Sprinkles']['durability'],
                        bu * ingredientsDict['Butterscotch']['durability'],
                        ch * ingredientsDict['Chocolate']['durability'],
                        ca * ingredientsDict['Candy']['durability']
                    ])
                    durability = max([durability, 0])
                    flavor = sum([
                        sp * ingredientsDict['Sprinkles']['flavor'],
                        bu * ingredientsDict['Butterscotch']['flavor'],
                        ch * ingredientsDict['Chocolate']['flavor'],
                        ca * ingredientsDict['Candy']['flavor']
                    ])
                    flavor = max([flavor, 0])
                    texture = sum([
                        sp * ingredientsDict['Sprinkles']['texture'],
                        bu * ingredientsDict['Butterscotch']['texture'],
                        ch * ingredientsDict['Chocolate']['texture'],
                        ca * ingredientsDict['Candy']['texture']
                    ])
                    texture = max([texture, 0])
                    score.append(capacity * durability * flavor * texture)
    return(max(score))

maximizeCookie(input)

# part 2
maximizeCookie(input, partTwo = True)

