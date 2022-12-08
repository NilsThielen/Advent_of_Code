document = open('input.txt').read().splitlines()

for i, row in enumerate(document):
    document[i] = list(row)
    for j, char in enumerate(row):
        document[i][j] = int(char)

rowLen = 99
visibilityGrid = [[0 for n in range(rowLen)] for n in range(rowLen)]

def rowsToColumns(rows):
    columns = [[0 for n in range(rowLen)] for n in range(rowLen)]
    
    for i, row in enumerate(rows):
        for j, n in enumerate(row):
            columns[j][i] = n

    return columns


def checkIterable(grid, isCol):

        for i, lis in enumerate(grid):

            for x in range(2):
                previous = [-1]
                if x == 0: iterator = enumerate(lis)
                if x == 1: iterator = reversed(list(enumerate(lis)))

                for j, n in iterator:
                    noneAreTaller = True
                    for k in previous:
                        if k >= n: noneAreTaller = False
                    previous.append(n)
                    if noneAreTaller and not isCol: visibilityGrid[i][j] = 1
                    if noneAreTaller and isCol: visibilityGrid[j][i] = 1

    
def main(grid):

    checkIterable(grid, False)
    checkIterable(rowsToColumns(grid), True)

    vizSum = 0

    for row in visibilityGrid:
        vizSum += sum(row)

    return vizSum

print(main(document))




    


