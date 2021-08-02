number = int(input('Please, type a number: '))
result = number ** 2

if number == 1:
    print('1³ = 1')
else:
    interactions = 0
    stop = 0

    if result % 2 == 1: # odd ─ OK
        i = result - 2
        j = result + 2
        stop = (number-1) / 2
    else:               # even
        i = result - 1
        j = result + 1
        result = 0
        stop = number / 2

    while interactions < stop:
        print(f'res.: {result} interac.: {interactions} i: {i} j: {j}')
        result += i + j
        interactions += 1
        i -= 2
        j += 2

    print(f'{number}³ = {result}')
