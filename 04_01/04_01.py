document = open('input.txt')
pairs = [[list(map(int,assignment.split('-'))) for assignment in pair.split(',')] for pair in document.read().split()]

counter = 0

for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]: counter+=1
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]: counter+=1

print(counter)
