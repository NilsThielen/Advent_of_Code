with open('calories.txt') as caloriesList:
    calories = []
    document = caloriesList.read()

    for entry in document.split('\n\n'):
        sum = 0
        for line in entry.split('\n'):
            sum += int(line)
        calories.append(sum)

    calories.sort()
    print(calories[-1])
