document = open('input.txt').read().splitlines()

gridSize = 1001
startPos = int(gridSize / 2)

vizGrid = [['_' for n in range(gridSize)] for n in range(gridSize)]
visitedGrid = [[0 for n in range(gridSize)] for n in range(gridSize)]

hPos = [startPos, startPos]

tPos = [startPos, startPos]

vizGrid[startPos][startPos] = 'H'
visitedGrid[startPos][startPos] = 1

def updateTail():
    if vizGrid[tPos[0]][tPos[1]] == 'T': vizGrid[tPos[0]][tPos[1]] = '_'

    xDif = 0
    yDif = 0

    if hPos[0] < tPos[0]: yDif -= (tPos[0] - hPos[0])
    if hPos[0] > tPos[0]: yDif += (hPos[0] - tPos[0])
    if hPos[1] < tPos[1]: xDif -= (tPos[1] - hPos[1])
    if hPos[1] > tPos[1]: xDif += (hPos[1] - tPos[1])


    if yDif == -2: #up
        tPos[0] -= 1 #diagonals
        if xDif == 1: tPos[1] += 1
        if xDif == -1: tPos[1] -= 1

    if yDif == 2: #down
        tPos[0] += 1 #diagonals
        if xDif == 1: tPos[1] += 1
        if xDif == -1: tPos[1] -= 1

    if xDif == -2: #left
        tPos[1] -= 1
        if yDif == 1: tPos[0] += 1
        if yDif == -1: tPos[0] -= 1

    if xDif == 2: #right
        tPos[1] += 1
        if yDif == 1: tPos[0] += 1
        if yDif == -1: tPos[0] -= 1

    if vizGrid[tPos[0]][tPos[1]] == '_': vizGrid[tPos[0]][tPos[1]] = 'T'
    visitedGrid[tPos[0]][tPos[1]] = 1


def moveHead(move):
        dist = int(move.split(' ')[1])

        posX, posY = hPos[1], hPos[0]

        if 'U' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posY, hPos[0] = posY -1, hPos[0] -1
                vizGrid[posY][posX] = 'H'
                updateTail()

        if 'D' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posY, hPos[0] = posY +1, hPos[0] +1
                vizGrid[posY][posX] = 'H'
                updateTail()
            
        if 'L' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posX, hPos[1] = posX -1, hPos[1] -1
                vizGrid[posY][posX] = 'H'
                updateTail()                

        if 'R' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posX, hPos[1] = posX +1, hPos[1] +1
                vizGrid[posY][posX] = 'H'
                updateTail()

def main(document):
    for move in document:
        moveHead(move)

    visitedCellsSum = 0

    for row in visitedGrid:
        for n in row:
            visitedCellsSum += n

    return visitedCellsSum

print(main(document))