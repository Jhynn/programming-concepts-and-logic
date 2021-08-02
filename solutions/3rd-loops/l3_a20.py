number = int(input('Type a number, please: '))
numbers = list()

root = number ** 0.5
number = str(number)
counter = 0
odd = len(number) % 2 == 1

while counter < len(number) - 1:
    numbers.append(int(str().join(number[counter:counter + 2])))
    counter += 2

if odd:
    numbers.append(int(str().join(number[counter])))

n = [str(i) for i in numbers]
summation = ' + '.join(n)

if odd:
    summation = summation + '0'

if sum(numbers) == root:
    print(f'The sum of {summation} is equal to √{number}')
else:
    print(f'The sum of {summation} is not equal to √{number}')
