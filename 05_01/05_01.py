document = open('input.txt')
moves = [move.strip('move ').split(' ') for move in document.read().splitlines()]

for move in moves:
    move.remove('from')
    move.remove('to')

    for i, string in enumerate(move):
        move[i] = int(string)


stacks =[
    ['Z', 'J', 'G'],                                    # 1
    ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],           # 2
    ['F', 'P', 'M', 'C', 'L', 'G', 'R'],                # 3
    ['L', 'F', 'B', 'W', 'P', 'H', 'M'],                # 4
    ['G', 'C', 'F', 'S', 'V', 'Q'],                     # 5
    ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],           # 6
    ['H', 'F', 'S', 'B', 'V'],                          # 7
    ['F', 'J', 'Z', 'S'],                               # 8
    ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']            # 9
]


def moveCargo(amount, source, target):
    for i in range(amount):
        stacks[target-1].append(stacks[source-1].pop())

for move in moves:
    for i,  stack in enumerate(stacks):
        print(i+1, '  ', stack)
    print('\n\n')
    moveCargo(move[0], move[1], move[2])


solveString = ''
for stack in stacks:
    solveString += stack[-1]

print(solveString)