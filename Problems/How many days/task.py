seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
seconds_in_day = 60 * 60 * 24
print([num // seconds_in_day for num in seconds])
