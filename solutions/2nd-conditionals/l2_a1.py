genre = input('Please, type your genre (M or F): ')
height = float(input('And also your height: '))

if genre == 'F':
    print(f'{62.1*height - 44.7} is your ideal wheight.')

else:
    print(f'{72*height - 58} is your ideal wheight.')
