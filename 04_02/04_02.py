document = open('input.txt')
pairs = [[list(map(int,assignment.split('-'))) for assignment in pair.split(',')] for pair in document.read().split()]

counter = 0

for pair in pairs:
    contained = False

    for assignment in pair[0]:
        if assignment >= pair[1][0] and assignment <= pair[1][1]: contained = True

    for assignment in pair[1]:
        if assignment >= pair[0][0] and assignment <= pair[0][1]: contained = True

    if contained == True: counter += 1

print(counter)
