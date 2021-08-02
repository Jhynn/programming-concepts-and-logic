role = int(input('Type the code of the role: '))
name = input('What the name of the employe: ')
salary = float(input('Type the actual salary of the employe: $'))

increase_amount = 0

if role == 136:
    increase_amount = salary * 0.3
elif role == 137:
    increase_amount = salary * 0.43
elif role == 138:
    increase_amount = salary * 0.12
elif role == 139:
    increase_amount = salary * 0.33
elif role == 140:
    increase_amount = salary * 0.5
else:
    increase_amount = salary * 0.4

print(f'{name} your old salary: ${salary} and your new salary: '
      f'${salary + increase_amount}, you now receive ${increase_amount} more.'
      )
