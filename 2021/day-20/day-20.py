# advent of code 2021
# day 20

# part 1
code, image = open('input.txt', 'r').read().rstrip().split('\n\n')

def refineImage(image, code, partTwo=False):
    def gridImage(image):
        imageDict = {}
        image = [[c for c in r.strip()] for r in image.split('\n')]
        for r in range(len(image)):
            for c in range(len(image[r])):
                imageDict[(r, c)] = 1 if image[r][c] == '#' else 0
        return(imageDict)
    def printImage(imageDict):
        minY = min([key[0] for key in imageDict.keys()])
        maxY = max([key[0] for key in imageDict.keys()])
        minX = min([key[1] for key in imageDict.keys()])
        maxX = max([key[1] for key in imageDict.keys()])
        image = ''
        for r in range(minY, maxY + 1):
            for c in range(minX, maxX + 1):
                image += '#' if imageDict[(r, c)] == 1 else ' '
            image += '\n'
        print(image)
    def updatePixel(pixel, imageDict, code, default):
        r, c = pixel
        nw = str(imageDict[(r - 1, c - 1)]) if (r - 1, c - 1) in imageDict else default
        n = str(imageDict[(r - 1, c)]) if (r - 1, c) in imageDict else default
        ne = str(imageDict[(r - 1, c + 1)]) if (r - 1, c + 1) in imageDict else default
        w = str(imageDict[(r, c - 1)]) if (r, c - 1) in imageDict else default
        p = str(imageDict[(r, c)]) if (r, c) in imageDict else default
        e = str(imageDict[(r, c + 1)]) if (r, c + 1) in imageDict else default
        sw = str(imageDict[(r + 1, c - 1)]) if (r + 1, c - 1) in imageDict else default
        s = str(imageDict[(r + 1, c)]) if (r + 1, c) in imageDict else default
        se = str(imageDict[(r + 1, c + 1)]) if (r + 1, c + 1) in imageDict else default
        binIndex = nw + n + ne + w + p + e + sw + s + se
        index = int(binIndex, 2)
        return(1 if code[index] == '#' else 0)
    def updateImage(imageDict, code, default):
        minY = min([key[0] for key in imageDict.keys()])
        maxY = max([key[0] for key in imageDict.keys()])
        minX = min([key[1] for key in imageDict.keys()])
        maxX = max([key[1] for key in imageDict.keys()])
        nextDefault = str(updatePixel((99999, 99999), imageDict, code, default))
        newImage = {}
        for r in range(minY - 1, maxY + 2):
            for c in range(minX - 1, maxX + 2):
                newImage[(r, c)] = updatePixel((r, c), imageDict, code, default)
        return(newImage, nextDefault)
    picture = gridImage(image)
    default = '0'
    if partTwo is False:
        n = 2
    else: 
        n = 50
    for i in range(n):
        refinementResults = updateImage(picture, code, default)
        picture = refinementResults[0]
        default = refinementResults[1]
    return(sum(list(picture.values())))

refineImage(image, code)

# part 2
refineImage(image, code, True)