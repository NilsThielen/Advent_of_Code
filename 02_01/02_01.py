with open('input.txt') as strategyGuide:
    score = 0

    for line in strategyGuide.readlines():
        line = line.strip()
        line = line.replace(' ', '')
        line = line.replace('A', 'R')
        line = line.replace('B', 'P')
        line = line.replace('C', 'S')
        line = line.replace('X', 'R')
        line = line.replace('Y', 'P')
        line = line.replace('Z', 'S')

        match line[1]:
            case 'R':
                score += 1
            case 'P':
                score += 2
            case 'S':
                score += 3

        match line:
            case 'RP' | 'PS' | 'SR':
                score += 6

        if line[0] == line[1]:
            score += 3

    print(score)

