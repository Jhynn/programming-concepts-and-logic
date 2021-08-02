quantity = int(input('How many numbers in the sequence: '))

numbers = list()
duplicates = 0

if quantity < 2:
    print('No duplicates.')

else:
    old_value = int(input(f'Number (1 of {quantity}): '))
    numbers.append(old_value)

    for _ in range(1, quantity-1):
        actual_value = int(input(f'Number ({_+1} of {quantity+1}): '))
        numbers.append(actual_value)

        if old_value != actual_value:
            old_value = actual_value
            duplicates += 1
            continue

    if numbers[-1] != numbers[-2]:
        duplicates -= 1

print(f'The sequence have {duplicates} duplicates.')
