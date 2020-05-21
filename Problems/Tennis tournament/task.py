names = [result[0] for _ in range(int(input())) for result in [input().split()] if result[1] == "win"]
print(names)
print(len(names))
