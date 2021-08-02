number = float(input('Type a number: '))
iterations = summation = 0

while number:   # 0 = False
    summation += number
    iterations += 1
    number = float(input('Type another number: '))

print(f'The average is {summation/iterations}')
