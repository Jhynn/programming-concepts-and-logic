day = int(input('Type the day: '))
month = int(input('Type the month: '))
year = int(input('Type the year: '))

if day < 1 or day > 31:
    print("Don't exist a day less than 1 and greater than 31.")
elif month == 1 or month == 3 or month == 7 or month == 8 or \
        month == 10 or month == 12:
    print(f'{day}/{month}/{year}')
elif month == 2:
    if day == 30 or day == 31:
        print('This is impossible! (30/02)')
    if day == 29:
        if (year % 100 != 0) and (year % 4 == 0 or year % 400 == 0):
            print(f'{day}/{month}/{year}')
        else:
            print('Invalid date.')
elif day == 31:
    print('Invalid date.')
else:
    print(f'{day}/{month}/{year}')
