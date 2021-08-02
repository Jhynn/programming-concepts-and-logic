number_1 = float(input('Type a number: '))
number_2 = float(input('Type another one: '))
number_3 = float(input('Type the last one, please: '))

if number_1 > number_2 and number_1 > number_3:
    if number_2 > number_3:
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
    else:
        print(f'{number_1} + {number_3} = {number_1 + number_3}')
elif number_2 > number_3 and number_2 > number_1:
    if number_1 > number_3:
        print(f'{number_2} + {number_1} = {number_2 + number_1}')
    else:
        print(f'{number_2} + {number_3} = {number_3 + number_2}')
else:
    if number_1 > number_2:
        print(f'{number_3} + {number_1} = {number_3 + number_1}')
    else:
        print(f'{number_3} + {number_2} = {number_2 + number_3}')
