size = int(input('How many numbers do you want? '))
numbers = list()    # [7, 15, 16, 1, 30, 29, 14, 15, 22, 37]

aux, great = 0, 0

for _ in range(size):
    numbers.append(float(input(f'Type a number ({_ + 1} of {size}): ')))

for _ in range(1, size):

    if numbers[_] > numbers[_ - 1]:
        aux += 1

        if great < aux:
            great = aux + 1
    else:
        aux = 0

print(f'The most long growing series is {great}.')
print(f'The sequence {numbers}')
