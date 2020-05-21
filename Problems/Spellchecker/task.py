dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
incorrectly_spelled = [x for x in input().split(" ") if x not in dictionary]
print("\n".join(incorrectly_spelled) if len(incorrectly_spelled) > 0 else "OK")
