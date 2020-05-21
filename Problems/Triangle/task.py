number = int(input())
print("\n".join([("#" * (2 * x - 1)).center(2 * number - 1) for x in range(1, number + 1)]))
