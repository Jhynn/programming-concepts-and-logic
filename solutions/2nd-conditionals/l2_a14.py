print('Please.')
i = int(input('Type a natural number: '))
a = float(input('Type a real number: '))
b = float(input('Type a real number: '))
c = float(input('Type a real number: '))

if i <= 0:
    print('Please, first, type a natural number!')
else:
    # Hopefully you remember that this is the solution of the problem 5.
    # Use it ─ ascending order.
    if i == 1:
        if a < b and a < c:
            if b < c:
                print(f'{a}, {b} and {c}')
            else:
                print(f'{a}, {c} and {b}')
        elif b < c and b < a:
            if a < c:
                print(f'{b}, {a} and {c}')
            else:
                print(f'{b}, {c} and {a}')
        else:
            if a < b:
                print(f'{c}, {a} and {b}')
            else:
                print(f'{c}, {b} and {a}')
    # Descending order.
    elif i == 2:
        if a > b and a > c:
            if b > c:
                print(f'{a}, {b} and {c}')
            else:
                print(f'{a}, {c} and {b}')
        elif b > c and b > a:
            if a > c:
                print(f'{b}, {a} and {c}')
            else:
                print(f'{b}, {c} and {a}')
        else:
            if a > b:
                print(f'{c}, {a} and {b}')
            else:
                print(f'{c}, {b} and {a}')
    else:
        if a > b and a > c:
            print(f'{b}, {a} and {c}')
        elif b > c and b > a:
            print(f'{a}, {b} and {c}')
        else:
            print(f'{a}, {c} and {b}')
