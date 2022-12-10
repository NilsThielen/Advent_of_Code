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

    if crtCol == x : crtDisplay[crtRow][crtCol] = '#'
    if crtCol == x + 1 : crtDisplay[crtRow][crtCol] = '#'
    if crtCol == x - 1 : crtDisplay[crtRow][crtCol] = '#'

    line = document[lineNum]
    
    print('instruction =', line, '\t', 'x = ',  x, '\t', 'cyc = ', cycleNum)

    if line.split(' ')[0] == 'addx':
            
            if cycleNum == addCycle:

                if int(line.split(' ')[1]) < 0:
                    x += int(line.split(' ')[1])
                    addCycle += 1
                    lineNum += 1

                elif int(line.split(' ')[1]) > 0:
                    x += int(line.split(' ')[1])
                    addCycle += 1
                    lineNum += 1


            elif cycleNum < addCycle:
                cycleNum += 1
                try: runCycle(document)
                except: return

    if line == 'noop': lineNum += 1

    addCycle += 1
    cycleNum += 1

    try: runCycle(document)
    except: return



runCycle(document)

print() 

for row in crtDisplay:
    print(''.join(row))  
print() 

# tried BGKAEREZ - right output