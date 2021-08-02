a = int(input('Please, type a number: '))
b = int(input('Type another number: '))

while (b != 0):
       a, b = b, a % b

print(f'The Greatest Common Divisor is {a}.')
