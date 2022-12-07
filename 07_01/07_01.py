import random

console = open('input.txt').read().splitlines()
maxDirSize = 100000

def detectCommand(line):
    if '$' in line: return True
    else: return False
def detectCommandType(line):
    if '$ cd ..' in line: return 'move up'
    elif '$ cd /' in line: return 'move up'
    elif '$ cd' in line: return 'move in'
    if '$ ls' in line: return 'list'

def main(console):
    directories = {'root' : 0}
    currentHierarchy = ['root']
    currentDepth = 1
    smallDirsSum = 0

    for line in console:
        firstInLine = line.split(' ')[0]
        secondInLine = line.split(' ')[1]

        if detectCommand(line):
            match detectCommandType(line):
                case 'move up':
                    currentDepth -= 1
                    currentHierarchy.pop()

                case 'move in':
                    currentDepth += 1
                    keyExists = False

                    for key in directories.keys():
                        if line.split(' ')[2] in key:
                            keyExists = True

                    if keyExists:
                        genKey = str(random.randint(1000,9999))
                        directories[line.split(' ')[2] + genKey] = 0
                        currentHierarchy.append(line.split(' ')[2] + genKey)
                        
                    else:
                        directories[line.split(' ')[2]] = 0 
                        currentHierarchy.append(line.split(' ')[2])

        elif not detectCommand(line):                    
            if firstInLine.isnumeric():
                for directory in currentHierarchy:
                    directories[directory] += int(firstInLine)


    for directory in directories:
        if directories[directory]<= maxDirSize:
            smallDirsSum += directories[directory]

    return(smallDirsSum)

print(main(console))