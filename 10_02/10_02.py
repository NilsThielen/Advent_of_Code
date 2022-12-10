document = open('input.txt').read().splitlines()

cycleNum = 1
addCycle = 2
lineNum = 0
x = 1

crtDisplay = [['_' for n in range(40)] for n in range(6)]

def runCycle(document):
    global counter, x, addCycle, lineNum, cycleNum, signalStrengths

    crtCol = ((cycleNum - 1) % 40)
    crtRow = int((cycleNum - 1) / 40)

    if crtCol == x or crtCol == x-1 or crtCol == x+1 : crtDisplay[crtRow][crtCol] = '#'

    line = document[lineNum]
    
    print('instruction =', line, '\t', 'x = ',  x, '\t', 'cyc = ', cycleNum)

    if line.split(' ')[0] == 'addx':
            
            if cycleNum == addCycle:
                if int(line.split(' ')[1]) < 0: x += int(line.split(' ')[1])
                else: x += int(line.split(' ')[1])

                addCycle += 1

            elif lineNum < len(document):
                cycleNum += 1
                runCycle(document)

    lineNum += 1
    addCycle += 1
    cycleNum += 1

    if lineNum < len(document): runCycle(document)


runCycle(document)

print() 

for row in crtDisplay:
    print(''.join(row))  
print() 

# tried BGKAEREZ - right output