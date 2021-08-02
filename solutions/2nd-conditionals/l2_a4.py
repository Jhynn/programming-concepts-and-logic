operator = input('Type an arithmetic operator (+, -, *, /): ')
number_1 = float(input('Type an operand: '))
number_2 = float(input('Another one: '))

result = None  # Just to be visible and be used in the final instruction.

if operator == '+':
    result = number_1 + number_2

elif operator == '-':
    result = number_1 - number_2

if operator == '*':
    result = number_1 * number_2

elif operator == '/' and number_2 == 0:
    print('This is impossible.')

else:
    result = number_1 / number_2

print(f'{number_1} {operator} {number_2} = {result}')
