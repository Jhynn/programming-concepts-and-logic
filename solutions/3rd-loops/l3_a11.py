rates = list()      # Equals to: rates = []
genres = list()
ages = list()

another_one = True

while another_one:
    genre = input('Please enter your genre (either M or F): ')
    genres.append(genre)

    age = int(input('Type your age: '))
    ages.append(age)

    rate = input('You rate the product as '
                 '1-unsatisfactory 2-bad 3-regular 4-good 5-great: ')
    rates.append(rate)

    print()
    another_one = input('Do you want to add another client\'s rate (Y/N): ')
    print()

    if another_one == 'N':
        another_one = False

counter = 0
females = 0
females_40 = 0
females_50 = 0
men_rate_un = 0

while counter < len(genres):
    if genres[counter] == "F":
        females += 1

        if ages[counter] > 50 and rates[counter] == 4:
            females_50 += 1

        elif ages[counter] > 40 and rates[counter] == 4:
            females_40 += 1

    else:
        if rates[counter] == 1:
            men_rate_un += 1

    counter += 1

men = len(genres) - females

print(f'{females_40} women over 40 years old rated the product as good.')
print(f'{females_50} women over 50 years old rated the product as good.')
print(f'{men_rate_un} men rated the product as unsatisfactory.')
print(f'{females} women partipated in the survey.')
print(f'{men} men partipated in the survey.')
