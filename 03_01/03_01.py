letters = [chr(num) for num in range(97,97 + 26)]
letters += [chr(num) for num in range(65,65 + 26)]

with open('input.txt') as document:
    priorities  = 0

    for rucksack in document.read().splitlines():
        firstCompartment = [letter for letter in rucksack[:int(len(rucksack)/2)]]
        secondCompartment = [letter for letter in rucksack[int(len(rucksack)/2):]]
    
        print(firstCompartment)
        print(secondCompartment)
    
        for i in firstCompartment:
            for j in secondCompartment:
                if i == j:
                    priorities += letters.index(i) + 1
                    break
            else: continue
            break

    print(priorities)
