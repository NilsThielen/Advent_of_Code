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
    if cycleNum == 60: signalStrengths.append(cycleNum * x)
    if cycleNum == 100: signalStrengths.append(cycleNum * x)
    if cycleNum == 140: signalStrengths.append(cycleNum * x)
    if cycleNum == 180: signalStrengths.append(cycleNum * x)
    if cycleNum == 220: signalStrengths.append(cycleNum * x)

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
print(sum(signalStrengths)) 
print() 


# tried 14360 - right output