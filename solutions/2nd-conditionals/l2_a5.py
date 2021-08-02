number_1 = float(input('Type a number: '))
number_2 = float(input('Type another one: '))
number_3 = float(input('Type the last one, please: '))

if number_1 < number_2 and number_1 < number_3:
    # number_1 is the smallest of all.
    if number_2 < number_3:
        print(f'{number_1}, {number_2} and {number_3}')
    else:
        print(f'{number_1}, {number_3} and {number_2}')
elif number_2 < number_3 and number_2 < number_1:
    # number_2 is the smallest of all.
    if number_1 < number_3:
        print(f'{number_2}, {number_1} and {number_3}')
    else:
        print(f'{number_2}, {number_3} and {number_1}')
# Since neither number_1 nor number_2 are the smallest, number3 is the smallest.
else:
    if number_1 < number_2:
        print(f'{number_3}, {number_1} and {number_2}')
    else:
        print(f'{number_3}, {number_2} and {number_1}')
