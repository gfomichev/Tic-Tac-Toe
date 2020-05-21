numbers = [int(x) for x in input()]
print([(numbers[i - 1] + numbers[i]) / 2 for i in range(1, len(numbers))])
