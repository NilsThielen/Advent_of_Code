document = open('input.txt').read().splitlines()

gridSize = 2001
segmentAmount = 10
segments = []

startPos = int(gridSize / 2)

vizGrid = [['_' for n in range(gridSize)] for n in range(gridSize)]
visitedGrid = [[0 for n in range(gridSize)] for n in range(gridSize)]

print(visitedGrid)

vizGrid[startPos][startPos] = 'H'
visitedGrid[startPos][startPos] = 1

class RopeSegment:

    def __init__(self, index, parent):
        self.index = index
        self.parent = parent
        self.pos = [startPos,startPos]

    def updateTail(self):
        if vizGrid[self.pos[0]][self.pos[1]] == 'T':
            vizGrid[self.pos[0]][self.pos[1]] = '_'

        prevSegPos = segments[self.index - 1].pos

        xDif = 0
        yDif = 0

        if prevSegPos[0] < self.pos[0]: yDif -= (self.pos[0] - prevSegPos[0])
        if prevSegPos[0] > self.pos[0]: yDif += (prevSegPos[0] - self.pos[0])
        if prevSegPos[1] < self.pos[1]: xDif -= (self.pos[1] - prevSegPos[1])
        if prevSegPos[1] > self.pos[1]: xDif += (prevSegPos[1] - self.pos[1])


        if yDif == -2: #up
            self.pos[0] -= 1 
            if xDif == 1: self.pos[1] += 1 #diagonals
            if xDif == -1: self.pos[1] -= 1

        if yDif == 2: #down
            self.pos[0] += 1 
            if xDif == 1: self.pos[1] += 1 #diagonals
            if xDif == -1: self.pos[1] -= 1

        if xDif == -2: #left
            self.pos[1] -= 1
            if yDif == 1: self.pos[0] += 1 #diagonals
            if yDif == -1: self.pos[0] -= 1

        if xDif == 2: #right
            self.pos[1] += 1
            if yDif == 1: self.pos[0] += 1 #diagonals
            if yDif == -1: self.pos[0] -= 1

        if vizGrid[self.pos[0]][self.pos[1]] == '_' or vizGrid[self.pos[0]][self.pos[1]] == 'T':
            vizGrid[self.pos[0]][self.pos[1]] = 'T'

        if self.index == segments[-1].index:
            visitedGrid[self.pos[0]][self.pos[1]] = 1

        if self.index < segmentAmount - 1:
            segments[self.index + 1].updateTail()


    def moveHead(self, move):
        dist = int(move.split(' ')[1])

        posX, posY = self.pos[1], self.pos[0]

        if 'U' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posY, self.pos[0] = posY -1, self.pos[0] -1
                vizGrid[posY][posX] = 'H'
                segments[self.index + 1].updateTail()


        if 'D' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posY, self.pos[0] = posY +1, self.pos[0] +1
                vizGrid[posY][posX] = 'H'
                segments[self.index + 1].updateTail()

            
        if 'L' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posX, self.pos[1] = posX -1, self.pos[1] -1
                vizGrid[posY][posX] = 'H'
                segments[self.index + 1].updateTail()

        if 'R' in move:
            for x in range(dist):
                vizGrid[posY][posX] = '_'
                posX, self.pos[1] = posX +1, self.pos[1] +1
                vizGrid[posY][posX] = 'H'
                segments[self.index + 1].updateTail()


def instantiateSegments():
    for x in range(segmentAmount):
        segments.append(RopeSegment(x, x-1))
        

def main(document):
    instantiateSegments()

    for move in document:
        segments[0].moveHead(move)

    visitedCellsSum = 0

    for row in visitedGrid:
        for n in row:
            visitedCellsSum += n

    return visitedCellsSum

print(main(document))
