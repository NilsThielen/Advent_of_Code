letters = [chr(num) for num in range(97,97 + 26)]
letters += [chr(num) for num in range(65,65 + 26)]

document = open('input.txt').read().splitlines()
groupSize = 3
groups = [document[n:n+groupSize] for n in range(0,len(document), groupSize)]

priorities  = 0

for group in groups:
    for letter in group[0]:
        matchCount = 0

        for i in range(1, groupSize):
            
            if letter in group[i]:
                matchCount += 1

        if matchCount == groupSize - 1:
            priorities += letters.index(letter) + 1
            break

print(priorities)
