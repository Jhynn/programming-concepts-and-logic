number_1 = int(input('Type a integer number: '))
number_2 = int(input('Type another one: '))

if number_1 % number_2 == 0:
    print(f'{number_1} is a multiple of {number_2}.')
elif number_2 % number_1 == 0:
    print(f'{number_2} is a multiple of {number_1}.')
