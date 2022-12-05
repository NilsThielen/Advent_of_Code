with open('input.txt') as caloriesList:
    calories = []
    document = caloriesList.read()

    for entry in document.split('\n\n'):
        calorieSum = 0
        for line in entry.split('\n'):
            calorieSum += int(line)
        calories.append(calorieSum)

    calories.sort()
    print(sum(calories[-3:]))