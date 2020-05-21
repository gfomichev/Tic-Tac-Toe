numbers = input().split()
number = input()
indexes = [str(i) for i in range(len(numbers)) if numbers[i] == number]
print(" ".join(indexes) if len(indexes) > 0 else "not found")
