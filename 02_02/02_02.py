with open('input.txt') as strategyGuide:
    score = 0

    for line in strategyGuide.readlines():
        line = line.strip()
        line = line.replace(' ', '')
        line = line.replace('A', 'R')
        line = line.replace('B', 'P')
        line = line.replace('C', 'S')
        line = line.replace('X', 'L')
        line = line.replace('Y', 'D')
        line = line.replace('Z', 'W')

        choice = ''

        match line[1]:
            case 'D':
                choice = line[0]
                score += 3
            case 'W':
                if line[0] == 'R': choice = 'P'
                if line[0] == 'P': choice = 'S'
                if line[0] == 'S': choice = 'R'
                score += 6
            case 'L':
                if line[0] == 'R': choice = 'S'
                if line[0] == 'P': choice = 'R'
                if line[0] == 'S': choice = 'P'

        match choice:
            case 'R': score += 1
            case 'P': score += 2
            case 'S': score += 3

    print(score)

