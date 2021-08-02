alumni = list()     # or alumni = []

another_one = 'Y'
older = men = women = 0
younger = 100_000

while another_one == 'Y':
    age = float(input('Type the age of the student: '))
    alumni.append(age)

    if older < age:
        older = age
    if younger > age:
        younger = age

    genre = input('Type the age of the student (M or F): ')
    alumni.append(genre)

    if genre == 'M':
        men += 1
    elif genre == 'F':
        women += 1

    another_one = input('Do you want to sign another student (Y or N): ')

print()
print(f'Total of male students: {men}')
print(f'Total of female students: {women}')

print(f'The younger student is {younger} years old.')
print(f'The older student is {older} years old.')
