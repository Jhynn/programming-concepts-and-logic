begin = int(input('Enter the begin of the range: '))
end = int(input('Enter the end of it: '))

# Note that we assume that the begin is greater than the end.
print(f'\nThe odd numbers between {begin} and {end}', end=': ')

# If begin is odd we will print it, else we go to the odd number ─ next number.
begin = begin if (begin % 2 != 0) else (begin + 1)
end += 2

greater = 0

for number in range(begin, end, 2):
    print(number, end=' ')

    if greater < number:
        greater = number
print(f"\nThe greater is {greater}")
