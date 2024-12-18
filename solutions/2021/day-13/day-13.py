# advent of code
# day 13

# part 1
import numpy as np

coordinates = open('day-13.txt', 'r').read().split('\n\n')[0].split('\n')
folds = open('day-13.txt', 'r').read().split('\n\n')[1].split('\n')[:-1]


def decodePaper(coordinates, folds, partTwo=False):
    def foldPaper(page, fold):
        if 'x' in fold:
            xVal = int(fold.split('=')[1])
            return(page[:, :xVal] * page[:, :xVal:-1])
        else:
            yVal = int(fold.split('=')[1])
            return(page[:yVal, :] * page[:yVal:-1, :])
    maxX = max([int(x.split(',')[0]) for x in coordinates]) + 1
    maxY = max([int(y.split(',')[1]) for y in coordinates]) + 1
    coordPlane = np.array([1] * (maxX * maxY)).reshape((maxY, maxX))
    for coord in coordinates:
        coordPlane[int(coord.split(',')[1]), int(coord.split(',')[0])] = 0
    if partTwo is False:
        print([cell for row in foldPaper(coordPlane, folds[0])
              for cell in row].count(0))
    else:
        for fold in folds:
            coordPlane = foldPaper(coordPlane, fold)
        print('\n'.join(
            [''.join(['#' if cell == 0 else ' ' for cell in row]) for row in coordPlane]))


decodePaper(coordinates, folds)

# part 2
decodePaper(coordinates, folds, partTwo=True)
