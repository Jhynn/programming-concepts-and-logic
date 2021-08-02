denominator = int(input('Type an integer number and non-zero: '))
summation = 0

numerator = 1

while denominator:
    summation += numerator / denominator
    denominator -= 1
    numerator += 1

print(f'The summation is {summation}')
