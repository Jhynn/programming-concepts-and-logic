number = int(input('Enter a number: '))
summation = 0

if number < 0:
    number *= -1

for _ in range(2, int(number / 2)):
    if number % _ == 0:
        summation += _

summation += 1  # Every number is divisible by 1.

print(f'|{number}| is perfect.')
