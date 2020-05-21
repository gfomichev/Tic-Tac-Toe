nums = [int(x) for x in input()]
print([sum(nums[:i + 1]) for i, n in enumerate(nums)])
