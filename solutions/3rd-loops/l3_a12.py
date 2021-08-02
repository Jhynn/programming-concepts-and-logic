base = float(input('Please, type the base: '))
exponent = int(input('Type the exponent: '))

power = float()

for _ in range(exponent + 1):
    power += base * base

print(f'{base} to the {exponent}th power is {power}')
