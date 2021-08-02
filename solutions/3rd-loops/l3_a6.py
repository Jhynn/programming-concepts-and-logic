number = float(input('Type a number: '))

for n in range(1, 11):
    print(f'{number} + {n} = {number + n}\t\t{number} - {n} = {number - n}\t\t \
            {number} * {n} = {number * n}\t\t{number} / {n} = {number / n} '
    )
