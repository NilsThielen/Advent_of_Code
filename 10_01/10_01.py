document = open('input.txt').read().splitlines()

cycleNum = 1
addCycle = 2
lineNum = 0
x = 1

signalStrengths =  []

def runCycle(document):
    global counter, x, addCycle, lineNum, cycleNum, signalStrengths, drawCycle
    
    line = document[lineNum]
    
    print('instruction =', line, '\t', 'x = ',  x, '\t', 'cyc = ', cycleNum)

    if cycleNum == 20: signalStrengths.append(cycleNum * x)
    elif (cycleNum - 20) % 40 == 0: signalStrengths.append(cycleNum * x)

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
print(sum(signalStrengths)) 
print() 


# tried 14360 - right output