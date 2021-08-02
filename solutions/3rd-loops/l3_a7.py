number = float(input('Type a number: '))
decreasingly = increasingly = unordered = False
previous = number

while number:
    number = float(input('Type another number: '))

    if number < previous:
        decreasingly = True
    elif number > previous:
        increasingly = True
    else:
        unordered = True

if unordered:
    print('The numbers are unordered.')
else:
    if increasingly:
        print('The numbers are ordered ─ increasingly.')
    elif decreasingly:
        print('The numbers are ordered ─ decreasingly.')
