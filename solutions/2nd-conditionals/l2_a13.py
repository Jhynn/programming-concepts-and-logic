a = float(input('Type the size of the A side: '))
b = float(input('Type the size of the B side: '))
c = float(input('Type the size of the C side: '))

if not (a + b > c and a + c > b and c + b > a):
    print('This sides cannot creates a triagle.')
else:
    if a == b and b == c and a == c:
        print('This triangle is equilateral.')
    elif a == b or b == c or a == c:
        print('This triangle is isosceles.')
    else:
        print('This triangle is scalene.')
