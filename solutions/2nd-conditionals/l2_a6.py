name = input('Please, type your name: ')
marital_state = input('Are you married (y or n): ')

if marital_state == 'y':
    time = int(input('For how long time (in months): '))
    if time > 12:
        if time % 12 > 0:
            months = time % 24
        print(f'You have been married for {time//12} year(s) and {months} '
              'month(s), kiss and hug your beloved.', end=' ')

print(f'{name} have a nice day!')
