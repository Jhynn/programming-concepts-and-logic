print('Accumulated value of a scheduled savings account')
p = float(input('Type the value of the monthly application constant: '))
i = float(input('The tax: '))
n = int(input('How many months: '))

accumulated_value = p*((1 + i)**n - 1) / i

print(f'The accumulated value is $${accumulated_value}.')
