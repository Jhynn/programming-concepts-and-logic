number_1 = float(input('Type a number: '))
number_2 = float(input('Another one, please: '))

# Probably the way that you thought...

auxiliar = number_1
number_1 = number_2
number_2 = auxiliar

print()
print(f'First number typed: {number_2}')
print(f'Second number typed: {number_1}')

# Another way to do that.

# number_1 += number_2  # number_1 = number_1 + number_2
# number_2 = (number_2 - number_1) * -1   # To normalize.
# number_1 -= number_2

# print(f'First number typed: {number_2}')
# print(f'Second number typed: {number_1}')
