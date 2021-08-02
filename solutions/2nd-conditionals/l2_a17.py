age = int(input('Please, type your age: '))

category = None

if age > 4 and age < 8:
    category = 'Child A'
elif age > 7 and age < 11:
    category = 'Child B'
elif age > 10 and age < 14:
    category = 'Juvenile A'
elif age > 13 and age < 18:
    category = 'Juvenile B'
else:
    category = 'Adult'

print(f'Your category is {category}.')
