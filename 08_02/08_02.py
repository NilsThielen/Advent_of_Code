document = open('input.txt').read().splitlines()

for i, row in enumerate(document):
    document[i] = list(row)
    for j, char in enumerate(row):
        document[i][j] = int(char)

rowLen = 99
sightLineGrid = [[0 for n in range(rowLen)] for n in range(rowLen)]

def rowsToColumns(rows):
    columns = [[0 for n in range(rowLen)] for n in range(rowLen)]
    
    for i, row in enumerate(rows):
        for j, n in enumerate(row):
            columns[j][i] = n

    return columns

def checkCells(grid):
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            sightLineGrid[i][j] = calculateScore(
                checkDirection(grid, n, j, i, 'up'),
                checkDirection(grid, n, j, i, 'down'),
                checkDirection(grid, n, j, i, 'left'),
                checkDirection(grid, n, j, i, 'right')
            )

def checkDirection(grid, height, posX, posY, orientation):
    cellsInDirection= []
    dist = 0

    match orientation:
        case 'left' | 'right':
            posX, posY = posY, posX
        case 'up' | 'down':
            grid = rowsToColumns(grid)

    if orientation == 'right' or orientation == 'down':
        iterator = reversed(list(enumerate(grid[posX])))
    if orientation == 'left' or orientation == 'up':
        iterator = enumerate(grid[posX])
    

    for i, cell in iterator:
        if orientation == 'left' or orientation == 'up':
            if i < posY: cellsInDirection.append(cell)
            else: break
        if orientation == 'right' or orientation == 'down':
            if i > posY: cellsInDirection.append(cell)
            else: break

    for i, cell in reversed(list(enumerate(cellsInDirection))):
        if cell >= height:
            dist += 1
            break
        dist += 1

    return dist

def calculateScore(up, down, left, right):
    return up * down * left * right

def main(grid):

    checkCells(grid)

    highestInRow = []

    for row in sightLineGrid:
        highestInRow.append(max(row))
        print(row)
    
    highestInRow.sort()

    return highestInRow[-1]

print(main(document))



    


